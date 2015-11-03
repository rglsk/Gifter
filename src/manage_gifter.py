#!/usr/bin/env python
import os

from flask import Flask

from gifter.api.gifter_api import gifter_api


app = Flask(__name__)
app.config.from_object(os.environ.get('GIFTER_CONFIG_MODULE',
                                      'gifter.config'))
app.register_blueprint(gifter_api)


if __name__ == '__main__':
    app.run()
