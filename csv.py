import pandas as pd
  
data = pd.read_csv('employeedata.csv')

data.loc[data['Email_Address'] == 'something@helpinghands.cm', 'Email_Address'] = 'something@helpinghands.org'

print(data)
data.to_csv('modemployeedata.csv', index=False)


