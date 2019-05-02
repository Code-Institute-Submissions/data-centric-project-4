from flask import Flask,render_template,request,redirect
import os,pymongo
from bson import ObjectId
app = Flask(__name__)
db_url = 'mongodb://mhelmyc:mhelmyc1234@cluster0-shard-00-00-dathk.mongodb.net:27017,cluster0-shard-00-01-dathk.mongodb.net:27017,cluster0-shard-00-02-dathk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
conn = pymongo.MongoClient(db_url)

@app.route('/')
def getindex():
    collection_recipes = conn['cookingRecipes']['recipes']
    found = list(collection_recipes.find({}))
    # for m in found:
    #     print(m)
    # found.rewind()
    collection_allergens = conn['cookingRecipes']['allergens']
    found_allergens = list(collection_allergens.find({}))
    # for a in found_allergens:
    #     print(a)
    # found_allergens.rewind()
    collection_course = conn['cookingRecipes']['course']
    found_course = list(collection_course.find({}))
    # for b in found_course:
    #     print(b)
    # found_course.rewind()
    collection_cuisine = conn['cookingRecipes']['cuisine']
    found_cuisine = list(collection_cuisine.find({}))
    # for d in found_cuisine:
    #     print(d)
    # found_cuisine.rewind()
    return render_template("index.html",collection_recipes=found,collection_allergens=found_allergens,collection_course=found_course,collection_cuisine=found_cuisine)

@app.route('/add', methods =['GET','POST'])
def addrecipe():
    if request.method =='GET':
        collection_cuisine= conn['cookingRecipes']['cuisine']
        found_cuisine =  collection_cuisine.find({})
        return render_template("add.html",collection_cuisine=found_cuisine)
    else:
        name_recipe = request.form['recipename']
        num_calories = request.form['numofcalories']
        serving_size = request.form['servingsize']
        recipe_author = request.form['recipeauthor']
        prep_time = request.form['preptime']
        cook_time = request.form['cooktime']
        instructions = request.form['instructions']
        cuisine_type = request.form['cuisinetype']
        collection_recipes = conn['cookingRecipes']['recipes']
        collection_recipes.insert({
            'name': name_recipe,
            'num_of_calories_per_serving': num_calories,
            'num_of_serving': serving_size,
            'recipe_author' : recipe_author,
            'preptime' : prep_time,
            'cooktime' : cook_time,
            'instructions' : instructions,
            'cuisine_type': cuisine_type
        })
        return redirect('/')

@app.route('/edit_recipe/<recipe_id>', methods=['GET','POST'])
def edit_recipe(recipe_id):
    collection_recipes = conn['cookingRecipes']['recipes']
    if request.method == 'GET':
        collection_from_db = collection_recipes.find_one({
            '_id': ObjectId(recipe_id)
        })
        collection_cuisine= conn['cookingRecipes']['cuisine']
        found = collection_cuisine.find({})
        return render_template('edit.html',getrecipe=collection_from_db, collection_cuisine=list(found))
    else:
        name_recipe = request.form['recipename']
        num_calories = request.form['numofcalories']
        serving_size = request.form['servingsize']
        recipe_author = request.form['recipeauthor']
        prep_time = request.form['preptime']
        cook_time = request.form['cooktime']
        instructions = request.form['instructions']
        cuisine_type = request.form['cuisinetype']
        collection_recipes.update({
            '_id':ObjectId(recipe_id)
        },{
            '$set':{
            'name': name_recipe,
            'num_of_calories_per_serving': num_calories,
            'num_of_serving': serving_size,
            'recipe_author' : recipe_author,
            'preptime' : prep_time,
            'cooktime' : cook_time,
            'instructions' : instructions,
            'cuisine_type': cuisine_type
            }
        })
        return redirect('/')
        
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    collection_recipes = conn['cookingRecipes']['recipes']
    collection_recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect('/')
    
@app.route('/base')
def home():
    return render_template("home.html")

@app.route('/layout')
def getlayout():
    return render_template("layout.html")

@app.route('/testing')
def testing():
    return "testing"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)