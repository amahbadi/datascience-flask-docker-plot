#--------ALI AKBAR MAHBADI :aamahbadi@yahoo.com----------
from app import app,Flask, render_template, csv, os, plt, pd, np, BytesIO, base64


count = 0

def readcsv(filename, count):
    for row in open(os.path.join(os.path.dirname(__file__), filename), 'r'):
        yield row
        count += 1
        if count == 15:
            break

FILE = 'static/titanic.csv'
iter_file = iter(readcsv(FILE, count))

list_data = pd.read_csv(FILE)

def get_plot_data(field_name, list_data):
    field = list(np.array(list_data[field_name]))
    mu , sigma = np.mean(field), np.std(field)
    plt.figure()
    plt.hist(field, 50, density=True, facecolor='#FF1744', alpha=0.75)
    plt.xlabel(field_name)
    plt.ylabel('Probability')
    plt.title('Histogram of %s' %(field_name))
    plt.text(48, .03, r'$\mu={},\ \sigma={}$'.format(round(mu),round(sigma)))
    plt.grid(color='k', linestyle='--', linewidth=0.5)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    return figdata_png


@app.route('/')
def plot_data_age():
    result = get_plot_data('Age', list_data)
    return render_template('plot_age.html', result=result.decode('utf8'))

@app.route('/fare')
def plot_data_fare():
    result = get_plot_data('Fare', list_data)
    return render_template('plot_fare.html', result=result.decode('utf8'))

list_titanic = []
@app.route('/table')
def home():
    for i in iter_file:
        list_titanic.append(i.strip().split(','))
    return render_template('table.html', for_i = list_titanic)
