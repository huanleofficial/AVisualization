import numpy as np
import pandas as pd
from numpy.random import randn

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(randn(6,2), hier_index, ['A', 'B'])
df.index.names = ['Group', 'Num']
print(df)

print(df.loc['G1'].loc[2]['B'])

print(df.xs(1, level = 'Num'))