import bpy


def main(context):
    name_list = [
    ['Waist','bonefunction_001'],
    ['Spine','bonefunction_002'],
    ['Neck','bonefunction_003'],
    ['Head','bonefunction_004'],
    ['Shoulder_L','bonefunction_005'],
    ['Arm_L','bonefunction_006'],
    ['Elbow_L','bonefunction_007'],
    ['Wrist_L','bonefunction_008'],
    ['Shoulder_R','bonefunction_009'],
    ['Arm_R','bonefunction_010'],
    ['Elbow_R','bonefunction_011'],
    ['Wrist_R','bonefunction_012'],
    ['Hip','bonefunction_013'],
    ['Thigh_L','bonefunction_014'],
    ['Knee_L','bonefunction_015'],
    ['Ankle_offset_L','bonefunction_016'],
    ['Toe_offset_L','bonefunction_017'],
    ['Thigh_R','bonefunction_018'],
    ['Knee_R','bonefunction_019'],
    ['Ankle_offset_R','bonefunction_020'],
    ['Toe_offset_R','bonefunction_021'],
    ['Thumb_01_L','bonefunction_031'],
    ['Thumb_02_L','bonefunction_032'],
    ['Thumb_03_L','bonefunction_033'],
    ['Index_01_L','bonefunction_034'],
    ['Index_02_L','bonefunction_035'],
    ['Index_03_L','bonefunction_036'],
    ['Middle_01_L','bonefunction_037'],
    ['Middle_02_L','bonefunction_038'],
    ['Middle_03_L','bonefunction_039'],
    ['Sp_Ch_Bust0_L_01','L_Oupai_00'],
    ['Ring_01_L','bonefunction_041'],
    ['Ring_02_L','bonefunction_042'],
    ['Ring_03_L','bonefunction_043'],
    ['Pinky_01_L','bonefunction_044'],
    ['Pinky_02_L','bonefunction_045'],
    ['Pinky_03_L','bonefunction_046'],
    ['Thumb_01_R','bonefunction_048'],
    ['Thumb_02_R','bonefunction_049'],
    ['Thumb_03_R','bonefunction_050'],
    ['Index_01_R','bonefunction_051'],
    ['Index_02_R','bonefunction_052'],
    ['Index_03_R','bonefunction_053'],
    ['Middle_01_R','bonefunction_054'],
    ['Middle_02_R','bonefunction_055'],
    ['Middle_03_R','bonefunction_056'],
    ['Sp_Ch_Bust0_R_01','R_Oupai_00'],
    ['Ring_01_R','bonefunction_058'],
    ['Ring_02_R','bonefunction_059'],
    ['Ring_03_R','bonefunction_060'],
    ['Pinky_01_R','bonefunction_061'],
    ['Pinky_02_R','bonefunction_062'],
    ['Pinky_03_R','bonefunction_063'],
    ['null1','L_Arm_00_W'],
    ['null2','L_Arm_01_W'],
    ['null3','R_Arm_00_W'],
    ['null4','R_Arm_01_W'],
    ['null5','L_Leg_00_W'],
    ['null6','L_Leg_01_W'],
    ['null7','R_Leg_00_W'],
    ['null8','R_Leg_01_W'],
    ['ShoulderRoll_L','bonefunction_080'],
    ['ArmRoll_L','bonefunction_081'],
    ['ShoulderRoll_R','bonefunction_082'],
    ['ArmRoll_R','bonefunction_083'],
    ]
    
    for obj in bpy.context.selected_objects:
        v_groups = obj.vertex_groups
        for n in name_list:
            if n[0] in v_groups:
                v_groups[n[0]].name = n[1]
        
       

class UMAtoMHWRename(bpy.types.Operator):
    bl_idname = "tool.umatomhwrename"
    bl_label = "UMA to MHWorld"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )

    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    

