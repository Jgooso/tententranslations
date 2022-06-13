import sys
sys.path.insert(0,'var/www/html/tententranslations/flaskbackend')


activate_this = '/home/tententranslations/.local/share/virtualenvs/flaskbackend-AtrWObps/bin/active_this.py'
with_open(activate_this) as file_:
    exact(file.read(), dict(__file__=activate_this))

from flaskbackend import app as application