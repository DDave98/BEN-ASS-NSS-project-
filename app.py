################################################
## Project: ASS/NSS API 
## Author: David Michalica, Team 1
## Date: 2024
## 
## Documentation: https://medium.com/@asvinjangid.kumar/creating-your-own-api-in-python-a-beginners-guide-59f4dd18d301
#################################################

from flask import Flask, jsonify, abort 
from config import Config
#import BussinessLayer.SensoreService
#from BussinessLayer.MultiSpectral_Camera_Controller import Multispectral_Camera_Controller
#from BussinessLayer.RGB_Camera_Controller import RGB_Camera_Controller
from BussinessLayer.SensorController import SensorController
 
# instance of flask application
app = Flask(__name__)
app.config.from_object(Config)
#from .routes import api
#app.register_blueprint(api)

# definition of confrollers
sensorController = SensorController("192.168.0.196", 40999)
#multispectral_Camera_Controller = Multispectral_Camera_Controller()
#rGB_Camera_Controller = RGB_Camera_Controller()

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/sensor/start', methods=['GET'])
def SensorStart():
    ##
    try:
        result = {
            "time": sensorController.GetSystemTime,
            "sensors": sensorController.GetSensors("001"),
            "config": sensorController.GetConfiguration("001"),
            "recording": sensorController.StartRecording("001"),
            "reader": sensorController.OpenFileReaderByName("001"),
            "reader_info": sensorController.GetFileReaderInfo("001"),
            "reader_data": sensorController.GetFileReaderData("001")
        }
        return jsonify(result)
    except:
        abort(500)

@app.route('/sensor/stop', methods=['GET'])
def SensoreStop():
    return jsonify(message='Hello, World!')
 
if __name__ == '__main__':  
   app.run(debug = True)
