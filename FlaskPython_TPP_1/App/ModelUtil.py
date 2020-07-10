from App.ext import db

SUCCESS, FAILURE = 1, 0


class BaseModel:

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            return FAILURE
        else:
            return


    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            return FAILURE
        else:
            return SUCCESS

    @staticmethod
    def save_all(self, model_list):
        try:
            db.session.add_all(model_list)
            db.session.commit()
        except Exception as e:
            return FAILURE
        else:
            return SUCCESS
