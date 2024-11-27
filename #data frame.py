#data frame create
import pandas as pd

df = pd.DataFrame ({'A' : [1,2,50],
                    'B' : [5,20,8],
                    'C' : [8,4,19]})
print(df.apply(lambda x : x + 5))




