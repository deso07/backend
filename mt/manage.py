<<<<<<< HEAD
=======

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
import os
import sys

def main():
<<<<<<< HEAD
=======
    """Run administrative tasks."""
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
<<<<<<< HEAD
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
=======
            "Couldn't import Django. Are you sure it's installed?"
>>>>>>> bddae2e57bd51d9b3a5c0d1ac075d0ae8df1698d
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()