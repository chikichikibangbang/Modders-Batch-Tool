import bpy

def main(context):
    unfixed_name_list = [
    ['下半身','_000'],
    ]

    fixed_name_list = [
    ['Hip','_000'],
    ['Waist','_001'],
    ['Spine','_002'],
    ['Chest','_003'],
    ['Neck','_004'],
    ['Neck','_a04'],
    ['Head','_005'],
    
    ['Shoulder_L','_a0a'],
    ['Shoulder_L','_00a'],
    ['Arm_L','_a0b'],
    ['Arm_L','_00b'],
    ['Elbow_L','_a0c'],
    ['Elbow_L','_00c'],
    ['Elbow_L','_a37'],
    ['Elbow_L','_a38'],
    ['Wrist_L','_00d'],
    ['Wrist_L','_a0d'],
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
    ['Wrist_L','_230'],
    ['Wrist_L','_240'],
   
    
    ['Shoulder_R','_a06'],
    ['Shoulder_R','_006'],
    ['Arm_R','_a07'],
    ['Arm_R','_007'],
    ['Elbow_R','_a08'],
    ['Elbow_R','_008'],
    ['Elbow_R','_a27'],
    ['Elbow_R','_a28'],
    ['Wrist_R','_009'],
    ['Wrist_R','_a09'],
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
    ['Wrist_R','_130'],
    ['Wrist_R','_140'],
    
    
    ['Thigh_L','_012'],
    ['Thigh_L','_a12'],
    ['Thigh_L','_a34'],
    ['Thigh_L','_a35'],
    ['Thigh_L','_a36'],
    ['Thigh_L','_a32'],
    ['Knee_L','_013'],
    ['Knee_L','_a13'],
    ['Knee_L','_a39'],
    ['Knee_L','_a3a'],
    ['Knee_L','_a33'],
    ['Ankle_offset_L','_014'],
    ['Ankle_offset_L','_a14'],
    ['Toe_offset_L','_015'],
    
    ['Thigh_R','_00e'],
    ['Thigh_R','_a0e'],
    ['Thigh_R','_a24'],
    ['Thigh_R','_a25'],
    ['Thigh_R','_a26'],
    ['Thigh_R','_a22'],
    ['Knee_R','_00f'],
    ['Knee_R','_a0f'],
    ['Knee_R','_a29'],
    ['Knee_R','_a2a'],
    ['Knee_R','_a23'],
    ['Ankle_offset_R','_010'],
    ['Ankle_offset_R','_a10'],
    ['Toe_offset_R','_011'],

    ['ShoulderRoll_L','_a30'],
    ['ArmRoll_L','_a21'],
    ['ShoulderRoll_R','_a20'],
    ['ArmRoll_R','_a31'],
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
                bpy.ops.armature.select_all(action='DESELECT')
                #bpy.context.area.type = 'TEXT_EDITOR'
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


class SnapBonesUMAtoGBFR(bpy.types.Operator):
    bl_idname = "tool.snapbonesumatogbfr"
    bl_label = "UMA Armature"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "ARMATURE" ) and bool(bpy.context.object.mode == "OBJECT") 
    
    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'adsorption completed')
        return {'FINISHED'}
    