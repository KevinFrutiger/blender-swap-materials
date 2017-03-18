import bpy


def get_objects_from_material_name(material_name):
        
    objects = []
        
    for ob in bpy.context.scene.objects:
        if (hasattr(ob.data, 'materials') 
                and material_name in ob.data.materials):
            objects.append(ob)
       
    return objects


class ChangeToRenderMaterial(bpy.types.Operator):
    """Change to material for rendering/baking"""
    
    bl_label = 'Change to render materials'
    bl_idname = 'materials.change_to_render_material'
    bl_options = {'REGISTER', 'UNDO'}
    
    suffix = '_export'
    
    def execute(self, context):
        
        objects_to_change = {
            'plane_body_mat' + self.suffix: 
            get_objects_from_material_name('plane_body_mat' + self.suffix),
            'tire_mat' + self.suffix: 
            get_objects_from_material_name('tire_mat' + self.suffix)
        }
        
        for material_name in objects_to_change:
            for ob in objects_to_change[material_name]:
                new_material_name = material_name[:-len(self.suffix)]
                ob.data.materials[0] = bpy.data.materials[new_material_name]
        
        return {'FINISHED'}

    
class ChangeToExportMaterial(bpy.types.Operator):
    """Change to materials for export"""
    
    bl_label = 'Change to export materials'
    bl_idname = 'materials.change_to_export_material'
    bl_options = {'REGISTER', 'UNDO'}
    
    suffix = '_export'
    
    def execute(self, context):
        
        objects_to_change = {
            'plane_body_mat': get_objects_from_material_name('plane_body_mat'),
            'tire_mat': get_objects_from_material_name('tire_mat')
        }
        
        for material_name in objects_to_change:
            for ob in objects_to_change[material_name]:
                new_material_name = material_name + self.suffix
                ob.data.materials[0] = bpy.data.materials[new_material_name]
        
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
