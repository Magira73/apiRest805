from ast import If
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, ressources={r"/calculTime*": {"origins": "*"}})
api = Api(app)

class CalculTime(Resource):
    def get(self, distance, nbArret, tArret):
        time = float(distance)/70.0
        if int(nbArret) > 0:
            tmp = int(tArret)*int(nbArret)
        else:
            tmp = 0        
        time = time + float(tmp)
        return {'time': time}

api.add_resource(CalculTime, '/calculTime/<distance>/<nbArret>/<tArret>')

if __name__ == '__main__':
    app.run(debug=True)

 