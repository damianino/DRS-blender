import logging
import os
import bpy
from PIL import Image

class DRS_OP_AssembleResult(bpy.types.Operator):
    bl_idname = "drs.assembleresult"
    bl_label = "assembleResult"

    resImageFileName : bpy.props.StringProperty(name="fragments path", description="path to all the rendered fragments", default="")
    resImageDirectory : bpy.props.StringProperty(name="fragments path", description="path to all the rendered fragments", default="")
    uuid : bpy.props.StringProperty(name="job uuid", default="")

    def execute(self, context):
        if self.resImageFileName == "" and self.resImageDirectory == "" and self.uuid == "":
            self.uuid = bpy.types.WindowManager.DRS.uuid
            print("uuid", bpy.types.WindowManager.DRS.uuid)

        if self.uuid != "":
            self.resImageDirectory = os.path.join(bpy.utils.user_resource('SCRIPTS'), 'addons', 'drs_addon', 'temp', self.uuid + "_customer")
            self.resImageFileName = os.path.join(self.resImageDirectory, self.uuid + ".png")
            print(self.resImageFileName)

        # if not os.path.exists(self.resImageDirectory):
        #     logging.error("Result image does not exist")
        #     print("Result image does not exist")
        #     return {'FINISHED'}
        
        if len(os.listdir(self.resImageDirectory)) < 102:
            logging.error("missing files to assemble")
            print("missing files to assemble")
            return {'FINISHED'}

        resImg = Image.open(self.resImageFileName)

        stepX, stepY = resImg.size
        stepX /= 10
        stepY /= 10
        stepX = int(stepX)
        stepY = int(stepY)

        for i in range(0, 100):
            x = (i % 10) * stepX
            y = (10 - i // 10) * stepY
            print(f"{i} : {(x, y)}")
            fragmentPath = os.path.join(self.resImageDirectory , str(i)+".png")
            print(fragmentPath)
            fragment = Image.open(fragmentPath)
            resImg.paste(fragment, (x, y))

        resImg.save(self.resImageFileName, "PNG")

        return {'FINISHED'}
