import datetime
import logging
import os
import bpy

class DRS_OP_Init(bpy.types.Operator):
    bl_idname = "drs.init"
    bl_label = "DRS_OP_Init"

    def execute(self, context):
        DRSStore = bpy.types.WindowManager.DRS
        DRSStore.path = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'drs_addon')
        DRSStore.tempPath = os.path.join(DRSStore.path, 'temp')

        curDTstr = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        logFilePath =  os.path.join(DRSStore.path, "logs", curDTstr + ".log")
        bpy.ops.drs.enablelogging(logFilePath = logFilePath)

        logging.info("Started logging")

        logging.info("Inited Path: \n{DRSStore.path}\n{DRSStore.tempPath}")
        return {'FINISHED'}
