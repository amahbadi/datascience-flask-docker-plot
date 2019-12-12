#--------ALI AKBAR MAHBADI :aamahbadi@yahoo.com----------
from app import app, render_template,os
count = 0

def readcsv(filename, count):
    for row in open(os.path.join(os.path.dirname(__file__), filename), 'r'):
        yield row
        count += 1
        if count == 15:
            break
        
FILE = 'static/titanic.csv'
iter_file = iter(readcsv(FILE, count))

list_titanic = []
for i in iter_file:
    list_titanic.append(i.strip().split(','))

@app.route('/')
def home():
    return render_template('index.html', for_i = list_titanic)
