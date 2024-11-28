from flask import Flask, render_template, url_for

web = Flask(__name__)

@web.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    web.run(debug=True)