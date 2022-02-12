from api import db


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(db.String(32))
    role = db.Column(db.String(32))

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"<User {self.id}>"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

