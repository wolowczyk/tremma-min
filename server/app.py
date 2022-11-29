from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/navigation', methods=['GET'])
def tremma_user():
    return jsonify('starting here!')


if __name__ == '__main__':
    app.run()