bl_info = {
    "name": "Modder's Batch Tool",
    "author": "诸葛不太亮, 折戟沉沙丶丿, Dytser, Shotariya",
    "version": (1, 2, 5),
    "blender": (2, 93, 0),
    "location": "View3D > Tool Shelf > Modder's Batch Tool",
    "description": "Utility tools to do a lot of repetitive operations automatically",
    "warning": "",
    "category": "3D View",
}

import bpy
import math
from bpy.props import BoolProperty


#Extra Function
from .modules.separatebymaterials import SeparateByMaterials
from .modules.cleanzerovg import CleanZeroVG
from .modules.normalize_limit_vg import NormalizeLimitVG
from .modules.split_seam import SplitSeamSharp
#MHRise
from .Games.MHRise.ImportMesh import importMHRfmesh, importMHRmmesh
from .Games.MHRise.SnapBones_MMD import SnapBonesMMDtoMHR
from .Games.MHRise.MMDtoMHR import MMDtoMHRRename
from .Games.MHRise.UMAtoMHR import UMAtoMHRRename
from .Games.MHRise.MHWtoMHR import MHWtoMHRRename
from .Games.MHRise.XPStoMHR import XPStoMHRRename
#MHWorld
from .Games.MHWorld.ImportMesh import importMHWorldfmesh, importMHWorldmmesh
from .Games.MHWorld.SnapBones_MMD import SnapBonesMMDtoMHW
from .Games.MHWorld.MMDtoMHW import MMDtoMHWRename
from .Games.MHWorld.UMAtoMHW import UMAtoMHWRename
from .Games.MHWorld.MHRtoMHW import MHRtoMHWRename
from .Games.MHWorld.addemptymesh import AddMHWorldemptymesh

#GranblueFantasyRelink
from .Games.GranblueFantasyRelink.gbfr_tpose import GBFRTPOSE
from .Games.GranblueFantasyRelink.SnapBones_MMD import SnapBonesMMDtoGBFR
from .Games.GranblueFantasyRelink.SnapBones_UMA import SnapBonesUMAtoGBFR
from .Games.GranblueFantasyRelink.MMDtoGBFR import MMDtoGBFRRename
from .Games.GranblueFantasyRelink.UMAtoGBFR import UMAtoGBFRRename

#ResidentEvil4
from .Games.ResidentEvil4.MMDtoRE4 import MMDtoRE4Rename
#DevilMayCry5
from .Games.DMC5.MMDtoDMC5 import MMDtoDMC5Rename

def prefs():
    return bpy.context.preferences.addons[__name__].preferences


class ToolPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    show_mhrise: BoolProperty(
        name="MHRise",
        description="show MHRise panel", default=True)
    show_mhworld: BoolProperty(
        name="MHWorld",
        description="show MHWorld panel", default=False)
    show_re4: BoolProperty(
        name="ResidentEvil4",
        description="show ResidentEvil4 panel", default=False)
    show_dmc5: BoolProperty(
        name="DevilMayCry5",
        description="show DevilMayCry5 panel", default=False)
    show_gbfr: BoolProperty(
        name="GranblueFantasyRelink",
        description="show GranblueFantasyRelink panel", default=False)



class ShowPanel(bpy.types.Panel):
    bl_label = "Show Panel Settings"
    bl_idname = "OBJECT_PT_ShowPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        pr = prefs()
        layout = self.layout
        row = layout.row()
        row.prop(pr, "show_mhrise")
        row = layout.row()
        row.prop(pr, "show_mhworld")
        row = layout.row()
        row.prop(pr, "show_gbfr")
        #row = layout.row()
        #row.prop(pr, "show_re4")
        #row = layout.row()
        #row.prop(pr, "show_dmc5")

from .modules.imagecombiner.ui import main_menu, property_menu

class ExtraFunction(bpy.types.Panel):
    bl_label = "Universal Function"
    bl_idname = "OBJECT_PT_ExtraFunction"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("tool.separatebymaterials",icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("tool.cleanzerovg",icon="OUTLINER_DATA_MESH")
 

class MHRise(bpy.types.Panel):
    bl_label = "MHRise"
    bl_idname = "OBJECT_PT_MHRise"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"
  
    @classmethod
    def poll(self, context):
        pr = prefs()
        return bool(pr.show_mhrise)

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="import MHRise shadow mesh")
        row = layout.row()
        row.operator("tool.importmhrfmesh",icon="OUTLINER_OB_MESH") 
        row.operator("tool.importmhrmmesh",icon="OUTLINER_OB_MESH")    
        
        layout.label(text="batch snap bones (only support tpose)")
        row = layout.row()
        row.scale_y = 1.2
        row.label(text="make sure you select mmd armature first and then the game armature in the object mode", icon="INFO")
        row = layout.row()
        row.operator("tool.snapbonesmmdtomhr",icon="OUTLINER_OB_ARMATURE")
        
        layout.label(text="batch rename vertax groups")
        row = layout.row()
        row.operator("tool.mmdtomhrrename",icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("tool.umatomhrrename",icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("tool.mhwtomhrrename",icon="OUTLINER_DATA_MESH")
        #row = layout.row()
        #row.operator("tool.xpstomhrrename",icon="OUTLINER_DATA_MESH")


class MHWorld(bpy.types.Panel):
    bl_label = "MHWorld"
    bl_idname = "OBJECT_PT_MHWorld"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"

    @classmethod
    def poll(self, context):
        pr = prefs()
        return bool(pr.show_mhworld)

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.scale_y = 1.2
        row.label(text="make sure you have installed <Easier MHW MOD3 Import_Export> plugin", icon="INFO")
        row = layout.row()

        layout.label(text="import MHWorld basic armature")
        row = layout.row()
        row.operator("tool.importmhworldfmesh",icon="OUTLINER_OB_MESH") 
        row.operator("tool.importmhworldmmesh",icon="OUTLINER_OB_MESH") 

        layout.label(text="batch snap bones (only support tpose)")
        row = layout.row()
        row.scale_y = 1.2
        row.label(text="make sure you select mmd armature first and then the game armature in the object mode", icon="INFO")
        row = layout.row()
        row.operator("tool.snapbonesmmdtomhw",icon="OUTLINER_OB_ARMATURE")

        layout.label(text="batch rename vertax groups")
        row = layout.row()
        row.operator("tool.mmdtomhwrename",icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("tool.umatomhwrename",icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("tool.mhrtomhwrename",icon="OUTLINER_DATA_MESH")
        
        layout.label(text="batch normalize and limit meshes by 4wt")
        row = layout.row()
        row.operator("tool.normalizelimitvg",icon="OUTLINER_DATA_MESH")

        layout.label(text="batch split seam")
        row = layout.row()
        row.operator("mod_tools.split_seam_sharp",icon="OUTLINER_DATA_MESH")

        #layout.label(text="batch add empty meshes with properties")
        #row = layout.row()
        #row.operator("tool.addmhworldemptymesh",icon="OUTLINER_OB_MESH")

class GranblueFantasyRelink(bpy.types.Panel):
    bl_label = "GranblueFantasyRelink"
    bl_idname = "OBJECT_PT_GBFR"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"

    @classmethod
    def poll(self, context):
        pr = prefs()
        return bool(pr.show_gbfr)

    def draw(self, context):
        layout = self.layout

        layout.label(text="convert gbfr model to tpose")
        row = layout.row()
        row.operator("tool.gbfrtpose",icon="OUTLINER_OB_ARMATURE")

        layout.label(text="batch snap bones (only support tpose)")
        row = layout.row()
        row.scale_y = 1.2
        row.label(text="make sure you select mmd armature first and then the game armature in the object mode", icon="INFO")
        row = layout.row()
        row.operator("tool.snapbonesmmdtogbfr",icon="OUTLINER_OB_ARMATURE")
        row = layout.row()
        row.operator("tool.snapbonesumatogbfr",icon="OUTLINER_OB_ARMATURE")

        layout.label(text="batch rename vertax groups")
        row = layout.row()
        row.operator("tool.mmdtogbfrrename",icon="OUTLINER_DATA_MESH")
        row = layout.row()
        row.operator("tool.umatogbfrrename",icon="OUTLINER_DATA_MESH")
    
        layout.label(text="batch normalize and limit meshes by 4wt")
        row = layout.row()
        row.operator("tool.normalizelimitvg",icon="OUTLINER_DATA_MESH")

        layout.label(text="batch split seam")
        row = layout.row()
        row.operator("mod_tools.split_seam_sharp",icon="OUTLINER_DATA_MESH")
   
class ResidentEvil4(bpy.types.Panel):
    bl_label = "ResidentEvil4"
    bl_idname = "OBJECT_PT_ResidentEvil4"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"

    @classmethod
    def poll(self, context):
        pr = prefs()
        return bool(pr.show_re4)

    def draw(self, context):
        layout = self.layout
        layout.label(text="batch rename vertax groups")
        row = layout.row()
        row.operator("tool.mmdtore4rename",icon="OUTLINER_DATA_MESH")  

        layout.label(text="batch snap bones(undo)")   

class DevilMayCry5(bpy.types.Panel):
    bl_label = "DevilMayCry5"
    bl_idname = "OBJECT_PT_DevilMayCry5"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Modder's Batch Tool"

    @classmethod
    def poll(self, context):
        pr = prefs()
        return bool(pr.show_dmc5)

    def draw(self, context):
        layout = self.layout
        layout.label(text="batch rename vertax groups")
        row = layout.row()
        row.operator("tool.mmdtodmc5rename",icon="OUTLINER_DATA_MESH")   

        layout.label(text="batch snap bones(undo)")  

classes = (
    ToolPreferences,
    ShowPanel,

    ExtraFunction,
    SeparateByMaterials,
    CleanZeroVG,
    NormalizeLimitVG,
    SplitSeamSharp,

    MHRise,
    importMHRfmesh,
    importMHRmmesh,
    SnapBonesMMDtoMHR,
    MMDtoMHRRename,
    UMAtoMHRRename,
    MHWtoMHRRename,
    XPStoMHRRename,
    
    MHWorld,
    importMHWorldfmesh,
    importMHWorldmmesh,
    SnapBonesMMDtoMHW,
    AddMHWorldemptymesh,
    MMDtoMHWRename,
    UMAtoMHWRename,
    MHRtoMHWRename,

    GranblueFantasyRelink,
    GBFRTPOSE,  
    SnapBonesMMDtoGBFR,
    SnapBonesUMAtoGBFR,
    MMDtoGBFRRename,
    UMAtoGBFRRename,
  

    ResidentEvil4,
    MMDtoRE4Rename,
  
    DevilMayCry5,
    MMDtoDMC5Rename,
    )


#register, unregister = bpy.utils.register_classes_factory(classes)
#print(classes)

from .modules.imagecombiner.registration import __bl_classes,register_all,unregister_all
#print(__bl_classes)
def register():
    for i in range(len(classes)):
        bpy.utils.register_class(classes[i])
    register_all(__bl_classes)
    from .translation import translation_dict
    bpy.app.translations.register(bl_info['name'], translation_dict)
def unregister():
    bpy.app.translations.unregister(bl_info['name'])
    unregister_all(__bl_classes)
    for i in range(len(classes)):
        bpy.utils.unregister_class(classes[i])

if __name__ == "__main__":
    register()

