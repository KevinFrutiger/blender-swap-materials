"""Swap Materials Panel

This module creates a panel in Blender under the Render properties that allows
swapping of the first material on objects.

To use:
    (If you haven't already, create separate materials for baking and exporting)
    1. Load into Blender.
    2. Update the MATERIAL_LOOKUP variable below to have the names of the
       materials you want to swap.
    3. Run Script.
    4. A panel title 'Swap Materials' should be in the Render properties.
    5. Click the appropriate button to change to render or export materials.
    
You'll need to interact with any 3D Viewports to see the updated material on your model(s).

Warning:
    Be sure to turn on the Fake User toggle for the materials so the unassigned
    material is not disguarded whenever the file is closed. This module (as of
    yet) does not set the Fake User property nor does it check whether a
    material is left without a user (likely) when the new material replaces
    it on an object.

"""

__author__ = 'Kevin Frutiger'
__version__ = '0.2.1'

import bpy


# 'render_material_name' : 'export_material_name'
MATERIAL_LOOKUP = {
    'red_mat': 'blue_mat',
    'green_mat': 'yellow_mat',
}
"""Lookup for materials to be swapped, by name."""


def get_objects_from_material_name(material_name):
    """Return all objects in the current scene that have the material name as
    their first material.

    Keyword arguments:
    material_name -- the name of the material to get objects from
    """

    objects = []

    # Get all objects in the scene that use this material.
    for obj in bpy.context.scene.objects:
        if (hasattr(obj.data, 'materials')
                and len(obj.data.materials) > 0
                and obj.data.materials[0].name == material_name):

            objects.append(obj)

    return objects


def assign_material_to_objects(objects, new_mat_name):
    """Set the first material of the objects to the new material.

    Keyword arguments:
    objects -- a list of objects to assign the new material to
    new_mat_name -- the name of the material to assign to the objects
    """

    for obj in objects:
        obj.data.materials[0] = bpy.data.materials[new_mat_name]


class ChangeToRenderMaterial(bpy.types.Operator):
    """Change to materials for rendering/baking."""

    bl_label = 'Change to render materials'
    bl_idname = 'materials.change_to_render_material'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for render_mat_name, export_mat_name in MATERIAL_LOOKUP.items():
            objects = get_objects_from_material_name(export_mat_name)

            # If no objects, just warn user and continue.
            if len(objects) == 0:
                self.report(
                    {'WARNING'},
                    'No objects to assign {}'.format(render_mat_name)
                )
                continue
            else:
                # Give feedback.
                self.report(
                    {'INFO'},
                    'Assigning {} to {} objects'.format(
                        render_mat_name, len(objects)
                    )
                )

                # Assign the material.
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

            # If no objects, just warn and continue.
            if len(objects) == 0:
                self.report(
                    {'WARNING'},
                    'No objects to assign {}'.format(export_mat_name)
                )
                continue
            else:
                # Give feedback.
                self.report(
                    {'INFO'},
                    'Assigning {} to {} objects'.format(
                        export_mat_name, len(objects)
                    )
                )

                # Assign the material.
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

        layout.label(text='Change the assigned materials:')
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
