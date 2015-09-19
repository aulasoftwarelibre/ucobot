from pony.orm import *
from datetime import *
from ucobot import config

db = Database()

# Clases

from ucobot.model import user

# Fin clases

db.bind('sqlite', '../../config/data.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
