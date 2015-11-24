#!/usr/bin/env python
from gifter import create_app

app = create_app(config_filename='core.config')

if __name__ == '__main__':
    app.run(debug=True)
