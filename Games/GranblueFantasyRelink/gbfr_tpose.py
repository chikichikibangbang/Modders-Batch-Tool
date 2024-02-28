import bpy
import math
import re
import copy
from mathutils import Vector, Euler, Matrix


def main(context):
    bone_list = [
    ["_900"],
    ["_910"],
    ["_920"],
    ["_960"],
    ["_000"], 
    ["_001"], 
    ["_002"], 
    ["_003"], 
    ["_004"], 
    ["_005"], 
    ["_00a"], 
    ["_00b"], 
    ["_00c"], 
    ["_00d"], 
    ["_231"], 
    ["_232"], 
    ["_233"], 
    ["_241"], 
    ["_242"], 
    ["_243"], 
    ["_200"], 
    ["_201"], 
    ["_202"], 
    ["_211"], 
    ["_212"], 
    ["_213"], 
    ["_221"], 
    ["_222"], 
    ["_223"], 
    #["_401"], 
    #["_403"], 
    ["_a0d"], 
    ["_a21"], 
    ["_a0c"], 
    ["_a38"], 
    ["_a37"], 
    ["_a30"], 
    ["_a0b"], 
    ["_006"], 
    ["_007"], 
    ["_008"], 
    ["_009"], 
    ["_131"], 
    ["_132"], 
    ["_133"], 
    ["_141"], 
    ["_142"], 
    ["_143"], 
    ["_100"], 
    ["_101"], 
    ["_102"], 
    ["_111"], 
    ["_112"], 
    ["_113"], 
    ["_121"], 
    ["_122"], 
    ["_123"], 
    #["_400"], 
    #["_402"], 
    ["_a09"], 
    ["_a31"], 
    ["_a08"], 
    ["_a28"], 
    ["_a27"], 
    ["_a20"], 
    ["_a07"], 
    ["_a04"], 
    ["_a0a"], 
    ["_a06"], 
    #["_a15"], 
    #["_a16"], 
    #["_a17"], 
    #["_a18"], 
    #["_a19"], 
    #["_a1a"], 
    ["_012"], 
    ["_013"], 
    ["_014"], 
    ["_015"], 
    ["_a14"], 
    ["_a33"], 
    ["_a13"], 
    ["_a39"], 
    ["_a3a"], 
    ["_a32"], 
    ["_00e"], 
    ["_00f"], 
    ["_010"], 
    ["_011"], 
    ["_a10"], 
    ["_a23"], 
    ["_a0f"], 
    ["_a29"], 
    ["_a2a"], 
    ["_a22"], 
    ["_a12"], 
    ["_a34"], 
    ["_a35"], 
    ["_a36"], 
    ["_a0e"], 
    ["_a24"], 
    ["_a25"], 
    ["_a26"]
    ]
    
    ArmatureName = bpy.context.active_object.data.name
    obj = bpy.context.active_object

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones["_000"]    
    bpy.ops.armature.select_all(action='DESELECT')

    bpy.ops.object.mode_set(mode='POSE')
    for n in bone_list:
        bpy.ops.object.select_pattern(pattern=n[0], case_sensitive=False, extend=True)


    backup = [Matrix()]*len(bpy.context.selected_pose_bones)
    
    for i in range(len(backup)):
        backup[i] = copy.deepcopy(bpy.context.selected_pose_bones[i].matrix)
        zero = copy.deepcopy(bpy.context.selected_pose_bones[i].matrix)
        
        zero[0][0] = 1.0
        zero[0][1] = 0.0
        zero[0][2] = 0.0
        zero[1][0] = 0.0
        zero[1][1] = 1.0
        zero[1][2] = 0.0
        zero[2][0] = 0.0
        zero[2][1] = 0.0
        zero[2][2] = 1.0
        zero[3][0] = 0.0
        zero[3][1] = 0.0
        zero[3][2] = 0.0
        zero[3][3] = 1.0
    
    
        bpy.context.selected_pose_bones[i].matrix = zero
        bpy.context.view_layer.update()  
    
    bpy.ops.object.mode_set(mode='OBJECT')  
    bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE', extend=True)
    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.armature_apply(selected=True)
    bpy.ops.object.mode_set(mode='OBJECT')  

    bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
    modifier = bpy.context.active_object.modifiers.new(name = "", type='ARMATURE')
    modifier.object = obj
    bpy.ops.object.make_links_data(type='MODIFIERS')
    bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)

    if bpy.context.object.rotation_euler[0] == 0:
         bpy.context.object.rotation_euler[0] = 1.5708
         bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE', extend=True)
         bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            

class GBFRTPOSE(bpy.types.Operator):
    bl_idname = "tool.gbfrtpose"
    bl_label = "convert to tpose"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "ARMATURE" )

    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    


