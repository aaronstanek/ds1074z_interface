from ds1074z_controlPanel import ds1074z_controlPanel as cpc

def main():
    channels = [1,2]
    eventCount = 5000
    secondsBetweenEvents = 0.3
    savePath = "/home/aaron/Desktop/data/"
    # savePath needs to end with / or \
    cp = cpc()
    cp.collector(channels,eventCount,secondsBetweenEvents,savePath,"json_clump")

main()
