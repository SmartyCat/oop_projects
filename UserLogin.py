from flask_login import UserMixin
class UserLogin(UserMixin):
    def fromDB(self,user_id,db):
        self.__user=db.cursor().execute("SELECT * FROM users WHERE id = ? LIMIT 1",(user_id,)).fetchone()
        self.__id=user_id
        return self
    def create(self,user):
        self.__user=user
        return self
    def is_authenticate(self):
        return True
    def is_active(self):
        return True
    def is_anon(self):
        return False
    def get_id(self):
        return str(self.__user[0])