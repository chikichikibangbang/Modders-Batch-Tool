# 本脚本用于在blender侧边工具栏添加一个分页按钮，一键修改MMD模型的顶点组名称以匹配MHR的骨骼名（不包含物理骨骼）。
# 由于各种MMD模型的顶点组名称不尽相同，权重分布也不尽相同，所以该脚本可以根据不同情况自行修改。例如将下方的“胸２.L”修改为“胸上2.L”，或者修改“自定义x”的名称来添加旋转骨骼和辅助骨骼的识别。
# 像腕捩.L、手捩.L、腕捩.R、手捩.R以及面部肌肉的顶点组，请自行安排方案，或者配合CATS插件的子级骨骼合并功能使用。

import bpy


def main(context):
    name_list = [
    ['下半身','Waist_00'],
    ['上半身','Spine_00'],
    ['上半身2','Spine_01'],
    ['首','Neck_00'],
    ['頭','Head_00'],

    ['胸２.L','L_Oupai_00'],
    ['胸２.R','R_Oupai_00'],
    
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
    ['自定义2','L_Arm_01_W'],
    ['自定义3','L_Arm_01_T'],
    ['自定义4','L_Arm_02_T'],

    ['自定义5','R_Arm_00_W'],
    ['自定义6','R_Arm_01_W'],
    ['自定义7','R_Arm_01_T'],
    ['自定义8','R_Arm_02_T'],

    ['自定义9','L_Leg_00_W'],
    ['自定义10','L_Leg_01_W'],
    ['自定义11','L_Leg_02_T'],
    
    ['自定义12','R_Leg_00_W'],
    ['自定义13','R_Leg_01_W'],
    ['自定义14','R_Leg_02_T'],
    ]
    
    for obj in bpy.context.selected_objects:
        v_groups = obj.vertex_groups
        for n in name_list:
            if n[0] in v_groups:
                v_groups[n[0]].name = n[1]
        
       

class MMDtoDMC5Rename(bpy.types.Operator):
    bl_idname = "tool.mmdtodmc5rename"
    bl_label = "MMD to DMC5(undo)"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" )

    def execute(self, context):
        main(context)
        return {'FINISHED'}
    


