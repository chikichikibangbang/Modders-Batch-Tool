import bpy


def main(context):
    name_list = [
    ['Waist','Spine_00'],
    ['Spine','Spine_01'],
    ['Neck','Neck_00'],
    ['Head','Head_00'],
    ['Shoulder_L','L_Arm_00'],
    ['Arm_L','L_Arm_01'],
    ['Elbow_L','L_Arm_02'],
    ['Wrist_L','L_Arm_03'],
    ['Shoulder_R','R_Arm_00'],
    ['Arm_R','R_Arm_01'],
    ['Elbow_R','R_Arm_02'],
    ['Wrist_R','R_Arm_03'],
    ['Hip','Waist_00'],
    ['Thigh_L','L_Leg_00'],
    ['Knee_L','L_Leg_01'],
    ['Ankle_offset_L','L_Leg_02'],
    ['Toe_offset_L','L_Leg_03'],
    ['Thigh_R','R_Leg_00'],
    ['Knee_R','R_Leg_01'],
    ['Ankle_offset_R','R_Leg_02'],
    ['Toe_offset_R','R_Leg_03'],
    ['Thumb_01_L','L_Finger_00'],
    ['Thumb_02_L','L_Finger_01'],
    ['Thumb_03_L','L_Finger_02'],
    ['Index_01_L','L_Finger_03'],
    ['Index_02_L','L_Finger_04'],
    ['Index_03_L','L_Finger_05'],
    ['Middle_01_L','L_Finger_06'],
    ['Middle_02_L','L_Finger_07'],
    ['Middle_03_L','L_Finger_08'],
    ['Sp_Ch_Bust0_L_01','L_Oupai_00'],
    ['Ring_01_L','L_Finger_10'],
    ['Ring_02_L','L_Finger_11'],
    ['Ring_03_L','L_Finger_12'],
    ['Pinky_01_L','L_Finger_13'],
    ['Pinky_02_L','L_Finger_14'],
    ['Pinky_03_L','L_Finger_15'],
    ['Thumb_01_R','R_Finger_00'],
    ['Thumb_02_R','R_Finger_01'],
    ['Thumb_03_R','R_Finger_02'],
    ['Index_01_R','R_Finger_03'],
    ['Index_02_R','R_Finger_04'],
    ['Index_03_R','R_Finger_05'],
    ['Middle_01_R','R_Finger_06'],
    ['Middle_02_R','R_Finger_07'],
    ['Middle_03_R','R_Finger_08'],
    ['Sp_Ch_Bust0_R_01','R_Oupai_00'],
    ['Ring_01_R','R_Finger_09'],
    ['Ring_02_R','R_Finger_10'],
    ['Ring_03_R','R_Finger_11'],
    ['Pinky_01_R','R_Finger_12'],
    ['Pinky_02_R','R_Finger_13'],
    ['Pinky_03_R','R_Finger_14'],
    ['BoneFunction070','L_Arm_00_W'],
    ['BoneFunction071','L_Arm_01_W'],
    ['BoneFunction072','R_Arm_00_W'],
    ['BoneFunction073','R_Arm_01_W'],
    ['BoneFunction074','L_Leg_00_W'],
    ['BoneFunction075','L_Leg_01_W'],
    ['BoneFunction076','R_Leg_00_W'],
    ['BoneFunction077','R_Leg_01_W'],
    ['ShoulderRoll_L','L_Arm_01_T'],
    ['ArmRoll_L','L_Arm_02_T'],
    ['ShoulderRoll_R','R_Arm_01_T'],
    ['ArmRoll_R','R_Arm_02_T'],
    ]
    
    for obj in bpy.context.selected_objects:
        v_groups = obj.vertex_groups
        for n in name_list:
            if n[0] in v_groups:
                v_groups[n[0]].name = n[1]
        
       

class UMAtoMHRRename(bpy.types.Operator):
    bl_idname = "tool.umatomhrrename"
    bl_label = "UMA to MHRise"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )
            
    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    

