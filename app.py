from flask import Flask
from flask_restful import Api

from resource.todoResource import TodoResource, Todos

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'thomas'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(TodoResource, '/todo/<string:todo>')
api.add_resource(Todos, '/todos')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)
