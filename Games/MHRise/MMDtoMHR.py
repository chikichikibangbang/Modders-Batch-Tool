import bpy


def main(context):
    unfixed_name_list = [
    ['下半身','Waist_00'],
    ['上半身','Spine_00'],
    ['上半身2','Spine_01'],
    ['首','Neck_00'],
    ['頭','Head_00'],
    
    ['肩.L','L_Arm_00'],
    ['腕.L','L_Arm_01'],
    ['ひじ.L','L_Arm_02'],
    ['手首.L','L_Arm_03'],
    ['親指０.L','L_Finger_00'],
    ['親指１.L','L_Finger_01'],
    ['親指２.L','L_Finger_02'],
    ['人指１.L','L_Finger_03'],
    ['人指２.L','L_Finger_04'],
    ['人指３.L','L_Finger_05'],
    ['中指１.L','L_Finger_06'],
    ['中指２.L','L_Finger_07'],
    ['中指３.L','L_Finger_08'],
    ['自定义L','L_Finger_09'],
    ['薬指１.L','L_Finger_10'],
    ['薬指２.L','L_Finger_11'],
    ['薬指３.L','L_Finger_12'],
    ['小指１.L','L_Finger_13'],
    ['小指２.L','L_Finger_14'],
    ['小指３.L','L_Finger_15'],
    
    ['肩.R','R_Arm_00'],
    ['腕.R','R_Arm_01'],
    ['ひじ.R','R_Arm_02'],
    ['手首.R','R_Arm_03'],
    ['親指０.R','R_Finger_00'],
    ['親指１.R','R_Finger_01'],
    ['親指２.R','R_Finger_02'],
    ['人指１.R','R_Finger_03'],
    ['人指２.R','R_Finger_04'],
    ['人指３.R','R_Finger_05'],
    ['中指１.R','R_Finger_06'],
    ['中指２.R','R_Finger_07'],
    ['中指３.R','R_Finger_08'],
    ['自定义R','R_Grip_00'],
    ['薬指１.R','R_Finger_09'],
    ['薬指２.R','R_Finger_10'],
    ['薬指３.R','R_Finger_11'],
    ['小指１.R','R_Finger_12'],
    ['小指２.R','R_Finger_13'],
    ['小指３.R','R_Finger_14'],
    
    ['足D.L','L_Leg_00'],
    ['ひざD.L','L_Leg_01'],
    ['足首D.L','L_Leg_02'],
    ['足先EX.L','L_Leg_03'],
    
    ['足D.R','R_Leg_00'],
    ['ひざD.R','R_Leg_01'],
    ['足首D.R','R_Leg_02'],
    ['足先EX.R','R_Leg_03'],
    
    ['自定义1','L_Arm_00_W'],
    ['+ひじ補助.L','L_Arm_01_W'],
    ['ひじ補助.L','L_Arm_01_W'],
    ['自定义3','L_Arm_01_T'],
    ['自定义4','L_Arm_02_T'],

    ['自定义5','R_Arm_00_W'],
    ['+ひじ補助.R','R_Arm_01_W'],
    ['ひじ補助.R','R_Arm_01_W'],
    ['自定义7','R_Arm_01_T'],
    ['自定义8','R_Arm_02_T'],

    ['お尻.L','L_Leg_00_W'],
    ['+ひざ補助.L','L_Leg_01_W'],
    ['ひざ補助.L','L_Leg_01_W'],
    ['自定义11','L_Leg_02_T'],
    
    ['お尻.R','R_Leg_00_W'],
    ['+ひざ補助.R','R_Leg_01_W'],
    ['ひざ補助.R','R_Leg_01_W'],
    ['自定义14','R_Leg_02_T'],
    ]

    fixed_name_list = [
    ['Hips','Waist_00'],
    ['Spine','Spine_00'],
    ['Chest','Spine_01'],
    ['Neck','Neck_00'],
    ['Head','Head_00'],
    
    ['Left shoulder','L_Arm_00'],
    ['zArmTwist_L','L_Arm_01'],
    ['Left elbow','L_Arm_02'],
    ['Left wrist','L_Arm_03'],
    ['Thumb0_L','L_Finger_00'],
    ['Thumb1_L','L_Finger_01'],
    ['Thumb2_L','L_Finger_02'],
    ['IndexFinger1_L','L_Finger_03'],
    ['IndexFinger2_L','L_Finger_04'],
    ['IndexFinger3_L','L_Finger_05'],
    ['MiddleFinger1_L','L_Finger_06'],
    ['MiddleFinger2_L','L_Finger_07'],
    ['MiddleFinger3_L','L_Finger_08'],
    ['自定义L','L_Finger_09'],
    ['RingFinger1_L','L_Finger_10'],
    ['RingFinger2_L','L_Finger_11'],
    ['RingFinger3_L','L_Finger_12'],
    ['LittleFinger1_L','L_Finger_13'],
    ['LittleFinger2_L','L_Finger_14'],
    ['LittleFinger3_L','L_Finger_15'],
    
    ['Right shoulder','R_Arm_00'],
    ['zArmTwist_R','R_Arm_01'],
    ['Right elbow','R_Arm_02'],
    ['Right wrist','R_Arm_03'],
    ['Thumb0_R','R_Finger_00'],
    ['Thumb1_R','R_Finger_01'],
    ['Thumb2_R','R_Finger_02'],
    ['IndexFinger1_R','R_Finger_03'],
    ['IndexFinger2_R','R_Finger_04'],
    ['IndexFinger3_R','R_Finger_05'],
    ['MiddleFinger1_R','R_Finger_06'],
    ['MiddleFinger2_R','R_Finger_07'],
    ['MiddleFinger3_R','R_Finger_08'],
    ['自定义R','R_Grip_00'],
    ['RingFinger1_R','R_Finger_09'],
    ['RingFinger2_R','R_Finger_10'],
    ['RingFinger3_R','R_Finger_11'],
    ['LittleFinger1_R','R_Finger_12'],
    ['LittleFinger2_R','R_Finger_13'],
    ['LittleFinger3_R','R_Finger_14'],
    
    ['Left leg','L_Leg_00'],
    ['Left knee','L_Leg_01'],
    ['Left ankle','L_Leg_02'],
    ['Left toe','L_Leg_03'],
    
    ['Right leg','R_Leg_00'],
    ['Right knee','R_Leg_01'],
    ['Right ankle','R_Leg_02'],
    ['Right toe','R_Leg_03'],
    
    ['自定义1','L_Arm_00_W'],
    ['+ElbowAux_L','L_Arm_01_W'],
    ['ElbowAux_L','L_Arm_01_W'],
    ['Left arm','L_Arm_01_T'],
    ['zHandTwist_L','L_Arm_02_T'],

    ['自定义5','R_Arm_00_W'],
    ['+ElbowAux_R','R_Arm_01_W'],
    ['ElbowAux_R','R_Arm_01_W'],
    ['Right arm','R_Arm_01_T'],
    ['zHandTwist_R','R_Arm_02_T'],

    ['OhButt_L','L_Leg_00_W'],
    ['+KneeAux_L','L_Leg_01_W'],
    ['KneeAux_L','L_Leg_01_W'],
    ['自定义11','L_Leg_02_T'],
    
    ['OhButt_R','R_Leg_00_W'],
    ['+KneeAux_R','R_Leg_01_W'],
    ['KneeAux_R','R_Leg_01_W'],
    ['自定义14','R_Leg_02_T'],
    ]
    
    for obj in bpy.context.selected_objects:
        v_groups = obj.vertex_groups
        if unfixed_name_list[0][0] in v_groups:
            for n in unfixed_name_list:
                if n[0] in v_groups:
                    v_groups[n[0]].name = n[1]
        elif fixed_name_list[0][0] in v_groups:
            for n in fixed_name_list:
                if n[0] in v_groups:
                    v_groups[n[0]].name = n[1]
        
       

class MMDtoMHRRename(bpy.types.Operator):
    bl_idname = "tool.mmdtomhrrename"
    bl_label = "MMD to MHRise"
    bl_options = {'REGISTER', 'UNDO'}
  
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )

    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    


