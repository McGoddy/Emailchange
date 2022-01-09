import openpyxl as xl
import csv

exl = 'C:/Users/HP/Documents/Python Scripts/employedata.xlsx'

wb = xl.load_workbook(exl)

sheet = wb['sheet1']

old = 'helpinghands.cm'
new = 'handsinhand.org'

for i in range (2, sheet.max_row + 1):
    cell = sheet.cell(i, 2)
    if old in cell.value:
        updated_email = {cell.value}.replace(old, new)
        sheet.cell(i, 2).value = updated_email
    

wb.save('C:/Users/HP/Documents/Python Scripts/newemployeedata.xlsx')





op = open('C:/Users/HP/Documents/Python Scripts/employeedata.csv', 'r')
dt = csv.DictReader(op)
print(dt)
up_dt = []
for r in dt:
    print(r)
    row = {'Employee_Name' : r['Employe_Name'],
           'Email_Address' : r['Email_Address'].replace('helpinghands.cm', 'handsinhand.org'),
           'Phone_Number' : r['Phone_Number'],}
    up_dt.append(row)
print(up_dt)
op.close

op = open('C:/Users/HP/Documents/Python Scripts/newemployeedata.csv', 'w', newline = '')
headers = ['Employee Name', 'Email Address', 'Phone Number']
data = csv.DictWriter(op, delimiter=',', fieldnames= headers)
data.writerow(dict((heads, heads) for heads in headers))
data.writerows(up_dt)
op.close