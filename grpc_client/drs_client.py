import time
from threading import Event
import bpy
from grpc_client import *
from p2p_node import *

class DRSClient():

    uuid = ""
    path = ""
    tempPath = ""
    fragmentRenderedEvent : Event

    @classmethod
    def InitPath(cls):
        cls.path = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'drs_addon')
        cls.tempPath = os.path.join(cls.path, 'temp')

    @classmethod
    def Connect(cls, ip = "localhost", port = "4000"):
        GRPCClient.Connect(f"{ip}:{port}")
        pass
    
    @classmethod
    def SetRole(cls, role):
        pass

    @classmethod
    def Render(cls, fp):
        pass
    
    @classmethod
    def WorkerRoutine(cls):
        workingDirPath = cls.tempPath
        while True:
            while cls.uuid == "": 
                response = GRPCClient.JobPoll("")
                time.sleep(5000)
                if response.Success:
                    cls.uuid = response.Body 
                    workingDirPath = os.path.join(workingDirPath, cls.uuid)
                    jobFilePath = os.path.join(workingDirPath, "job.blend")
                    os.mkdir(workingDirPath)
                    node = Worker()
                    node.Connect( addr = "localhost:4001" )
                    node.ReciveFile( fp = jobFilePath )
                    break
            
            response = GRPCClient.JobPoll(cls.uuid)
            if response.Success:
                cls.fragmentRenderedEvent.clear()
                bpy.ops.drs.initiatetaskrender(filepath = jobFilePath, fragmentIndex = response.FragmentIndex[0])
                cls.fragmentRenderedEvent.wait()

        pass

    @classmethod
    def Disconnect(cls, ):
        pass


    
    


    