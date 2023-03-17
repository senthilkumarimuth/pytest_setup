
"""
Pytest demo

"""

from flask import Flask
from submodule import sub

# Setting up the app
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def addition():
    try:
        c = sub.divide(100, 100)
    except Exception as e:
        c =e

    return str(c)


if __name__ == "__main__":
    app.run(port=500, debug=True)
