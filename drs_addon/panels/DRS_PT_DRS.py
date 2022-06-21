import bpy

class DRS_PT_Panel(bpy.types.Panel):
    bl_idname = "OUTPUT_PT_DRS"
    bl_label = "DRS"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="Distributed Rendering System")

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Server")
        box.prop("id").id = 1
        box.operator("drs.connect").ip = ""
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")

if __name__ == "__main__":
    bpy.utils.register_class(DRS_PT_Panel)