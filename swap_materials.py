import bpy

class ChangeToRenderMaterial(bpy.types.Operator):
    """Change to material for rendering/baking"""
    
    bl_label = "Change to render material"
    bl_idname = "materials.change_to_render_material"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for ob in bpy.data.groups["TextureAtlas"].objects:
            ob.data.materials[0] = bpy.data.materials["plane_body_mat"]
            
        for ob in bpy.data.groups["TiresAtlas"].objects:
            ob.data.materials[0] = bpy.data.materials["tire_mat"]
        
        return {'FINISHED'}
    
class ChangeToExportMaterial(bpy.types.Operator):
    """Change to materials for export"""
    
    bl_label = "Change to export materials"
    bl_idname = "materials.change_to_export_material"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for ob in bpy.data.groups["TextureAtlas"].objects:
            ob.data.materials[0] = bpy.data.materials["plane_body_mat_export"]
            
        for ob in bpy.data.groups["TiresAtlas"].objects:
            ob.data.materials[0] = bpy.data.materials["tire_mat_export"]
            
        return {'FINISHED'}

class SwapMaterialPanel(bpy.types.Panel):
    """Panel for swapping materials for export to Altspace"""
    bl_label = "Swap Materials"
    bl_idname = "render_pt_swap_material_panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label("Change the assigned materials:")
        layout.operator(ChangeToRenderMaterial.bl_idname)
        layout.operator(ChangeToExportMaterial.bl_idname)

def register():
    bpy.utils.register_class(ChangeToRenderMaterial)
    bpy.utils.register_class(ChangeToExportMaterial)
    bpy.utils.register_class(SwapMaterialPanel)

def unregister():
    bpy.utils.register_class(ChangeToRenderMaterial)
    bpy.utils.regsiter_class(ChangeToExportMaterial)
    bpy.utils.unregister_class(SwapMaterialPanel)

if __name__ == '__main__':
    register()
