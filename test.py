import xlrd
import csv


item_list = ["foccacia", "tea", "cake", "juice"]

for item in item_list:
    print(item)

#    jabber = open("./Users/pinelopiparaskevopoulou/Desktop/sample.txt", 'r')

 #   for line in jabber:
  #      print(line)

    #jabber.close()


#book = xlrd.open_workbook("/Users/pinelopiparaskevopoulou/Desktop/python_docs/sample3.xls")
#print("The number of worksheets is {0}".format(book.nsheets))
#print("Worksheet name(s): {0}".format(book.sheet_names()))
#sh = book.sheet_by_index(0)
#print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
#print("Cell D30 is {0}".format(sh.cell_value(rowx=5, colx=3)))
#for rx in range(sh.nrows):
#    print(sh.row(rx))




# opening the CSV file

with open('/Users/pinelopiparaskevopoulou/Desktop/python_docs/sample3.csv', mode='r')as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)

