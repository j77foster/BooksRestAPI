import os

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
#import psycopg2
#import psycopg2.extras

from models import WorksModel

host = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
username = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASS"]
database = os.environ["POSTGRES_DB"]

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{username}:{password}@{host}:{port}/{database}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#@app.route('/items/isbn/<isbn>', methods=['GET'])
#def get_isbn(isbn):
#      item = WorksModel.query.get(isbn)
#      del item.__dict__['_sa_instance_state']
#      return jsonify(item.__dict__)

#Single work_id endpoint
@app.route('/items/id/<work_id>', methods=['GET'])
def get_id(work_id):
    if request.method == "GET":
      item = WorksModel.query.get(work_id)
      del item.__dict__['_sa_instance_state']
      return jsonify(item.__dict__)
    else:
      return {"message": "failure"}  

#Get all items 
@app.route("/items/", methods=["GET"])
def handle_items():
    if request.method == "GET":
      items = WorksModel.query.all()
      return jsonify([item.serialize for item in items])
    else:
      return {"message": "failure"}

if __name__ == "__main__":
    app.run(debug=True).query.all
