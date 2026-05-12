# フォント設定
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataset1

x_line = np.linspace(-1, 1, 100)
y_line = dataset1.true_function(x_line)

plt.figure(figsize=(8, 6))  

plt.plot(x_line, y_line, label="真の関数")

x = dataset1.random_x()
y = dataset1.true_function(x)   

df = pd.DataFrame({
    '観測点': x,
    '真値': y
})

print(df)


plt.scatter(x, y, color='red', label="サンプル点")

plt.legend()

plt.savefig("ex1.2.png")

plt.show()