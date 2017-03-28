# Swap Materials module

A module that creates a panel used to swap materials, primarily for use swapping between materials for texture baking and export.

## Installation

1. Download the .zip file or clone the repostory.
2. Place swap_materials.py wherever you'd like. It's intended to be run as a script, not as a add-on.

## Usage

1. Create separate materials for baking and export as needed.
  * Be sure to toggle the Fake User button for the material. This module doesn't set it and the "other" material likely will have no users and be disgarded when you save the Blender file.
2. Load swap_materials.py in Blender (see [Text Editor] (https://docs.blender.org/manual/en/dev/editors/text_editor.html))
3. Modify the MATERIAL_LOOKUP variable with the names of all the render/export materials
```
MATERIAL_LOOKUP = {
  'your_render_mat': 'your_export_mat',
  'another_render_mat': 'another_export_mat'
}
```
4. Run Script
  * You'll need to do this every time you open the Blender file unless you check on the *Register* option located at the bottom of the Text Editor
5. You should see a **Swap Material** panel at the bottom of the Render properties
6. Use the buttons to swap between materials

