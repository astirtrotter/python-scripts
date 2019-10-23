import xlsxwriter
import pandas as pd

workbook = xlsxwriter.Workbook('example.xlsx')
workbook.add_worksheet()
worksheet = workbook.add_worksheet('Data')

for i in range(20):
  for j in range(20):
    worksheet.write(i, j, (i + 1) * (j + 1))

workbook.close()

print('successfully written')

##################################################

data = pd.read_excel('example.xlsx', 'Data')
df =  pd.DataFrame(data, columns=[1, 2])
print(df)