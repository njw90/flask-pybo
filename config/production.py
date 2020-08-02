from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xc8\xb8\xd9\x93\xbd\x0c\xe1\xe6#\xbf\xae\xaf<J\xe8C'