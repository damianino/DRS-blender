import bpy

#
#   Описание интерфейса аддона
#

class DRS_PT_Panel(bpy.types.Panel):
    #   Выбор области отображения аддона
    bl_space_type = "VIEW_3D"
    #
    bl_region_type = "UI"
    #   Надпись в заголовке отображения аддона
    bl_label = "Distributed Rendering System"
    #   Категория в которой отображается аддон
    bl_category = "DRS"

    def draw(self, context):
        preferences = bpy.types.WindowManager.drsPrefs

        layout = self.layout
        wm = context.window_manager 

        row = layout.row()
        row.prop(wm, "customAddr") 
        row = layout.row()
        row.enabled = True if preferences.customAddr else False
        row.prop(wm, "addr") 
        row = layout.row()

        row = layout.row()
        row.label(text=" Client mode:")
        row = layout.row()
        row.operator("drs.render_section")
        row.enabled = 1 if preferences.role == 0 else 0
        
        row = layout.row()
        row.label(text=" Executor mode:")  
        col = row.column()
        props = col.operator("drs.update_machine_status",
            text = "I'm not available")
        props.status = 0
        col.enabled = 0 if preferences.role == 0 else 1

        col = row.column()
        props = col.operator("drs.update_machine_status",
            text = "I'm available")
        props.status = 1
        col.enabled = 1 if preferences.role == 0 else 0
