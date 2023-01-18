from pymongo import MongoClient

def connect_to_mongo():
    try:
        CONNECTION_STRING = "mongodb+srv://petu:petu@flask.gnczuux.mongodb.net/?retryWrites=true&w=majority"
        connection = MongoClient(CONNECTION_STRING)
        print("connection OK")
        return connection['flask_harjoitus']
    except Exception as e:
        print("cannot connect")
        raise e

def get_all_blogs():
    blogs_collection= db['flask_harjoitus']
    blogs = len(list(blogs_collection.find()))
    if blogs==0:
        all_blogs =[{"title": "No documents found!"}]
        return all_blogs
    else:
        all_blogs = blogs_collection.find()
        return all_blogs

def save_blog(form):
    blogs_collection = db['flask_harjoitus']
    title = form['title']
    snippet = form['snippet']
    body = form['body']

    new_blog = {"title":title, "snippet":snippet, "body":body}
    blogs_collection.insert_one(new_blog)


db = connect_to_mongo()