# フォント設定
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
import matplotlib.pyplot as plt
import dataset1
import numpy as np

x = np.linspace(-1, 1, 100)
y = dataset1.true_function(x)

plt.plot(x, y)
plt.show()