from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder="static")
print("hewwo")

@app.route('/')
@app.route('/app')
def index():
	return render_template("index.html")

