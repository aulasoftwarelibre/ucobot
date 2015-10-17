from pony.orm import *
from ucobot.model import db

class User(db.Entity):
    """Clase User.
    Representa a un usuario de Telegram.
    """
    id = PrimaryKey(int, auto=False)
    first_name = Optional(str, nullable=True)
    last_name = Optional(str, nullable=True)
    username = Optional(str, nullable=True)

@db_session
def search_user(user):
    """
    Busca y devuelve un usuario en la base de datos. Si no existe lo crea.
    """
    if select(u for u in User).filter(lambda x: x.id == user.id).exists():
        entity = User[user.id]
        entity.first_name = user.first_name
        entity.last_name = user.last_name
        entity.username = user.username
    else:
        entity = User(id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)
        commit()

    return entity
