from db import db


class TodoModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(250), nullable=False)
    done = db.Column(db.String(10), nullable=False)

    def __init__(self, todo, done):
        self.todo = todo
        self.done = done

    def json(self):
        return {"Todo": self.todo, "done": self.done}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_todo(cls, todo):
        return cls.query.filter_by(todo=todo).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
