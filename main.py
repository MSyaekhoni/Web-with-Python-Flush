from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main():
    web_title = 'Aplikasi Penghitung Usia'
    return render_template('index.html', web_title= web_title)

@app.route("/usia", methods= ['GET', 'POST'])
def cek_usia():
    tahun_sekarang = datetime.now().year
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        usia = tahun_sekarang - tahun_lahir
        return render_template('cek_usia.html', usia= usia, tahun_lahir= tahun_lahir)
    return render_template('cek_usia.html', tahun_sekarang= tahun_sekarang, usia= None)