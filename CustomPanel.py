import bpy

class CustomPanel(bpy.types.Panel):
    bl_label = "Control Panel"
    bl_idname = "PANEL_CSTM"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Panel Exercise'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "First Label")
        
def register():
    bpy.utils.register_class(CustomPanel)
    
def unregister():
    bpy.utils.unregister_class(CustomPanel)
    
if __name__ == "__main__":
    register()