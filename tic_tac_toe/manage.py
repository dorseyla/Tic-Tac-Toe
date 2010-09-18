#!/usr/bin/env python
import sys

sys.path.append('/data')
sys.path.append('/data/django_96/')
#sys.path.append('/data/django_4150/')
#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import lathario_settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(lathario_settings)
