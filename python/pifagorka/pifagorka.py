#coding: utf-8

from flask import Flask
app = Flask('pifagorka')
# этто нелья понять, надо запомнить, важно то что вот тут:
### | Тут написано "эта функция отвечает за адрес http://имясайта/
#### \|/
@app.route('/')
def index():
    return open('index.html').read()
## ^^^ читаем и сразу показываем, да
####    
if __name__ == "__main__":
    app.run()