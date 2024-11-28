from flask import Flask

web = Flask(__name__)

@app.route("/")
def index():
    return render_tamplate('templates\index.html')
