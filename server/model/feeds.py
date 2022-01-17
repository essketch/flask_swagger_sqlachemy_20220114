from server import db

class Feeds(db.Model):
    __tablename__ = 'feeds'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lecture_id = db.Column(db.Integer)
    content = db.Column(db.TEXT, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current.timestamp())

    writer = db.relationship('Users')

    def get_data_object(self, need_writer=True):
        data = {
            'id' : self.id,
            'user_id' : self.user_id,
            'lecture_id' : self.lecture_id,
            'content' : self.content,
            'created_at' : str(self.created_at),
            'writer' : self.writer.get_data_object('name'),
        }
        if need_writer:
            data['write'] = self.writer.get_data_object()
        print(f"{self.id}번 글 작성자 : {self.writer}")
        return data