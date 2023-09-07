#!/usr/bin/python3
"""__init__ magic method for models directory"""


import os


types = os.environ.get("HBNB_TYPE_STORAGE")
print(types)
if types == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
