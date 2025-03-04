# import the OS and system
import os
import sys

# just like a main in C++ 
def main():
        "Run tasks"
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jukeboxjam.settings')

        try:
                from django.core.management import execute_from_command_line
        except ImportError as exc:
                raise ImportError(
                        # these strings were written by AI as a substitute for errors
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
                ) from exc
        
        execute_from_command_line(sys.argv)

        if __name__ == '__main__':
                main() 