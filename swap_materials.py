__author__ = 'Kevin Frutiger'
__version__ = '0.1.0'

import bpy

# Lookup for render materials and export materials
# render material name : export material name
MATERIAL_LOOKUP = {
    'plane_body_mat': 'plane_body_mat_export',
    'tire_mat': 'tire_mat_export',
}


def get_objects_from_material_name(material_name):
    """Return all objects in the current scene that have the material name.
    
    Keyword arguments:
    material_name -- the name of the material to get objects from
    """
    
    objects = []
        
    for ob in bpy.context.scene.objects:
        if (hasattr(ob.data, 'materials') 
                and material_name in ob.data.materials):
            objects.append(ob)
       
    return objects


def assign_material_to_objects(objects, new_mat_name):
    """Set the first material of the objects to the new material.
    
    Keyword arguments:
    objects -- a list of objects to assign the new material to
    new_mat_name -- the name of the material to assign to the objects
    """
    
    for ob in objects:
        ob.data.materials[0] = bpy.data.materials[new_mat_name]


class ChangeToRenderMaterial(bpy.types.Operator):
    """Change to materials for rendering/baking"""
    
    bl_label = 'Change to render materials'
    bl_idname = 'materials.change_to_render_material'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        for render_mat_name, export_mat_name in MATERIAL_LOOKUP.items():
            objects = get_objects_from_material_name(export_mat_name)
            
            if len(objects) == 0:
                self.report(
                    {'WARNING'}, 
                    'No objects to assign {}'.format(render_mat_name)
                )
                continue
            else:
                self.report(
                    {'INFO'}, 
                    'Assigning {} to {} objects'.format(
                        render_mat_name, len(objects)
                    )
                )
            
                assign_material_to_objects(objects, render_mat_name)
        
        return {'FINISHED'}

    
class ChangeToExportMaterial(bpy.types.Operator):
    """Change to materials for export."""
    
    bl_label = 'Change to export materials'
    bl_idname = 'materials.change_to_export_material'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        for render_mat_name, export_mat_name in MATERIAL_LOOKUP.items():
            objects = get_objects_from_material_name(render_mat_name)
            
            if len(objects) == 0:
                self.report(
                    {'WARNING'}, 
                    'No objects to assign {}'.format(export_mat_name)
                )
                continue
            else:
                self.report(
                    {'INFO'}, 
                    'Assigning {} to {} objects'.format(
                        export_mat_name, len(objects)
                    )
                )
            
                assign_material_to_objects(objects, export_mat_name)
        
        return {'FINISHED'}


class SwapMaterialPanel(bpy.types.Panel):
    """Panel for swapping materials for baking/exporting."""
    
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
    bpy.utils.unregister_class(ChangeToRenderMaterial)
    bpy.utils.unregsiter_class(ChangeToExportMaterial)
    bpy.utils.unregister_class(SwapMaterialPanel)


if __name__ == '__main__':
    register()
