import bpy
import copy

def main(context):
    unfixed_name_list = [
    ['下半身','bonefunction_013'],
    ['上半身','bonefunction_001'],
    ['上半身2','bonefunction_002'],
    ['首','bonefunction_003'],
    ['頭','bonefunction_004'],
    ['首','bonefunction_254'],   
    
    ['肩.L','bonefunction_005'],
    ['腕.L','bonefunction_006'],
    ['ひじ.L','bonefunction_007'],
    ['手首.L','bonefunction_008'],
    ['手首.L','bonefunction_030'],
    ['親指０.L','bonefunction_031'],
    ['親指１.L','bonefunction_032'],
    ['親指２.L','bonefunction_033'],
    ['人指１.L','bonefunction_034'],
    ['人指２.L','bonefunction_035'],
    ['人指３.L','bonefunction_036'],
    ['中指１.L','bonefunction_037'],
    ['中指２.L','bonefunction_038'],
    ['中指３.L','bonefunction_039'],

    ['手首.L','bonefunction_040'],

    ['薬指１.L','bonefunction_041'],
    ['薬指２.L','bonefunction_042'],
    ['薬指３.L','bonefunction_043'],
    ['小指１.L','bonefunction_044'],
    ['小指２.L','bonefunction_045'],
    ['小指３.L','bonefunction_046'],
    
    ['肩.R','bonefunction_009'],
    ['腕.R','bonefunction_010'],
    ['ひじ.R','bonefunction_011'],
    ['手首.R','bonefunction_012'],
    ['手首.R','bonefunction_047'],
    ['親指０.R','bonefunction_048'],
    ['親指１.R','bonefunction_049'],
    ['親指２.R','bonefunction_050'],
    ['人指１.R','bonefunction_051'],
    ['人指２.R','bonefunction_052'],
    ['人指３.R','bonefunction_053'],
    ['中指１.R','bonefunction_054'],
    ['中指２.R','bonefunction_055'],
    ['中指３.R','bonefunction_056'],

    ['手首.R','bonefunction_057'],

    ['薬指１.R','bonefunction_058'],
    ['薬指２.R','bonefunction_059'],
    ['薬指３.R','bonefunction_060'],
    ['小指１.R','bonefunction_061'],
    ['小指２.R','bonefunction_062'],
    ['小指３.R','bonefunction_063'],
    
    ['足D.L','bonefunction_014'],
    ['ひざD.L','bonefunction_015'],
    ['足首D.L','bonefunction_016'],
    ['足先EX.L','bonefunction_017'],
    
    ['足D.R','bonefunction_018'],
    ['ひざD.R','bonefunction_019'],
    ['足首D.R','bonefunction_020'],
    ['足先EX.R','bonefunction_021'],
   
    ['腕.L','bonefunction_070'],
    ['ひじ.L','bonefunction_071'],
    ['腕.L','bonefunction_080'],
    ['手捩.L','bonefunction_081'],

    ['腕.R','bonefunction_072'],
    ['ひじ.R','bonefunction_073'],
    ['腕.R','bonefunction_082'],
    ['手捩.R','bonefunction_083'],

    ['足D.L','bonefunction_074'],
    ['ひざD.L','bonefunction_075'],
    ['足首D.L','bonefunction_084'],
    
    ['足D.R','bonefunction_076'],
    ['ひざD.R','bonefunction_077'],
    ['足首D.R','bonefunction_085']
    ]

    fixed_name_list = [
    ['Hips','bonefunction_013'],
    ['Spine','bonefunction_001'],
    ['Chest','bonefunction_002'],
    ['Neck','bonefunction_003'],
    ['Head','bonefunction_004'],
    ['Neck','bonefunction_254'],
  
    ['Left shoulder','bonefunction_005'],
    ['Left arm','bonefunction_006'],
    ['Left elbow','bonefunction_007'],
    ['Left wrist','bonefunction_008'],
    ['Left wrist','bonefunction_030'],
    ['Thumb0_L','bonefunction_031'],
    ['Thumb1_L','bonefunction_032'],
    ['Thumb2_L','bonefunction_033'],
    ['IndexFinger1_L','bonefunction_034'],
    ['IndexFinger2_L','bonefunction_035'],
    ['IndexFinger3_L','bonefunction_036'],
    ['MiddleFinger1_L','bonefunction_037'],
    ['MiddleFinger2_L','bonefunction_038'],
    ['MiddleFinger3_L','bonefunction_039'],

    ['Left wrist','bonefunction_040'],

    ['RingFinger1_L','bonefunction_041'],
    ['RingFinger2_L','bonefunction_042'],
    ['RingFinger3_L','bonefunction_043'],
    ['LittleFinger1_L','bonefunction_044'],
    ['LittleFinger2_L','bonefunction_045'],
    ['LittleFinger3_L','bonefunction_046'],
    
    ['Right shoulder','bonefunction_009'],
    ['Right arm','bonefunction_010'],
    ['Right elbow','bonefunction_011'],
    ['Right wrist','bonefunction_012'],
    ['Right wrist','bonefunction_047'],
    ['Thumb0_R','bonefunction_048'],
    ['Thumb1_R','bonefunction_049'],
    ['Thumb2_R','bonefunction_050'],
    ['IndexFinger1_R','bonefunction_051'],
    ['IndexFinger2_R','bonefunction_052'],
    ['IndexFinger3_R','bonefunction_053'],
    ['MiddleFinger1_R','bonefunction_054'],
    ['MiddleFinger2_R','bonefunction_055'],
    ['MiddleFinger3_R','bonefunction_056'],

    ['Right wrist','bonefunction_057'],

    ['RingFinger1_R','bonefunction_058'],
    ['RingFinger2_R','bonefunction_059'],
    ['RingFinger3_R','bonefunction_060'],
    ['LittleFinger1_R','bonefunction_061'],
    ['LittleFinger2_R','bonefunction_062'],
    ['LittleFinger3_R','bonefunction_063'],
    
    ['Left leg','bonefunction_014'],
    ['Left knee','bonefunction_015'],
    ['Left ankle','bonefunction_016'],
    ['Left toe','bonefunction_017'],
    
    ['Right leg','bonefunction_018'],
    ['Right knee','bonefunction_019'],
    ['Right ankle','bonefunction_020'],
    ['Right toe','bonefunction_021'],
   
    ['Left arm','bonefunction_070'],
    ['Left elbow','bonefunction_071'],
    ['Left arm','bonefunction_080'],
    ['zHandTwist_L','bonefunction_081'],

    ['Right arm','bonefunction_072'],
    ['Right elbow','bonefunction_073'],
    ['Right arm','bonefunction_082'],
    ['zHandTwist_R','bonefunction_083'],

    ['Left leg','bonefunction_074'],
    ['Left knee','bonefunction_075'],
    ['Left ankle','bonefunction_084'],
    
    ['Right leg','bonefunction_076'],
    ['Right knee','bonefunction_077'],
    ['Right ankle','bonefunction_085']
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
                if n[1] == 'bonefunction_007':
                    before_snap_head = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].head   
                    before_snap_tail = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].tail
                    before_snap_head = copy.deepcopy(before_snap_head)
                    before_snap_tail = copy.deepcopy(before_snap_tail)
                bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[0]]
                bpy.context.object.data.use_mirror_x = False
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=n[0], case_sensitive=False, extend=True)
                bpy.ops.object.select_pattern(pattern=n[1], case_sensitive=False, extend=True)
                bpy.context.area.type = 'VIEW_3D'
                bpy.ops.view3d.snap_selected_to_active()
                #bpy.context.area.type = 'TEXT_EDITOR'
                if n[1] == 'bonefunction_017' or n[1] == 'bonefunction_021':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.context.active_bone.head[1] = -104.611   
                    bpy.context.active_bone.tail[1] = -104.607
                if n[1] == 'bonefunction_007':
                    after_snap_head = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].head   
                    after_snap_tail = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].tail
                    snap_head_distance = after_snap_head - before_snap_head  
                    snap_tail_distance = after_snap_tail - before_snap_tail
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_101"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_101"].tail += snap_tail_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_102"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_102"].tail += snap_tail_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_103"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_103"].tail += snap_tail_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_104"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_104"].tail += snap_tail_distance

                bpy.ops.armature.select_all(action='DESELECT')
                #print(n[0],n[1])
    elif fixed_name_list[0][0] in name_in: 
        for n in fixed_name_list:
            if n[0] not in name_in:
                continue
            else:
                bpy.ops.object.mode_set(mode='EDIT')
                if n[1] == 'bonefunction_007':
                    before_snap_head = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].head   
                    before_snap_tail = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].tail
                    before_snap_head = copy.deepcopy(before_snap_head)
                    before_snap_tail = copy.deepcopy(before_snap_tail)
                bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[0]]
                bpy.context.object.data.use_mirror_x = False
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=n[0], case_sensitive=False, extend=True)
                bpy.ops.object.select_pattern(pattern=n[1], case_sensitive=False, extend=True)
                bpy.context.area.type = 'VIEW_3D'
                bpy.ops.view3d.snap_selected_to_active()
                #bpy.context.area.type = 'TEXT_EDITOR'
                if n[1] == 'bonefunction_017' or n[1] == 'bonefunction_021':
                    bpy.data.armatures[ArmatureName].edit_bones.active = bpy.data.armatures[ArmatureName].edit_bones[n[1]]
                    bpy.context.active_bone.head[1] = -104.611   
                    bpy.context.active_bone.tail[1] = -104.607 
                if n[1] == 'bonefunction_007':
                    after_snap_head = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].head   
                    after_snap_tail = bpy.data.armatures[ArmatureName].edit_bones["bonefunction_007"].tail
                    snap_head_distance = after_snap_head - before_snap_head  
                    snap_tail_distance = after_snap_tail - before_snap_tail
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_101"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_101"].tail += snap_tail_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_102"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_102"].tail += snap_tail_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_103"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_103"].tail += snap_tail_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_104"].head += snap_head_distance
                    bpy.data.armatures[ArmatureName].edit_bones["bonefunction_104"].tail += snap_tail_distance

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


class SnapBonesMMDtoMHW(bpy.types.Operator):
    bl_idname = "tool.snapbonesmmdtomhw"
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
    