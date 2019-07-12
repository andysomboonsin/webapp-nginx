from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route('/')
def www_outage():
    message = flask.request.headers['Host']
    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
