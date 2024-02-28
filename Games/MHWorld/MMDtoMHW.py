import bpy


def main(context):
    unfixed_name_list = [
    ['下半身','bonefunction_013'],
    ['上半身','bonefunction_001'],
    ['上半身2','bonefunction_002'],
    ['首','bonefunction_003'],
    ['頭','bonefunction_004'],
    
    ['肩.L','bonefunction_005'],
    ['腕.L','bonefunction_006'],
    ['ひじ.L','bonefunction_007'],
    ['手首.L','bonefunction_008'],
    ['親指０.L','bonefunction_031'],
    ['親指１.L','bonefunction_032'],
    ['親指２.L','bonefunction_033'],
    ['人指１.L','bonefunction_034'],
    ['人指２.L','bonefunction_035'],
    ['人指３.L','bonefunction_036'],
    ['中指１.L','bonefunction_037'],
    ['中指２.L','bonefunction_038'],
    ['中指３.L','bonefunction_039'],
    ['自定义L','bonefunction_040'],
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
    ['親指０.R','bonefunction_048'],
    ['親指１.R','bonefunction_049'],
    ['親指２.R','bonefunction_050'],
    ['人指１.R','bonefunction_051'],
    ['人指２.R','bonefunction_052'],
    ['人指３.R','bonefunction_053'],
    ['中指１.R','bonefunction_054'],
    ['中指２.R','bonefunction_055'],
    ['中指３.R','bonefunction_056'],
    ['自定义R','bonefunction_057'],
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
    
    ['自定义1','bonefunction_070'],
    ['+ひじ補助.L','bonefunction_071'],
    ['ひじ補助.L','bonefunction_071'],
    ['自定义3','bonefunction_080'],
    ['自定义4','bonefunction_081'],

    ['自定义5','bonefunction_072'],
    ['+ひじ補助.R','bonefunction_073'],
    ['ひじ補助.R','bonefunction_073'],
    ['自定义7','bonefunction_082'],
    ['自定义8','bonefunction_083'],

    ['お尻.L','bonefunction_074'],
    ['+ひざ補助.L','bonefunction_075'],
    ['ひざ補助.L','bonefunction_075'],
    ['自定义11','bonefunction_084'],
    
    ['お尻.R','bonefunction_076'],
    ['+ひざ補助.R','bonefunction_077'],
    ['ひざ補助.R','bonefunction_077'],
    ['自定义14','bonefunction_085'],
    ]

    fixed_name_list = [
    ['Hips','bonefunction_013'],
    ['Spine','bonefunction_001'],
    ['Chest','bonefunction_002'],
    ['Neck','bonefunction_003'],
    ['Head','bonefunction_004'],
    
    ['Left shoulder','bonefunction_005'],
    ['zArmTwist_L','bonefunction_006'],
    ['Left elbow','bonefunction_007'],
    ['Left wrist','bonefunction_008'],
    ['Thumb0_L','bonefunction_031'],
    ['Thumb1_L','bonefunction_032'],
    ['Thumb2_L','bonefunction_033'],
    ['IndexFinger1_L','bonefunction_034'],
    ['IndexFinger2_L','bonefunction_035'],
    ['IndexFinger3_L','bonefunction_036'],
    ['MiddleFinger1_L','bonefunction_037'],
    ['MiddleFinger2_L','bonefunction_038'],
    ['MiddleFinger3_L','bonefunction_039'],
    ['自定义L','bonefunction_040'],
    ['RingFinger1_L','bonefunction_041'],
    ['RingFinger2_L','bonefunction_042'],
    ['RingFinger3_L','bonefunction_043'],
    ['LittleFinger1_L','bonefunction_044'],
    ['LittleFinger2_L','bonefunction_045'],
    ['LittleFinger3_L','bonefunction_046'],
    
    ['Right shoulder','bonefunction_009'],
    ['zArmTwist_R','bonefunction_010'],
    ['Right elbow','bonefunction_011'],
    ['Right wrist','bonefunction_012'],
    ['Thumb0_R','bonefunction_048'],
    ['Thumb1_R','bonefunction_049'],
    ['Thumb2_R','bonefunction_050'],
    ['IndexFinger1_R','bonefunction_051'],
    ['IndexFinger2_R','bonefunction_052'],
    ['IndexFinger3_R','bonefunction_053'],
    ['MiddleFinger1_R','bonefunction_054'],
    ['MiddleFinger2_R','bonefunction_055'],
    ['MiddleFinger3_R','bonefunction_056'],
    ['自定义R','bonefunction_057'],
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
    
    ['自定义1','bonefunction_070'],
    ['+ElbowAux_L','bonefunction_071'],
    ['ElbowAux_L','bonefunction_071'],
    ['Left arm','bonefunction_080'],
    ['zHandTwist_L','bonefunction_081'],

    ['自定义5','bonefunction_072'],
    ['+ElbowAux_R','bonefunction_073'],
    ['ElbowAux_R','bonefunction_073'],
    ['Right arm','bonefunction_082'],
    ['zHandTwist_R','bonefunction_083'],

    ['OhButt_L','bonefunction_074'],
    ['+KneeAux_L','bonefunction_075'],
    ['KneeAux_L','bonefunction_075'],
    ['自定义11','bonefunction_084'],
    
    ['OhButt_R','bonefunction_076'],
    ['+KneeAux_R','bonefunction_077'],
    ['KneeAux_R','bonefunction_077'],
    ['自定义14','bonefunction_085'],
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
        
       

class MMDtoMHWRename(bpy.types.Operator):
    bl_idname = "tool.mmdtomhwrename"
    bl_label = "MMD to MHWorld"
    bl_options = {'REGISTER', 'UNDO'}
  
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )

    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    


