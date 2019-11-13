from arduino import db


# describe db model
class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    methane = db.Column(db.Integer)
    co = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __init__(self, methane, co, timestamp):
        self.methane = methane
        self.co = co
        self.timestamp = timestamp

    def __repr__(self):
        return "<User %r>" % self.methane
