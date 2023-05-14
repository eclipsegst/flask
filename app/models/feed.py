from app import db
from dataclasses import dataclass

@dataclass
class Feed(db.Model):
    __tablename__ = 'feeds'
    id: int
    content: str

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
