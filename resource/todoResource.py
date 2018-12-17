from flask_restful import Resource, reqparse
from models.todoModel import TodoModel


class TodoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('done',
        type=str,
        required=True,
        help='This field cannot be left blank'
    )

    def get(self, todo):
        task = TodoModel.find_by_todo(todo)
        if task:
            return task.json(), 200
        return {'message': 'Task not found'}, 404

    def post(self, todo):
        if TodoModel.find_by_todo(todo):
            return {'message': 'Task with that name already exists'}, 400
        data = TodoResource.parser.parse_args()
        task = TodoModel(todo, **data)

        try:
            task.save_to_db()
        except:
            return {'message' : 'An error occured trying to insert the todo in the database'}, 500

        return task.json(), 201

    def delete(self, todo):
        task = TodoModel.find_by_todo(todo)
        if task:
            task.delete_from_db()
            return {'message': 'Task Deleted'}
        return {'message': 'Task was not found'}


class Todos(Resource):
    def get(self):
        return {'TODOS': [todo.json() for todo in TodoModel.query.all()]}
