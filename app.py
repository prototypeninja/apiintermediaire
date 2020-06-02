from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)
@app.route('/')
def meteo():
    text = request.args.get('text')
    r = requests.get('https://0821cabf.ngrok.io/?text='+text)
    return r.text
if __name__ == "__main__":
    app.run()