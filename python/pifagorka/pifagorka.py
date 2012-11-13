#coding: utf-8
import sys; reload(sys); sys.setdefaultencoding('utf-8')

from pif_def import pif
from flask import Flask, request
app = Flask('pifagorka')
app.debug = True
# этто нелья понять, надо запомнить, важно то что вот тут:
### | Тут написано "эта функция отвечает за адрес http://имясайта/
#### \|/
@app.route('/')
def index():
    return open('index.html').read()
## ^^^ читаем и сразу показываем, да

###  |
### \|/ обработчик для адреса http://имясайта/resultat
###     адрес такой, потому что ctrl+f /resultat в index.html
@app.route('/resultat')
def resultat():
    data = request.args.get('data') # слово data берется из name="data" в index.html
    return pif(data)

### должно работать так. На глаз, не проверял, но должно.
### надо только убрать последнюю строчку (с raw_input которая) в pif_def.py

####
if __name__ == "__main__":
    app.run()
