import xlrd
import csv
from datetime import datetime, timedelta
from flask import Flask, render_template
import requests
import json




#book = xlrd.open_workbook("/Users/pinelopiparaskevopoulou/Desktop/python_docs_temp/sample3.xls")
#print("The number of worksheets is {0}".format(book.nsheets))
#print("Worksheet name(s): {0}".format(book.sheet_names()))
#sh = book.sheet_by_index(0)
#print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
#print("Cell D30 is {0}".format(sh.cell_value(rowx=5, colx=3)))
#for rx in range(sh.nrows):
#    print(sh.row(rx))


app = Flask (__name__)

@app.route('/', methods = ['GET'])
def home():
    request_joke = requests.get('http://api.icndb.com/jokes/random/')
    data = json.loads(request_joke.content)
    return render_template('index.html', data = data['value'])




if __name__ == "__main__":
    app.run()



