import bpy

def main(context):
    unfixed_name_list = [
    ['下半身','_000'],
    ['上半身','_001'],
    ['上半身2','_002'],
    ['上半身2','_003'],
    ['首','_004'],
    ['首','_a04'],
    ['頭','_005'],
    
    ['肩.L','_a0a'],
    ['肩.L','_00a'],
    ['腕.L','_a0b'],
    ['腕.L','_00b'],
    ['腕.L','_a30'],
    ['ひじ.L','_a0c'],
    ['ひじ.L','_00c'],
    ['ひじ.L','_a37'],
    ['ひじ.L','_a38'],
    ['手捩.L','_a21'],
    ['手首.L','_00d'],
    ['手首.L','_a0d'],
    ['親指０.L','_200'],
    ['親指１.L','_201'],
    ['親指２.L','_202'],
    ['人指１.L','_211'],
    ['人指２.L','_212'],
    ['人指３.L','_213'],
    ['中指１.L','_221'],
    ['中指２.L','_222'],
    ['中指３.L','_223'],
    ['手首.L','_230'],
    ['薬指１.L','_231'],
    ['薬指２.L','_232'],
    ['薬指３.L','_233'],
    ['手首.L','_240'],
    ['小指１.L','_241'],
    ['小指２.L','_242'],
    ['小指３.L','_243'],
    ['ダミー.L','_401'],
    ['ダミー.L','_403'],
    
    ['肩.R','_a06'],
    ['肩.R','_006'],
    ['腕.R','_a07'],
    ['腕.R','_007'],
    ['腕.R','_a20'],
    ['ひじ.R','_a08'],
    ['ひじ.R','_008'],
    ['ひじ.R','_a27'],
    ['ひじ.R','_a28'],
    ['手捩.R','_a31'],
    ['手首.R','_009'],
    ['手首.R','_a09'],
    ['親指０.R','_100'],
    ['親指１.R','_101'],
    ['親指２.R','_102'],
    ['人指１.R','_111'],
    ['人指２.R','_112'],
    ['人指３.R','_113'],
    ['中指１.R','_121'],
    ['中指２.R','_122'],
    ['中指３.R','_123'],
    ['手首.R','_130'],
    ['薬指１.R','_131'],
    ['薬指２.R','_132'],
    ['薬指３.R','_133'],
    ['手首.R','_140'],
    ['小指１.R','_141'],
    ['小指２.R','_142'],
    ['小指３.R','_143'],
    ['ダミー.R','_400'],
    ['ダミー.R','_402'],
    
    ['足D.L','_012'],
    ['足D.L','_a12'],
    ['足D.L','_a34'],
    ['足D.L','_a35'],
    ['足D.L','_a36'],
    ['足D.L','_a32'],
    ['ひざD.L','_013'],
    ['ひざD.L','_a13'],
    ['ひざD.L','_a39'],
    ['ひざD.L','_a3a'],
    ['ひざD.L','_a33'],
    ['足首D.L','_014'],
    ['足首D.L','_a14'],
    ['足先EX.L','_015'],
    
    ['足D.R','_00e'],
    ['足D.R','_a0e'],
    ['足D.R','_a24'],
    ['足D.R','_a25'],
    ['足D.R','_a26'],
    ['足D.R','_a22'],
    ['ひざD.R','_00f'],
    ['ひざD.R','_a0f'],
    ['ひざD.R','_a29'],
    ['ひざD.R','_a2a'],
    ['ひざD.R','_a23'],
    ['足首D.R','_010'],
    ['足首D.R','_a10'],
    ['足先EX.R','_011']
    ]

    fixed_name_list = [
    ['Hips','_000'],
    ['Spine','_001'],
    ['Chest','_002'],
    ['Chest','_003'],
    ['Neck','_004'],
    ['Neck','_a04'],
    ['Head','_005'],
    
    ['Left shoulder','_a0a'],
    ['Left shoulder','_00a'],
    ['Left arm','_a0b'],
    ['Left arm','_00b'],
    ['Left elbow','_a0c'],
    ['Left elbow','_00c'],
    ['Left elbow','_a37'],
    ['Left elbow','_a38'],
    ['Left wrist','_00d'],
    ['Left wrist','_a0d'],
    ['Thumb0_L','_200'],
    ['Thumb1_L','_201'],
    ['Thumb2_L','_202'],
    ['IndexFinger1_L','_211'],
    ['IndexFinger2_L','_212'],
    ['IndexFinger3_L','_213'],
    ['MiddleFinger1_L','_221'],
    ['MiddleFinger2_L','_222'],
    ['MiddleFinger3_L','_223'],
    ['Left wrist','_230'],
    ['RingFinger1_L','_231'],
    ['RingFinger2_L','_232'],
    ['RingFinger3_L','_233'],
    ['Left wrist','_240'],
    ['LittleFinger1_L','_241'],
    ['LittleFinger2_L','_242'],
    ['LittleFinger3_L','_243'],
    
    ['Right shoulder','_a06'],
    ['Right shoulder','_006'],
    ['Right arm','_a07'],
    ['Right arm','_007'],
    ['Right elbow','_a08'],
    ['Right elbow','_008'],
    ['Right elbow','_a27'],
    ['Right elbow','_a28'],
    ['Right wrist','_009'],
    ['Right wrist','_a09'],
    ['Thumb0_R','_100'],
    ['Thumb1_R','_101'],
    ['Thumb2_R','_102'],
    ['IndexFinger1_R','_111'],
    ['IndexFinger2_R','_112'],
    ['IndexFinger3_R','_113'],
    ['MiddleFinger1_R','_121'],
    ['MiddleFinger2_R','_122'],
    ['MiddleFinger3_R','_123'],
    ['Right wrist','_130'],
    ['RingFinger1_R','_131'],
    ['RingFinger2_R','_132'],
    ['RingFinger3_R','_133'],
    ['Right wrist','_140'],
    ['LittleFinger1_R','_141'],
    ['LittleFinger2_R','_142'],
    ['LittleFinger3_R','_143'],
    
    ['Left leg','_012'],
    ['Left leg','_a12'],
    ['Left leg','_a34'],
    ['Left leg','_a35'],
    ['Left leg','_a36'],
    ['Left leg','_a32'],
    ['Left knee','_013'],
    ['Left knee','_a13'],
    ['Left knee','_a39'],
    ['Left knee','_a3a'],
    ['Left knee','_a33'],
    ['Left ankle','_014'],
    ['Left ankle','_a14'],
    ['Left toe','_015'],
    
    ['Right leg','_00e'],
    ['Right leg','_a0e'],
    ['Right leg','_a24'],
    ['Right leg','_a25'],
    ['Right leg','_a26'],
    ['Right leg','_a22'],
    ['Right knee','_00f'],
    ['Right knee','_a0f'],
    ['Right knee','_a29'],
    ['Right knee','_a2a'],
    ['Right knee','_a23'],
    ['Right ankle','_010'],
    ['Right ankle','_a10'],
    ['Right toe','_011'],

    ['zArmTwist_L','_a30'],
    ['zHandTwist_L','_a21'],

    ['zArmTwist_R','_a20'],
    ['zHandTwist_R','_a31']
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
                bpy.ops.armature.select_all(action='DESELECT')
                if n[1] == '_011' or n[1] == '_015':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.context.active_bone.head[1] = 0.018812 
                    bpy.context.active_bone.tail[1] = 0.068812
                elif n[1] == '_130' or n[1] == '_140' or n[1] == '_230' or n[1] == '_240':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.ops.armature.delete()
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
                bpy.ops.armature.select_all(action='DESELECT')
                if n[1] == '_011' or n[1] == '_015':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.context.active_bone.head[1] = 0.018812 
                    bpy.context.active_bone.tail[1] = 0.068812
                elif n[1] == '_130' or n[1] == '_140' or n[1] == '_230' or n[1] == '_240':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.ops.armature.delete()
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


class SnapBonesMMDtoGBFR(bpy.types.Operator):
    bl_idname = "tool.snapbonesmmdtogbfr"
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
    