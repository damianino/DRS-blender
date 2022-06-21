import logging
import os
import bpy
from PIL import Image

class DRS_OP_AssembleResult(bpy.types.Operator):
    bl_idname = "drs.assembleResult"
    bl_label = "assembleResult"

    resImageFileName : bpy.props.StringProperty(name="fragments path", description="path to all the rendered fragments")
    resImageDirectory : bpy.props.StringProperty(name="fragments path", description="path to all the rendered fragments")

    def execute(self, context):
    
        if not os.path.exists(self.resImgPath):
            logging.error("Result image does not exist")
            return
        
        if len(os.listdir(dir)) < 102:
            logging.error("missing files to assemble")
            return

        resImg = Image.open(self.resImgPath)

        stepX, stepY = resImg.size
        stepX /= 10
        stepY /= 10
        stepX = int(stepX)
        stepY = int(stepY)

        for i in range(0, 100):
            x = (i % 10) * stepX
            y = (10 - i // 10) * stepY
            print(f"{i} : {(x, y)}")
            fragmentPath = os.path.join(dir, str(i)+".png")
            fragment = Image.open(fragmentPath)
            resImg.paste(fragment, (x, y))

        resImg.save(self.resImgPath, "PNG")

        return {'FINISHED'}
