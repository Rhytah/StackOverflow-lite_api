import os

from app import create_app
from api.views import app

app = create_app('development')


if __name__=='__main__':
    app.run(debug=True)