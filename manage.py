# manage.py

from app import app
# from index import sched
from flask_script import Manager

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
