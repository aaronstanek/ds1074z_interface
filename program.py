from ds1074z_controlPanel import ds1074z_controlPanel as cpc

def main():
    channels = [1,2] # which channels to collect
    eventCount = 5000 # how many events to collect
    secondsBetweenEvents = 0.3 # how much time should go between events *
    savePath = "/home/aaron/Desktop/data/" # where to save the data
    # savePath should indicate an exiting folder
    # savePath needs to end with / or \
    cp = cpc()
    cp.collector(channels,eventCount,secondsBetweenEvents,savePath,"json_clump")

main()

# *
# making this value too large will cause data collection to take forever
# making this value too small will cause the oscilloscope to spend all its time
# communicating with the computer, and never actually collect any events
# this value is probably best between 0.3 and 2.0
