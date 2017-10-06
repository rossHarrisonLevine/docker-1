#product service

from flask import flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'product': ['Ice cream',
                        'Chocolate'
                        'Fruit']
    }
api.add_resource(Product, '/')

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=80, debug=True)
