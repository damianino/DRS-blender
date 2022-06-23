from datetime import datetime
import time
from threading import Event
from PIL import Image
import bpy
from .grpc_client import *
from .p2p_node import *
from .utils import RenderProgressBar
import logging

class DRSClient():

    uuid = ""
    path = ""
    tempPath = ""
    fragmentRenderedEvent = Event()
    stopRoutineEvent = Event()

    @classmethod
    def Init(cls):
        cls.path = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'drs_addon')
        cls.tempPath = os.path.join(cls.path, 'temp')

        curDTstr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        logFilePath =  os.path.join(cls.path, "logs", curDTstr + ".log")
        bpy.ops.drs.enablelogging(logFilePath = logFilePath)

        logging.info("Started logging")

        logging.info("Inited Path: \n{cls.path}\n{cls.tempPath}")


    @classmethod
    def Connect(cls, addr = "localhost:4000", id = 1):
        GRPCClient.Connect(addr, id)
        pass
    
    @classmethod
    def SetRole(cls, role):
        pass

    @classmethod
    def RenderRoutine(cls, ip = "localhost"):
        response = GRPCClient.Render()

        if not response.Success:
            logging.info(f"response.Success was false Body : {response.Body}")
            return

        cls.uuid = response.Body
        bpy.types.WindowManager.DRS.uuid = response.Body
        workingDirPath = os.path.join(cls.tempPath, cls.uuid+"_customer")
        jobFilePath = os.path.join(workingDirPath, "job.blend")
        if not os.path.exists(workingDirPath):
                        os.mkdir(workingDirPath)
        bpy.ops.wm.save_as_mainfile(filepath=jobFilePath)

        resolution = (bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y)
        resImg = Image.new("RGBA", resolution, 1)
        resPath = os.path.join(workingDirPath, cls.uuid + ".png")
        resImg.save(resPath, "PNG")

        jobResult = Customer.CustomerRoutine(workingDir = workingDirPath, stopEvent = cls.stopRoutineEvent)
        if  jobResult == 'SUCCESS':
            bpy.ops.drs.assembleResult(resImgFileName=resPath)
            bpy.ops.drs.openImageWindow(fileName=cls.uuid + ".png")

    
    @classmethod
    def WorkerRoutine(cls):
        while True:
            if cls.stopRoutineEvent.is_set():
                logging.info("User stopped the routine")
                break

            if cls.uuid == "": 
                response = GRPCClient.JobPoll("")
                print("Polling for job")
                logging.info(f"Performing jobpoll request for JOB")

                if response.Success:
                    cls.uuid = response.Body.split("|")[1] 
                    Worker.customerIp = response.Body.split("|")[0].split(":")[0] 
                    print(f"Starting work on job {cls.uuid}")
                    workingDirPath = os.path.join(cls.tempPath, cls.uuid)
                    jobFilePath = os.path.join(workingDirPath, "job.blend")
                    if not os.path.exists(workingDirPath):
                        os.mkdir(workingDirPath)
                    Worker.Connect()
                    Worker.ReciveFile(fp = jobFilePath)

                time.sleep(5)

            else:
                print("Polling for task")
                logging.info(f"Performing jobpoll request for TASK")

                response = GRPCClient.JobPoll(cls.uuid)
                fragmentToRender = response.FragmentIndexes
                if fragmentToRender  < 0 :
                    Worker.SendFragmentIndex(-1)
                    logging.info("disconnecting")
                    Worker.Disconnect()
                    cls.uuid = ""
                    continue

                if response.Success:
                    cls.fragmentRenderedEvent.clear()
                    bpy.ops.drs.initiatetaskrender(filePath = workingDirPath, fragmentIndex = fragmentToRender)
                    cls.fragmentRenderedEvent.wait()
                    fragmentPath = os.path.join(workingDirPath, str(fragmentToRender) + ".png")
                    #Worker.SendFragmentIndex(fragmentToRender)
                    
                    #Worker.sock.send(f"{fragmentToRender}".encode("iso-8859-1"))
                    Worker.SendFile(fragmentPath)
                    GRPCClient.ReportProgress(str(fragmentToRender))
                    print(f"Rendered fragment {fragmentToRender}" )

        cls.stopRoutineEvent.clear()

    @classmethod
    def Disconnect(cls, ):
        pass

    @classmethod
    def StopRoutine(cls):
        cls.stopRoutineEvent.set()
    
    @classmethod
    def GetfragmentRenderedEvent(cls):
        return cls.fragmentRenderedEvent
