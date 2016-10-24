from app import db


class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    middle_name = db.Column(db.String(64), index=True)
    agency = db.Column(db.String(128), index=True)
    dept = db.Column(db.String(64))
    title = db.Column(db.String(128))
    wages = db.Column(db.Float(), index=True)
    year = db.Column(db.Integer(), index=True)

    def serialize(self):
        return {
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'agency': self.agency,
            'dept': self.dept,
            'wages': self.wages,
            'year': self.year,
            'title': self.title
        }


    def __repr__(self):
        return "<User: {0}, {1}>".format(self.last_name,
                                         self.first_name)
