import bpy

class DRS_OP_OpenImageWindow(bpy.types.Operator):
    bl_idname = "drs.openImageWindow"
    bl_label = "open_image_window"

    fileName : bpy.props.StringProperty(name="filename")

    def execute(self, context):
        area = bpy.context.window_manager.windows[-1].screen.areas[0]
        area.type = 'IMAGE_EDITOR'
        area.spaces.active.image = bpy.data.images[self.fileName]
        return {'FINISHED'}
