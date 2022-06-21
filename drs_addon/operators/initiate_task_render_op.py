import os
import sys
import subprocess
import bpy
from ..drs_client.drs_client import DRSClient

class DRS_OP_InitiateTaskRender(bpy.types.Operator):
    bl_idname = "drs.initiatetaskrender"
    bl_label = "initiate task render"
    bl_description = "initiates rendering of a section of the final render"

    filePath: bpy.props.StringProperty("Filepath")
    fragmentIndex: bpy.props.IntProperty("Fragment index")

    def execute(self, context):
        script_path = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'drs_addon', 'scripts', 'render_task.py')
        try:
            jobPath = os.path.join(self.filePath, "job.blend")
            subprocess.call([bpy.app.binary_path, jobPath, '--background', '--python', script_path, '--', str(self.fragmentIndex), self.filePath])
            DRSClient.fragmentRenderedEvent.set()
        except subprocess.CalledProcessError as e:
            print(e.output)
            return {'FINISHED'}
        return {'FINISHED'}