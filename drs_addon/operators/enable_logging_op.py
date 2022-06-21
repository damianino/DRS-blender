import logging
import datetime
import bpy

class DRS_OP_EnableLoggingOperator(bpy.types.Operator):
    bl_idname = "drs.enablelogging"
    bl_label = "Enable Logging"

    logFilePath : bpy.props.StringProperty(name="logName", description="sets the log file name")

    def execute(self, context):

        logging.basicConfig(filename=self.logFilePath, encoding='utf-8', level=logging.DEBUG)

        return {'FINISHED'}
