import sys
import os
from pathlib import Path, PurePath
sys.path.append(str(Path(str(PurePath(Path(__file__).parents[1])) + os.sep +"src")))
from myapp import app as flask_app
import pytest


@pytest.fixture()
def app():

    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


