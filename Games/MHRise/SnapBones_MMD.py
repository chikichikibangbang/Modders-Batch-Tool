import bpy

def main(context):
    unfixed_name_list = [
    ['下半身','Waist_00'],
    ['上半身','Spine_00'],
    ['上半身2','Spine_01'],
    ['首','Neck_00'],
    ['首','Neck_00_S'],
    ['頭','Head_00'],
    
    ['肩.L','L_Arm_00'],
    ['腕.L','L_Arm_01'],
    ['ひじ.L','L_Arm_02'],
    ['手首.L','L_Arm_03'],
    ['手首.L','L_Weapon_00'],
    ['親指０.L','L_Finger_00'],
    ['親指１.L','L_Finger_01'],
    ['親指２.L','L_Finger_02'],
    ['人指１.L','L_Finger_03'],
    ['人指２.L','L_Finger_04'],
    ['人指３.L','L_Finger_05'],
    ['中指１.L','L_Finger_06'],
    ['中指２.L','L_Finger_07'],
    ['中指３.L','L_Finger_08'],

    ['手首.L','L_Finger_09'],

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
    ['手首.R','R_Weapon_00'],
    ['親指０.R','R_Finger_00'],
    ['親指１.R','R_Finger_01'],
    ['親指２.R','R_Finger_02'],
    ['人指１.R','R_Finger_03'],
    ['人指２.R','R_Finger_04'],
    ['人指３.R','R_Finger_05'],
    ['中指１.R','R_Finger_06'],
    ['中指２.R','R_Finger_07'],
    ['中指３.R','R_Finger_08'],

    ['手首.R','R_Grip_00'],

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
   
    ['腕.L','L_Arm_00_W'],
    ['ひじ.L','L_Arm_01_W'],
    ['腕.L','L_Arm_01_T'],
    ['手捩.L','L_Arm_02_T'],

    ['腕.R','R_Arm_00_W'],
    ['ひじ.R','R_Arm_01_W'],
    ['腕.R','R_Arm_01_T'],
    ['手捩.R','R_Arm_02_T'],

    ['足D.L','L_Leg_00_W'],
    ['ひざD.L','L_Leg_01_W'],
    ['足首D.L','L_Leg_02_T'],
    
    ['足D.R','R_Leg_00_W'],
    ['ひざD.R','R_Leg_01_W'],
    ['足首D.R','R_Leg_02_T']
    ]

    fixed_name_list = [
    ['Hips','Waist_00'],
    ['Spine','Spine_00'],
    ['Chest','Spine_01'],
    ['Neck','Neck_00'],
    ['Neck','Neck_00_S'],
    ['Head','Head_00'],
  
    ['Left shoulder','L_Arm_00'],
    ['Left arm','L_Arm_01'],
    ['Left elbow','L_Arm_02'],
    ['Left wrist','L_Arm_03'],
    ['Left wrist','L_Weapon_00'],
    ['Thumb0_L','L_Finger_00'],
    ['Thumb1_L','L_Finger_01'],
    ['Thumb2_L','L_Finger_02'],
    ['IndexFinger1_L','L_Finger_03'],
    ['IndexFinger2_L','L_Finger_04'],
    ['IndexFinger3_L','L_Finger_05'],
    ['MiddleFinger1_L','L_Finger_06'],
    ['MiddleFinger2_L','L_Finger_07'],
    ['MiddleFinger3_L','L_Finger_08'],

    ['Left wrist','L_Finger_09'],

    ['RingFinger1_L','L_Finger_10'],
    ['RingFinger2_L','L_Finger_11'],
    ['RingFinger3_L','L_Finger_12'],
    ['LittleFinger1_L','L_Finger_13'],
    ['LittleFinger2_L','L_Finger_14'],
    ['LittleFinger3_L','L_Finger_15'],
    
    ['Right shoulder','R_Arm_00'],
    ['Right arm','R_Arm_01'],
    ['Right elbow','R_Arm_02'],
    ['Right wrist','R_Arm_03'],
    ['Right wrist','R_Weapon_00'],
    ['Thumb0_R','R_Finger_00'],
    ['Thumb1_R','R_Finger_01'],
    ['Thumb2_R','R_Finger_02'],
    ['IndexFinger1_R','R_Finger_03'],
    ['IndexFinger2_R','R_Finger_04'],
    ['IndexFinger3_R','R_Finger_05'],
    ['MiddleFinger1_R','R_Finger_06'],
    ['MiddleFinger2_R','R_Finger_07'],
    ['MiddleFinger3_R','R_Finger_08'],

    ['Right wrist','R_Grip_00'],

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
   
    ['Left arm','L_Arm_00_W'],
    ['Left elbow','L_Arm_01_W'],
    ['Left arm','L_Arm_01_T'],
    ['zHandTwist_L','L_Arm_02_T'],

    ['Right arm','R_Arm_00_W'],
    ['Right elbow','R_Arm_01_W'],
    ['Right arm','R_Arm_01_T'],
    ['zHandTwist_R','R_Arm_02_T'],

    ['Left leg','L_Leg_00_W'],
    ['Left knee','L_Leg_01_W'],
    ['Left ankle','L_Leg_02_T'],
    
    ['Right leg','R_Leg_00_W'],
    ['Right knee','R_Leg_01_W'],
    ['Right ankle','R_Leg_02_T']
    ]



    obj0 = bpy.context.active_object.data.bones 
    name_save = ['']*len(obj0)
    for i in range(len(obj0)):
        name_save[i] = obj0[i].name


    bpy.ops.object.join()
    ArmatureName = bpy.context.active_object.data.name
    obj = bpy.context.active_object.data.bones 

    name_in = ['']*len(obj)
    for i in range(len(obj)):
        name_in[i] = obj[i].name
    
    if unfixed_name_list[0][0] in name_in: 
        for n in unfixed_name_list:
            if n[0] not in name_in:
                continue
            else:
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[0]]
                bpy.context.object.data.use_mirror_x = False
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=n[0], case_sensitive=False, extend=True)
                bpy.ops.object.select_pattern(pattern=n[1], case_sensitive=False, extend=True)
                bpy.context.area.type = 'VIEW_3D'
                bpy.ops.view3d.snap_selected_to_active()
                #bpy.context.area.type = 'TEXT_EDITOR'
                if n[1] == 'L_Leg_03' or n[1] == 'R_Leg_03':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.context.active_bone.head[1] = -104.611 
                    bpy.context.active_bone.tail[1] = -89.8527
                bpy.ops.armature.select_all(action='DESELECT')
                #print(n[0],n[1])
    elif fixed_name_list[0][0] in name_in: 
        for n in fixed_name_list:
            if n[0] not in name_in:
                continue
            else:
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[0]]
                bpy.context.object.data.use_mirror_x = False
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=n[0], case_sensitive=False, extend=True)
                bpy.ops.object.select_pattern(pattern=n[1], case_sensitive=False, extend=True)
                bpy.context.area.type = 'VIEW_3D'
                bpy.ops.view3d.snap_selected_to_active()
                #bpy.context.area.type = 'TEXT_EDITOR'
                if n[1] == 'L_Leg_03' or n[1] == 'R_Leg_03':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.context.active_bone.head[1] = -104.611 
                    bpy.context.active_bone.tail[1] = -89.8527
                bpy.ops.armature.select_all(action='DESELECT')
                #print(n[0],n[1])

    for i in range(32):
        bpy.context.object.data.layers[i] = True

    for i in range(len(obj)):
        if name_in[i] in name_save:
            continue
        else:
            bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[name_in[i]]
            bpy.ops.armature.delete()

    bpy.ops.object.mode_set(mode='OBJECT')


class SnapBonesMMDtoMHR(bpy.types.Operator):
    bl_idname = "tool.snapbonesmmdtomhr"
    bl_label = "MMD Armature"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "ARMATURE" ) and bool(bpy.context.object.mode == "OBJECT") 
    
    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'adsorption completed')
        return {'FINISHED'}
    