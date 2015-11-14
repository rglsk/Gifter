#!/usr/bin/env python
from gifter import create_app


if __name__ == '__main__':
    app = create_app(config_filename='core.config')
    app.run(debug=True)
