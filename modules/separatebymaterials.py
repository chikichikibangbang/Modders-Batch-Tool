import bpy

class SeparateByMaterials(bpy.types.Operator):
    bl_idname = "tool.separatebymaterials"
    bl_label = "separate by materials (need CATS)"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        obj = bpy.context.active_object
        return bool( obj.type == "MESH" )
    
    def execute(self, context):
        bpy.ops.cats_manual.separate_by_materials()
        return {'FINISHED'}


   

