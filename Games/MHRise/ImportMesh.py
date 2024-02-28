import bpy
import pathlib
import os

main_dir = pathlib.Path(os.path.dirname(__file__)).parent.resolve()
resources_dir = os.path.join(str(main_dir), "MHRise")
mesh_dir = os.path.join(str(resources_dir), "mesh")
f_mesh_file = os.path.join(mesh_dir, "f_shadow_mesh.fbx")
m_mesh_file = os.path.join(mesh_dir, "m_shadow_mesh.fbx")
 

class importMHRfmesh(bpy.types.Operator):
    bl_idname = "tool.importmhrfmesh"
    bl_label = "f_shadow.mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=f_mesh_file)
        self.report({'INFO'}, 'Import completed')
        return {'FINISHED'}

class importMHRmmesh(bpy.types.Operator):
    bl_idname = "tool.importmhrmmesh"
    bl_label = "m_shadow.mesh"
    bl_options = {'REGISTER', 'UNDO'}
 
    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=m_mesh_file)
        self.report({'INFO'}, 'Import completed')
        return {'FINISHED'}



