import bpy


def main(context):
    name_list = [
    ['bonefunction_013','Waist_00'],
    ['bonefunction_001','Spine_00'],
    ['bonefunction_002','Spine_01'],
    ['bonefunction_003','Neck_00'],
    ['bonefunction_004','Head_00'],
    ['bonefunction_254','Neck_00_S'],

    ['bonefunction_005','L_Arm_00'],
    ['bonefunction_006','L_Arm_01'],
    ['bonefunction_007','L_Arm_02'],
    ['bonefunction_008','L_Arm_03'],
    ['bonefunction_009','R_Arm_00'],
    ['bonefunction_010','R_Arm_01'],
    ['bonefunction_011','R_Arm_02'],
    ['bonefunction_012','R_Arm_03'],

    ['bonefunction_014','L_Leg_00'],
    ['bonefunction_015','L_Leg_01'],
    ['bonefunction_016','L_Leg_02'],
    ['bonefunction_017','L_Leg_03'],
    ['bonefunction_018','R_Leg_00'],
    ['bonefunction_019','R_Leg_01'],
    ['bonefunction_020','R_Leg_02'],
    ['bonefunction_021','R_Leg_03'],

    ['bonefunction_031','L_Finger_00'],
    ['bonefunction_032','L_Finger_01'],
    ['bonefunction_033','L_Finger_02'],
    ['bonefunction_034','L_Finger_03'],
    ['bonefunction_035','L_Finger_04'],
    ['bonefunction_036','L_Finger_05'],
    ['bonefunction_037','L_Finger_06'],
    ['bonefunction_038','L_Finger_07'],
    ['bonefunction_039','L_Finger_08'],
    ['bonefunction_040','L_Finger_09'],
    ['bonefunction_041','L_Finger_10'],
    ['bonefunction_042','L_Finger_11'],
    ['bonefunction_043','L_Finger_12'],
    ['bonefunction_044','L_Finger_13'],
    ['bonefunction_045','L_Finger_14'],
    ['bonefunction_046','L_Finger_15'],

    ['bonefunction_048','R_Finger_00'],
    ['bonefunction_049','R_Finger_01'],
    ['bonefunction_050','R_Finger_02'],
    ['bonefunction_051','R_Finger_03'],
    ['bonefunction_052','R_Finger_04'],
    ['bonefunction_053','R_Finger_05'],
    ['bonefunction_054','R_Finger_06'],
    ['bonefunction_055','R_Finger_07'],
    ['bonefunction_056','R_Finger_08'],
    ['bonefunction_057','R_Grip_00'],
    ['bonefunction_058','R_Finger_09'],
    ['bonefunction_059','R_Finger_10'],
    ['bonefunction_060','R_Finger_11'],
    ['bonefunction_061','R_Finger_12'],
    ['bonefunction_062','R_Finger_13'],
    ['bonefunction_063','R_Finger_14'],

    ['bonefunction_070','L_Arm_00_W'],
    ['bonefunction_071','L_Arm_01_W'],
    ['bonefunction_072','R_Arm_00_W'],
    ['bonefunction_073','R_Arm_01_W'],

    ['bonefunction_074','L_Leg_00_W'],
    ['bonefunction_075','L_Leg_01_W'],
    ['bonefunction_076','R_Leg_00_W'],
    ['bonefunction_077','R_Leg_01_W'],

    ['bonefunction_080','L_Arm_01_T'],
    ['bonefunction_081','L_Arm_02_T'],
    ['bonefunction_082','R_Arm_01_T'],
    ['bonefunction_083','R_Arm_02_T'],
    ]
    
    for obj in bpy.context.selected_objects:
        v_groups = obj.vertex_groups
        for n in name_list:
            if n[0] in v_groups:
                v_groups[n[0]].name = n[1]
        
       

class MHWtoMHRRename(bpy.types.Operator):
    bl_idname = "tool.mhwtomhrrename"
    bl_label = "MHWorld to MHRise"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )

    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    


