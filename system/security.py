from werkzeug.security import safe_str_cmp
from resources.user import UserRegister

def authenticate(username, password):
    user = UserRegister.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
