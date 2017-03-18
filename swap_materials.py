import bpy

# render material name : export material name
material_lookup = {
    'plane_body_mat': 'plane_body_mat_export',
    'tire_mat': 'tire_mat_export',
}


def get_objects_from_material_name(material_name):
        
    objects = []
        
    for ob in bpy.context.scene.objects:
        if (hasattr(ob.data, 'materials') 
                and material_name in ob.data.materials):
            objects.append(ob)
       
    return objects


def set_material_for_objects(objects, new_mat_name):
    for ob in objects:
        ob.data.materials[0] = bpy.data.materials[new_mat_name]


class ChangeToRenderMaterial(bpy.types.Operator):
    """Change to materials for rendering/baking"""
    
    bl_label = 'Change to render materials'
    bl_idname = 'materials.change_to_render_material'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        for render_mat_name, export_mat_name in material_lookup.items():
            set_material_for_objects(
                get_objects_from_material_name(export_mat_name),
                render_mat_name
            )
        
        return {'FINISHED'}

    
class ChangeToExportMaterial(bpy.types.Operator):
    """Change to materials for export"""
    
    bl_label = 'Change to export materials'
    bl_idname = 'materials.change_to_export_material'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        for render_mat_name, export_mat_name in material_lookup.items():
            set_material_for_objects(
                get_objects_from_material_name(render_mat_name),
                export_mat_name
            )
        
        return {'FINISHED'}


class SwapMaterialPanel(bpy.types.Panel):
    """Panel for swapping materials for export to Altspace"""
    
    bl_label = 'Swap Materials'
    bl_idname = 'render_pt_swap_material_panel'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'render'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label('Change the assigned materials:')
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
