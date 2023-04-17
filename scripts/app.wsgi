import sys
sys.path.inster(0, '/var/www/html/tententranslations/flaskbackend')
activate_this = '/home/tententranslation/.local/share/virtualenvs/flaskbackend-AtrWObps/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file.read(),dict(__file__=activate_this))

from app import create_app
application = create_app()