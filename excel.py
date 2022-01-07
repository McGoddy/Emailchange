import pandas as pd

data2 = pd.read_excel('employeedata.xlsx')

data2.loc[data2['Email_Address'] == 'something@helpinghands.cm', 'Email_Address'] = 'something@helpinghands.org'

print(data2)
data2.to_excel('modemployeedata.xlsx', index=False)
