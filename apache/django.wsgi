import os
import sys

sys.path.append('/home/adam/webdev/register_slc')

os.environ['DJANGO_SETTINGS_MODULE'] = 'register_slc.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
