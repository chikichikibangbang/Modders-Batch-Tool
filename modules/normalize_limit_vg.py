import bpy

class NormalizeLimitVG(bpy.types.Operator):
    bl_idname = "tool.normalizelimitvg"
    bl_label = "convert 8wt to 4wt"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )
    
    def execute(self, context):
        meshes_sel_name = sorted([o.name for o in bpy.context.selected_objects if o.type == "MESH"])
        #print(meshes_sel_name)
    
        bpy.ops.tool.cleanzerovg()
        for n in meshes_sel_name:
            bpy.context.view_layer.objects.active = bpy.data.objects[n]
            bpy.ops.object.mode_set(mode='WEIGHT_PAINT')    
            bpy.ops.object.vertex_group_normalize_all(lock_active=False)
            bpy.ops.object.vertex_group_clean(group_select_mode='ALL', limit=0.001)  
            bpy.ops.object.vertex_group_limit_total(limit=4)
            bpy.ops.object.mode_set(mode='OBJECT')
            
        bpy.context.view_layer.objects.active = bpy.data.objects[meshes_sel_name[0]]
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}


   

