import os
import bpy

class DRS_OT_RenderSection(bpy.types.Operator):
    bl_idname = "drs.rendersection"
    bl_label = "render section of scene"
    bl_description = "renders a section of the final render"

    fragmentIndex: bpy.props.IntProperty(name = 'Fragment index', default = 0)
    savePath: bpy.props.StringProperty(name="Fragment save path")

    def execute(self, context):

        context.scene.render.use_border = True
        context.scene.render.use_crop_to_border = True

        context.scene.render.border_min_x = (self.fragmentIndex % 10) / 10
        context.scene.render.border_max_x = (self.fragmentIndex % 10) / 10 + 0.1
        context.scene.render.border_min_y = (self.fragmentIndex // 10) / 10
        context.scene.render.border_max_y = (self.fragmentIndex // 10) / 10 + 0.1



        bpy.ops.render.render()
        imagePath = os.path.join(self.savePath, f"{self.fragmentIndex}.png")
        bpy.data.images["Render Result"].save_render(imagePath)

        bpy.types.WindowManager.DRS.client.fragmentRenderedEvent.set()
        
        return {'FINISHED'}