import sys
sys.path.insert(0,'/var/www/html/tententranslations')

with open('/home/tententranslation/.local/share/virtualenvs/tententranslations-iIwyEgeb/bin/activate_this.py','r') as file_:
    exec(file_.read(),dict(__file__='/home/tententranslation/.local/share/virtualenvs/tententranslations-iIwyEgeb/bin/activate_this.py'))

from scripts.wsgi import app as application