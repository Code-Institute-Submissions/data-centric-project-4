from flask import Flask,render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/layout')
def getlayout():
    return render_template("layout.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)