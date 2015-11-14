from manage_gifter import create_app
from gifter.models import db


if __name__ == '__main__':
    app = create_app(config_filename='core.config')
    with app.app_context():
        db.create_all()
