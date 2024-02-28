import bpy
import pathlib
import os

main_dir = pathlib.Path(os.path.dirname(__file__)).parent.resolve()
resources_dir = os.path.join(str(main_dir), "MHWorld")
mesh_dir = os.path.join(str(resources_dir), "mesh")
empty_mesh_file = os.path.join(mesh_dir, "empty_mesh.fbx")

 

class AddMHWorldemptymesh(bpy.types.Operator):
    bl_idname = "tool.addmhworldemptymesh"
    bl_label = "add empty mesh"
    bl_options = {'REGISTER', 'UNDO'}
 
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "ARMATURE" ) 
   
    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        armature_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "ARMATURE"])
        for n in armature_sel_name:
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            bpy.ops.import_scene.fbx(filepath=empty_mesh_file)
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
            
            mesh_import_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])
            bpy.context.view_layer.objects.active = bpy.data.objects[mesh_import_name[0]]
            modifier = bpy.data.objects[mesh_import_name[0]].modifiers.new(name = "", type='ARMATURE')
            modifier.object = bpy.data.objects[n]
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
       
        bpy.context.view_layer.objects.active = bpy.data.objects[armature_sel_name[0]]
        for n in armature_sel_name:
            bpy.ops.object.select_pattern(pattern=n, case_sensitive=False, extend=True)
        self.report({'INFO'}, 'import completed')     
        return {'FINISHED'}





