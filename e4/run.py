import dataset1
import pandas as pd

x = dataset1.random_x()
y = dataset1.true_function(x)
# print( y )

data = {
    '観測点': x,
    '真値': y
}

df = pd.DataFrame(data)
print( df )