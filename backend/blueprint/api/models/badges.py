from api.db import db
import uuid


class Badges(db.Model):
    __tablename__ = 'Badges'

    image = db.Column(db.String(100), nullable=False)
    csv = db.Column(db.String(100), nullable=False)
    badge_id = db.Column(db.String(100), primary_key=True)
    text_color = db.Column(db.String(100), nullable=False)
    badge_size = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(100), db.ForeignKey('User.id', ondelete='CASCADE'))

    def save_to_db(self):
        self.badge_id = str(uuid.uuid4())
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print(e)

    @classmethod
    def getBadge(cls, badge_id):
        return cls.query.filter_by(badge_id=badge_id).first()
