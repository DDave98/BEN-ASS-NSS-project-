################################################
## Project: ASS/NSS API 
## Author: David Michalica, Team 1
## Date: 2024
## 
## Documentation: https://bitbucket.org/dakel/node-zedo-rpc/src/master/API.md
## alternativni knihovny pro py: pyro4, xmlrpc.server, jsonrpcserver, zerorpc
#################################################

import socket
import threading
import time
import json

class SensorController:

    methods =  {
        "GRFN": "generate_rec_folder_name",
        "CV": "compare_versions",
        "AMV": "assert_min_version",
        "CJ": "copy_json",
        "PJ": "print_json",
        "IJO": "is_json_object",
        "MJ": "merge_json",
        "IZD": "is_zdat_directory",
        "GS": "GetSensors",
        "GSS": "GetSystemStatus",
        "GST": "GetSystemTime",
        "GC": "GetConfiguration",
        "C": "Configure",
        "CLD": "ClearLiveData",
        "SR": "StartRecording",
        "PR": "PauseRecording",
        "StR": "StopRecording",
        "GRS": "GetRecordingState",
        "GAI": "GetAppInfo",
        "GAP": "GetActivePulsers",
        "APO": "AllPulsersOff",
        "PCS": "pulser_configs_same",
        "SP": "SetPulser",
        "ECR": "EnableContinuousRecording",
        "OFRBP": "OpenFileReaderByPath",
        "OFRBN": "OpenFileReaderByName",
        "SFRP": "SetFileReaderPath",
        "GFRI": "GetFileReaderInfo",
        "GFRD": "GetFileReaderData",
        "EFRD": "ExportFileReaderData",
        "EI": "ExportItems",
        "CGP": "CaptureGraphPictures",
        "WFRS": "WaitFileReaderScanned",
        "WI": "WaitItemsIdle",
        "GEJS": "GetExportJobStatus",
        "AEJ": "AbortExportJob",
        "WBJF": "WaitBackroundJobFinished",
        "EJPM": "ExportJobProgressMonitor",
        "GII": "GetItemInfo",
        "GSI": "GetSubItems"
    }

    
    def __init__(self, ip, port):
        self.IP_ADDR = ip
        self.PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self):
        self.client_socket.connect((self.IP_ADDR, self.PORT))

    def Call(self, method, id):
        # Vytvoření slovníku s hodnotami pro volání
        call_values = {'jsonrpc': '2.0', 'method': method, 'id': id}

        # Převod slovníku na řetězec JSON
        json_string = json.dumps(call_values)

        # Převod řetězce JSON na bajty
        bytes_to_send = json_string.encode('utf-8')    

        # Odeslání bajtů přes socket
        self.client_socket.send(bytes_to_send)
        response = self.client_socket.recv(4096)  # Přečte až 4096 bajtů (můžete upravit podle potřeby)

        # Převod bajtů na řetězec
        response_string = response.decode('utf-8')   
        return response_string 


    def Generate_rec_folder_name(self, id):
        return self.Call(self.methods["GRFN"], id)

    def Compare_versions(self, id):
        return self.Call("Compare_versions", id)

    def Assert_min_version(self, id):
        return self.Call("Assert_min_version", id)

    def Copy_json(self, id):
        return self.Call("Copy_json", id)

    def Print_json(self, id):
        return self.Call("Print_json", id)

    def Is_json_object(self, id):
        return self.Call("Is_json_object", id)

    def Merge_json(self, id):
        return self.Call("Merge_json", id)

    def Is_zdat_directory(self, id):
        return self.Call("Is_zdat_directory", id)

    def GetSensors(self, id):
        return self.Call("GetSensors", id)

    def GetSystemStatus(self, id):
        return self.Call("GetSystemStatus", id)

    def GetSystemTime(self, id):
        return self.Call("GetSystemTime", id)

    def GetConfiguration(self, id):
        return self.Call("GetConfiguration", id)

    def Configure(self, id):
        return self.Call("Configure", id)

    def ClearLiveData(self, id):
        return self.Call("ClearLiveData", id)

    def StartRecording(self, id):
        return self.Call("StartRecording", id)

    def PauseRecording(self, id):
        return self.Call("PauseRecording", id)

    def StopRecording(self, id):
        return self.Call("StopRecording", id)

    def GetRecordingState(self, id):
        return self.Call("GetRecordingState", id)

    def GetAppInfo(self, id):
        return self.Call("GetAppInfo", id)

    def GetActivePulsers(self, id):
        return self.Call("GetActivePulsers", id)

    def AllPulsersOff(self, id):
        return self.Call("AllPulsersOff", id)

    def pulser_configs_same(self, id):
        return self.Call("pulser_configs_same", id)

    def SetPulser(self, id):
        return self.Call("SetPulser", id)

    def EnableContinuousRecording(self, id):
        return self.Call("EnableContinuousRecording", id)

    def OpenFileReaderByPath(self, id):
        return self.Call("OpenFileReaderByPath", id)

    def OpenFileReaderByName(self, id):
        return self.Call("OpenFileReaderByName", id)

    def SetFileReaderPath(self, id):
        return self.Call("SetFileReaderPath", id)

    def GetFileReaderInfo(self, id):
        return self.Call("GetFileReaderInfo", id)

    def GetFileReaderData(self, id):
        return self.Call("GetFileReaderData", id)

    def ExportFileReaderData(self, id):
        return self.Call("ExportFileReaderData", id)

    def ExportItems(self, id):
        return self.Call("ExportItems", id)

    def CaptureGraphPictures(self, id):
        return self.Call("CaptureGraphPictures", id)

    def WaitFileReaderScanned(self, id):
        return self.Call("WaitFileReaderScanned", id)

    def WaitItemsIdle(self, id):
        return self.Call("WaitItemsIdle", id)

    def GetExportJobStatus(self, id):
        return self.Call("GetExportJobStatus", id)

    def AbortExportJob(self, id):
        return self.Call("AbortExportJob", id)

    def WaitBackroundJobFinished(self, id):
        return self.Call("WaitBackroundJobFinished", id)

    def ExportJobProgressMonitor(self, id):
        return self.Call("ExportJobProgressMonitor", id)

    def GetItemInfo(self, id):
        return self.Call("GetItemInfo", id)

    def GetSubItems(self, id):
        return self.Call("GetSubItems", id)

    # --------------------------------------
    def start_recording(self):
        # implementace operace pro start záznamu
        return "Recording started."

    def pause_recording(self):
        # implementace operace pro pozastavení záznamu
        return "Recording paused."

    def stop_recording(self):
        # implementace operace pro zastavení záznamu
        return "Recording stopped."

    def get_file_reader(self):
        # implementace operace pro získání čtečky souborů
        return "File reader obtained."

# Příklad použití třídy
if __name__ == "__main__":
    sensor = SensorController("localhost", 40999)
    response_string = sensor.GetSystemTime(001)

    # Vypsání odpovědi
    print("Response from server:", response_string)
