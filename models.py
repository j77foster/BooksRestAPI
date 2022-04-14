from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class WorksModel(db.Model):
    """
    Defines the items model
    """

    __tablename__ = "works"

    #name = db.Column("name", db.String, primary_key=True)
    #price = db.Column("price", db.Integer)

    work_id = db.Column("work_id", db.Integer, primary_key=True)
    title = db.Column("title", db.VARCHAR)
    authors = db.Column("authors", db.VARCHAR)
    isbn = db.Column("isbn", db.BIGINT)
    description = db.Column("description", db.VARCHAR)




    def __init__(self, work_id, title, authors, isbn, description):
        self.work_id = work_id
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.description = description

    def __repr__(self):
        return f"<Item {self.name}>"

    @property
    def serialize(self):
        """
        Return item in serializeable format
        """
        return {"work_id": self.work_id, "title": self.title, "authors": self.authors, "isbn": self.isbn, "description": self.description}

