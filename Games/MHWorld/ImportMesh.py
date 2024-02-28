import bpy
import pathlib
import os

main_dir = pathlib.Path(os.path.dirname(__file__)).parent.resolve()
resources_dir = os.path.join(str(main_dir), "MHWorld")
mesh_dir = os.path.join(str(resources_dir), "mesh")
f_mesh_file = os.path.join(mesh_dir, "f_mesh.mod3")
m_mesh_file = os.path.join(mesh_dir, "m_mesh.mod3")
 

class importMHWorldfmesh(bpy.types.Operator):
    bl_idname = "tool.importmhworldfmesh"
    bl_label = "female armature"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.custom_import.import_mhw_mod3(filepath=f_mesh_file)
        self.report({'INFO'}, 'Import completed')
        return {'FINISHED'}

class importMHWorldmmesh(bpy.types.Operator):
    bl_idname = "tool.importmhworldmmesh"
    bl_label = "male armature"
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        bpy.ops.custom_import.import_mhw_mod3(filepath=m_mesh_file)
        self.report({'INFO'}, 'Import completed')
        return {'FINISHED'}



