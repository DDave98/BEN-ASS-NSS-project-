################################################
## Project: ASS/NSS API 
## Author: David Michalica, Team 1
## Date: 2024
## 
## Documentation: https://medium.com/@asvinjangid.kumar/creating-your-own-api-in-python-a-beginners-guide-59f4dd18d301
#################################################

import os
from flask import Flask, jsonify, abort 
from config import Config

from BussinessLayer.MultiSpectral_Camera_Controller import Multispectral_Camera_Controller
#from BussinessLayer.RGB_Camera_Controller import RGB_Camera_Controller
from BussinessLayer.SensorController import SensorController
 
# instance of flask application
app = Flask(__name__)
app.config.from_object(Config)
#from .routes import api
#app.register_blueprint(api)


def GetSensorController(ip, port):
    return SensorController(ip, port)

def GetMultispecCameraController():
    return Multispectral_Camera_Controller()

def GetRGB_Camera_Controller():
    return RGB_Camera_Controller()

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
   port = int(os.environ.get('PORT', 5000))
   app.run(debug = True, host='0.0.0.0', port=port)
   # "192.168.0.196", 40999
