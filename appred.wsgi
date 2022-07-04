#! /home/ubuntu/appred/env/bin python3.8
import site
site.addsitedir('/var/www/html/iilwebserver/env/lib/python3.8/site-packages')
import sys
sys.path.insert(0, '/var/www/html/iilwebserver')

from appred import app as application
application.secret_key = 'gkuotkgjbnbbfpptiuxvznametyworghghvdkkdfllorrowgcbry'