import pandas as pd
import numpy as np
import math

df1 = pd.read_excel('HumaniT_Core.xlsx')
df2 = pd.read_excel('RE_Core.xlsx')

df1 = df1.sort_values(by='ref_account_id', ignore_index=True)
df2 = df2.sort_values(by='ref_account_id', ignore_index=True)

df1.equals(df2)

comparison_values = df1.values == df2.values
print(comparison_values)

rows, cols = np.where(comparison_values == False)
for item in zip(rows, cols):
    try:
        if not math.isnan(df1.iloc[item[0], item[1]]):
            # print(df1.iloc[item[0], item[1]], type(df1.iloc[item[0], item[1]]))
            df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])
    except:
        df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])


# function definition
def highlight_cols(s):
    try:
        color = 'yellow' if "-->" in s else 'white'
    except Exception as e:
        pass
    else:
        return 'background-color: % s' % color


# highlighting the cells
df1.style.applymap(highlight_cols).to_excel('./Diff_Eval_By_Sarthak.xlsx', index=False, header=True)

