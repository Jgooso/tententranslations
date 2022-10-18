import re
import json
import requests
import mysql.connector
from typing import Type
from slugify import slugify
import language_tool_python
from bs4 import BeautifulSoup
from googletrans import Translator


noveldb = mysql.connector.connect(**config)
novelcursor = noveldb.cursor(buffered=True)
translator = Translator()
tool = language_tool_python.LanguageTool('en-US')


