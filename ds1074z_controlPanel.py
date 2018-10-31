import only3
import ds1074z_oscilloscope

from rawEvent import *
from event import *
import decodeEvents

import save_json
import save_text
import save_ords

from folder_exists import *

class ds1074z_controlPanel:
    def __init__(self):
        self.osc = ds1074z_oscilloscope.ds1074z_oscilloscope()
        self.overwrite_ok = False
    def launch(self):
        print("Finding oscilloscope.")
        self.osc.find_device()
        print("Connecting to oscilloscope.")
        self.osc.connect()
    def close(self):
        self.osc.disconnect()
    def saveDataset(self,ds,passData):
        if passData["fmt"]=="json_basic":
            save_json.save_basic(ds,passData)
        elif passData["fmt"]=="json_meta":
            save_json.save_meta(ds,passData)
        elif passData["fmt"]=="json_clump":
            save_json.save_clump(ds,passData)
        elif passData["fmt"]=="text_basic":
            save_text.save_basic(ds,passData)
        elif passData["fmt"]=="text_stuart1":
            save_text.save_stuart1(ds,passData)
        elif passData["fmt"]=="text_stuart2":
            save_text.save_stuart2(ds,passData)
        elif passData["fmt"]=="text_stuart3":
            save_text.save_stuart3(ds,passData)
        elif passData["fmt"]=="ords":
            save_ords.save_ords(ds,passData)
        else:
            raise Exception("The save format ("+str(passData["fmt"])+") is not recognized.")
    def singleCollection(self,passData):
        print("Getting events.")
        if "options" in passData:
            raw = self.osc.getRawDataset(passData["channels"],100,passData["delay"],passData["options"])
        else:
            raw = self.osc.getRawDataset(passData["channels"],100,passData["delay"],dict())
        print("Filtering events.")
        filtered = raw.removeBadEvents()
        del(raw)
        print("Decoding events.")
        clean = decodeEvents.decodeEvents(filtered)
        del(filtered)
        print("Getting metadata.")
        meta = self.osc.getInfo()
        for x in meta:
            clean.meta[x] = meta[x]
        print("Saving events.")
        self.saveDataset(clean,passData)
    def collector(self,channels,count,delay,path,fmt,**options):
        self.launch()
        print("Setting up.")
        self.osc.readSetup()
        passData = dict()
        passData["overwrite_ok"] = self.overwrite_ok
        passData["channels"] = channels
        passData["count"] = count
        passData["delay"] = delay
        passData["path"] = path
        if folder_exists(path) == False:
            raise Exception("Output path does not exist or does not end in a slash character.")
        passData["fmt"] = fmt
        passData["eventCount"] = 0
        passData["fileCount"] = 0
        passData["options"] = options
        print("Starting data collection.")
        while passData["eventCount"]<passData["count"]:
            self.singleCollection(passData)
            print("Event Count: "+str(passData["eventCount"]))
            print("File Count: "+str(passData["fileCount"]))
        print("Data collection complete.")
        self.close()
        print("Connection closed.")
