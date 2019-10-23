import xlsxwriter

workbook = xlsxwriter.Workbook('example.xlsx')
worksheet = workbook.add_worksheet()
worksheet = workbook.add_worksheet('Data')

for i in range(20):
  for j in range(20):
    worksheet.write(i, j, (i + 1) * (j + 1))

workbook.close()