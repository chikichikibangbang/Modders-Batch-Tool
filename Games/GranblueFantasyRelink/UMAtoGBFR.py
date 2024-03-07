import bpy


def main(context):
    name_list = [
    ['Hip','_000'],
    ['Waist','_001'],
    ['Spine','_002'],
    ['Chest','_003'],
    ['Neck','_004'],
    ['Head','_005'],

    ['Sp_Ch_Bust0_L_01','_c42'],
    ['Sp_Ch_Bust0_R_01','_c40'],

    ['Shoulder_L','_a0a'],
    ['Arm_L','_00b'],
    ['Elbow_L','_00c'],
    ['Wrist_L','_00d'],
    ['Shoulder_R','_a06'],
    ['Arm_R','_007'],
    ['Elbow_R','_008'],
    ['Wrist_R','_009'],
    
    ['Thigh_L','_a12'],
    ['Knee_L','_013'],
    ['Ankle_offset_L','_014'],
    ['Toe_offset_L','_015'],
    ['Thigh_R','_a0e'],
    ['Knee_R','_00f'],
    ['Ankle_offset_R','_010'],
    ['Toe_offset_R','_011'],

    ['Thumb_01_L','_200'],
    ['Thumb_02_L','_201'],
    ['Thumb_03_L','_202'],
    ['Index_01_L','_211'],
    ['Index_02_L','_212'],
    ['Index_03_L','_213'],
    ['Middle_01_L','_221'],
    ['Middle_02_L','_222'],
    ['Middle_03_L','_223'],
    ['Ring_01_L','_231'],
    ['Ring_02_L','_232'],
    ['Ring_03_L','_233'],
    ['Pinky_01_L','_241'],
    ['Pinky_02_L','_242'],
    ['Pinky_03_L','_243'],

    ['Thumb_01_R','_100'],
    ['Thumb_02_R','_101'],
    ['Thumb_03_R','_102'],
    ['Index_01_R','_111'],
    ['Index_02_R','_112'],
    ['Index_03_R','_113'],
    ['Middle_01_R','_121'],
    ['Middle_02_R','_122'],
    ['Middle_03_R','_123'],
    ['Ring_01_R','_131'],
    ['Ring_02_R','_132'],
    ['Ring_03_R','_133'],
    ['Pinky_01_R','_141'],
    ['Pinky_02_R','_142'],
    ['Pinky_03_R','_143'],

    ['ShoulderRoll_L','_a0b'],
    ['ArmRoll_L','_a21'],
    ['ShoulderRoll_R','_a07'],
    ['ArmRoll_R','_a31'],
    ]
    
    for obj in bpy.context.selected_objects:
        v_groups = obj.vertex_groups
        for n in name_list:
            if n[0] in v_groups:
                v_groups[n[0]].name = n[1]
        
       

class UMAtoGBFRRename(bpy.types.Operator):
    bl_idname = "tool.umatogbfrrename"
    bl_label = "UMA to GBFR"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )
            
    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    

