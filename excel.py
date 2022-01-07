# importing panda
import pandas as pd

# reading the data from the excel file
data2 = pd.read_excel('employeedata.xlsx')

# replacing the something@helpinghands.cm with something@helpinghands.org using the loc function
data2.loc[data2['Email_Address'] == 'something@helpinghands.cm', 'Email_Address'] = 'something@helpinghands.org'

# printing the modified document
print(data2)
# making a copy of the document so as to avoid voiding the document in case of any errors 
data2.to_excel('modemployeedata.xlsx', index=False)
