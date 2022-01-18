from server import db

class FeedImages(db.Model):
    __tablename__ = 'feeds_images'

    id = db.Column(db.Integer, primary_key=True)
    feed_id = db.Column(db.Integer, db.ForeignKey('feeds.id'))
    img_url = db.Column(db.String(200))

    def get_data_object(self):
        data = {
            'id' : self.id,
            'feed_id' : self.feed_id,
            'img_url' : self.img_url,
        }

        return data