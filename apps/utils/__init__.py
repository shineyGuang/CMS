from exts import db


class DBModel(object):
    @classmethod
    def save(cls, obj, **kwargs):
        try:
            db.session.add(obj)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False

    @classmethod
    def delete(cls, obj, **kwargs):
        try:
            db.session.delete(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return False

    @classmethod
    def update(cls):
        try:
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
