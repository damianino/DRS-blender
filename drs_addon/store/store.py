from ..drs_client.drs_client import *

class DRS():
    client = DRSClient
    id = 1
    addr = "localhost:4000"
    role = None
    apiToken = ""
    uuid = ""
    path = ""
    tempPath = ""
    fragmentRenderedEvent = Event()
    stopRoutineEvent = Event()
    
        
