import pandas as pd
import numpy as np

data = [[1, 14890, 3], [4, 5, 6], [7, 8, 9], [11, 13, 14], [12, 0, 18], [87, None, 54], [1, 0, 3], [4, 5, 6], [7, 8, 9],
        [11, 13, 14], [12, 0, 18], [87, None, 54], [1, 0, 3], [4, 5, 6], [7, 8, 9], [11, 13, 14], [12, 0, 18],
        [87, 10026, 54]]
df = pd.DataFrame(data, columns=['column', 'data', 'something'])
df['ma'] = round(df['data'].rolling(4, 1).apply(lambda x: np.nanmean(x)), 2)
df['final2'] = np.where(df['data'] > 0, df['data'], df['ma'])
# This is nearly perfect! I modified it and now it handles all the 0s and NULLS
print(df)
