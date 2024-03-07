import bpy


def main(context):
    unfixed_name_list = [
    ['下半身','_000'],
    ['上半身','_001'],
    ['上半身2','_002'],
    ['首','_004'],
    ['頭','_005'],
    
    ['肩.L','_a0a'],
    ['腕.L','_a0b'],
    ['ひじ.L','_00c'],
    ['手首.L','_00d'],
    ['親指０.L','_200'],
    ['親指１.L','_201'],
    ['親指２.L','_202'],
    ['人指１.L','_211'],
    ['人指２.L','_212'],
    ['人指３.L','_213'],
    ['中指１.L','_221'],
    ['中指２.L','_222'],
    ['中指３.L','_223'],
    ['自定义L1','_230'],
    ['薬指１.L','_231'],
    ['薬指２.L','_232'],
    ['薬指３.L','_233'],
    ['自定义L2','_240'],
    ['小指１.L','_241'],
    ['小指２.L','_242'],
    ['小指３.L','_243'],
    
    ['肩.R','_a06'],
    ['腕.R','_a07'],
    ['ひじ.R','_008'],
    ['手首.R','_009'],
    ['親指０.R','_100'],
    ['親指１.R','_101'],
    ['親指２.R','_102'],
    ['人指１.R','_111'],
    ['人指２.R','_112'],
    ['人指３.R','_113'],
    ['中指１.R','_121'],
    ['中指２.R','_122'],
    ['中指３.R','_123'],
    ['自定义R1','_130'],
    ['薬指１.R','_131'],
    ['薬指２.R','_132'],
    ['薬指３.R','_133'],
    ['自定义R2','_140'],
    ['小指１.R','_141'],
    ['小指２.R','_142'],
    ['小指３.R','_143'],
    
    ['足D.L','_a12'],
    ['ひざD.L','_013'],
    ['足首D.L','_014'],
    ['足先EX.L','_015'],
    
    ['足D.R','_a0e'],
    ['ひざD.R','_00f'],
    ['足首D.R','_010'],
    ['足先EX.R','_011'],
    
    ['+ひじ補助.L','_a38'],
    ['ひじ補助.L','_a38'],
    ['自定义4','_a0d'],
    ['自定义5','_a30'],
    ['自定义6','_a21'],

    ['+ひじ補助.R','_a28'],
    ['ひじ補助.R','_a28'],
    ['自定义8','_a09'],
    ['自定义9','_a20'],
    ['自定义10','_a31'],

    ['お尻.L','a36'],
    ['+ひざ補助.L','_a39'],
    ['ひざ補助.L','_a39'],
    ['自定义11','_a14'],
    
    ['お尻.R','a26'],
    ['+ひざ補助.R','_a29'],
    ['ひざ補助.R','_a29'],
    ['自定义12','_a10'],
    ]

    fixed_name_list = [
    ['Hips','_000'],
    ['Spine','_001'],
    ['Chest','_002'],
    ['Neck','_004'],
    ['Head','_005'],
    
    ['Left shoulder','_a0a'],
    ['zArmTwist_L','_00b'],
    ['Left elbow','_00c'],
    ['Left wrist','_00d'],
    ['Thumb0_L','_200'],
    ['Thumb1_L','_201'],
    ['Thumb2_L','_202'],
    ['IndexFinger1_L','_211'],
    ['IndexFinger2_L','_212'],
    ['IndexFinger3_L','_213'],
    ['MiddleFinger1_L','_221'],
    ['MiddleFinger2_L','_222'],
    ['MiddleFinger3_L','_223'],
    ['自定义L1','_230'],
    ['RingFinger1_L','_231'],
    ['RingFinger2_L','_232'],
    ['RingFinger3_L','_233'],
    ['自定义L2','_240'],
    ['LittleFinger1_L','_241'],
    ['LittleFinger2_L','_242'],
    ['LittleFinger3_L','_243'],
    
    ['Right shoulder','_a06'],
    ['zArmTwist_R','_007'],
    ['Right elbow','_008'],
    ['Right wrist','_009'],
    ['Thumb0_R','_100'],
    ['Thumb1_R','_101'],
    ['Thumb2_R','_102'],
    ['IndexFinger1_R','_111'],
    ['IndexFinger2_R','_112'],
    ['IndexFinger3_R','_113'],
    ['MiddleFinger1_R','_121'],
    ['MiddleFinger2_R','_122'],
    ['MiddleFinger3_R','_123'],
    ['自定义R1','_130'],
    ['RingFinger1_R','_131'],
    ['RingFinger2_R','_132'],
    ['RingFinger3_R','_133'],
    ['自定义R2','_140'],
    ['LittleFinger1_R','_141'],
    ['LittleFinger2_R','_142'],
    ['LittleFinger3_R','_143'],
    
    ['Left leg','_a12'],
    ['Left knee','_013'],
    ['Left ankle','_014'],
    ['Left toe','_015'],
    
    ['Right leg','_a0e'],
    ['Right knee','_00f'],
    ['Right ankle','_010'],
    ['Right toe','_011'],
    
    ['自定义1','_a30'],
    ['自定义2','_a0d'],
    ['+ElbowAux_L','_a38'],
    ['ElbowAux_L','_a38'],
    ['Left arm','_a0b'],
    ['zHandTwist_L','_a21'],

    ['自定义3','_a20'],
    ['自定义4','__a09'],
    ['+ElbowAux_R','_a28'],
    ['ElbowAux_R','_a28'],
    ['Right arm','_a07'],
    ['zHandTwist_R','_a31'],
 
    ['自定义6','_a32'],
    ['OhButt_L','_a36'],
    ['+KneeAux_L','_a39'],
    ['KneeAux_L','_a39'],
    ['自定义7','_a14'],
    ['自定义8','_a33'],
    
    ['自定义10','_a22'],
    ['OhButt_R','_a26'],
    ['+KneeAux_R','_a29'],
    ['KneeAux_R','_a29'],
    ['自定义11','_a10'],
    ['自定义12','_a23'],
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
        
       

class MMDtoGBFRRename(bpy.types.Operator):
    bl_idname = "tool.mmdtogbfrrename"
    bl_label = "MMD to GBFR"
    bl_options = {'REGISTER', 'UNDO'}
  
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )

    def execute(self, context):
        main(context)
        self.report({'INFO'}, 'conversion completed')
        return {'FINISHED'}
    


