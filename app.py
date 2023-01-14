# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)


class Stock():
    def __init__(self, isin, name):
        self.isin = isin
        self.name = name

#MariaDB 3308 root root, fx23 dhH4387o99cma

@app.route('/')
def overview():
    list = [Stock("AT.....", "Immofinanz"), Stock("AT2020398", "S IMMO")]
    return render_template('table.html', list=list)



app.run()