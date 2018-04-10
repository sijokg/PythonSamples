#Create two excel files say mark1.xls & mark2.xls at any folder (Please modify the path at line 15 & 16 accordingly)
# And add sample values like below

#mark1.xls samples
# [1 2 3]
# [4 5 6]
# [7 8 9]
# [10 11 12]

#mark2.xls samples
# [1 2]
# [1 2]
# [3 4]

import xlrd
mark1_file="/MatrixMultiplicationPython/mark1.xls"
mark2_file="/MatrixMultiplicationPython/mark2.xls"

x1 = []
x2 = []
for file_number in range(1, 3):
  print(f'Hello {file_number}')
  wkb=xlrd.open_workbook(eval("mark"+str(file_number)+"_file"))
  sheet=wkb.sheet_by_index(0)
  for row in range (sheet.nrows):
    _row = []
    for col in range (sheet.ncols):
       _row.append(sheet.cell_value(row,col))
    eval("x"+str(file_number)).append(_row)
import numpy as np 

mx = np.matrix(x1)
my = np.matrix(x2)

print(mx * my)
