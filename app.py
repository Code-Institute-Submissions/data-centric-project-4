from flask import Flask,render_template,request,redirect
import os,pymongo
app = Flask(__name__)
db_url = 'mongodb://mhelmyc:mhelmyc1234@cluster0-shard-00-00-dathk.mongodb.net:27017,cluster0-shard-00-01-dathk.mongodb.net:27017,cluster0-shard-00-02-dathk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
conn = pymongo.MongoClient(db_url)

@app.route('/')
def getindex():
    collection = conn['cookingRecipes']['recipes']
    found = list(collection.find({}))
    # for m in found:
    #     print(m)
    # found.rewind()
    return render_template("index.html",collection=found)
    
@app.route('/base')
def home():
    return render_template("home.html")

@app.route('/layout')
def getlayout():
    return render_template("layout.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)