/var/www/html/adapter.wsgi
# coding: utf-8
import sys
sys.path.insert(0, '/var/www/tatekan/app')

from main import app as application