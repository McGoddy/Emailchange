# importing panda
import pandas as pd

# reading the data from the csv file
data = pd.read_csv('employeedata.csv')

# replacing the something@helpinghands.cm with something@helpinghands.org using the loc function
data.loc[data['Email_Address'] == 'something@helpinghands.cm', 'Email_Address'] = 'something@helpinghands.org'

# printing the modified document
print(data)
# making a copy of the document so as to avoid voiding the document in case of any errors 
data.to_csv('modemployeedata.csv', index=False)


