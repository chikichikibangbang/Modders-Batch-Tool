# -*- coding: utf-8 -*-
"""

@author: AsteriskAmpersand
@modify: Korone
"""
import bpy
import bmesh
import re
import random
from collections import OrderedDict

class modTool(bpy.types.Operator):
    addon_key = __package__.split('.')[0]
    #addon = bpy.context.user_preferences.addons[addon_key]    
    def __init__(self):
        self.addon = bpy.context.preferences.addons[self.addon_key]



def getSelection(onlySelection, selectionType = "MESH"):
    return [obj for obj in (bpy.context.selected_objects if onlySelection else bpy.context.scene.objects) 
            if obj.type == selectionType and not obj.hide and not obj.hide_select]
  

    
def detectRepeatedUV(mesh):
    mesh = mesh.data
    uvList = []
    offendingIndices = set()
    for layer in mesh.uv_layers:
        uvMap = {}
        for loop,loopUV in zip(mesh.loops, layer.data):
            uvPoint = (loopUV.uv[0],1-loopUV.uv[1])
            if loop.vertex_index in uvMap and uvMap[loop.vertex_index] != uvPoint:
                offendingIndices.add(loop.vertex_index)
            else:
                uvMap[loop.vertex_index] = uvPoint
        uvList.append(uvMap)
    return offendingIndices

class markUV(modTool):
    bl_idname = 'mod_tools.mark_uv_rep'
    bl_label = "Mark Repeated UVs"
    bl_description = 'Mark repeated UVs with empties.'
    bl_options = {"REGISTER", "PRESET", "UNDO"}    
    limit_application = bpy.props.BoolProperty(
                        name = 'Limit to selected obejcts',
                        description = 'Limit operator actions to current selected objects',
                        default = True
                        )

    def execute(self,context):
        meshes = getSelection(self.limit_application)
        for mesh in meshes:
            repeatedVertices = detectRepeatedUV(mesh)
            for vertIndex in repeatedVertices:
                o = bpy.data.objects.new("YAVP-%s"%mesh.name, None )
                bpy.context.scene.objects.link( o )
                o.location = mesh.matrix_world * mesh.data.vertices[vertIndex].co
                o.show_x_ray = True
                o.empty_draw_size = .5
        return {'FINISHED'}
    
        #col.operator("mod_tools.mark_uv_rep", icon='EDGESEL', text="Mark Repeated UVs")


def solveRepeatedEdge(op,mesh):
    #bpy.context.scene.tool_settings.use_uv_select_sync = True
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.uv.seams_from_islands()
    #
    me = mesh.data    
    bm = bmesh.from_edit_mesh(me)
    for e in bm.edges:
        if e.seam:
            e.select = True    
    bmesh.update_edit_mesh(me)
    bpy.ops.mesh.edge_split()
    bpy.ops.mesh.select_all(action='DESELECT')
    """
    bpy.ops.mesh.select_all(action='DESELECT')
    bm = bmesh.from_edit_mesh(mesh.data)
    oldmode = bm.select_mode
    bm.select_mode = {'FACE'}
    faceGroups = []
    bm.faces.ensure_lookup_table()
    
    bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
    save_sync = bpy.context.scene.tool_settings.use_uv_select_sync
    bpy.context.scene.tool_settings.use_uv_select_sync = True
    faces = set(bm.faces[:])
    while faces:
        bpy.ops.mesh.select_all(action='DESELECT')  
        face = faces.pop() 
        face.select = True
        bpy.ops.uv.select_linked()
        selected_faces = {f for f in faces if f.select}
        selected_faces.add(face) # this or bm.faces above?
        faceGroups.append(selected_faces)
        faces -= selected_faces
    
    bpy.context.scene.tool_settings.use_uv_select_sync = save_sync
    
    for g in faceGroups:
        bpy.ops.mesh.select_all(action='DESELECT')
        for f in g:
            f.select = True
        bpy.ops.mesh.split()
    bpy.ops.mesh.select_all(action='DESELECT')
    bm.select_mode = oldmode
    bm.verts.ensure_lookup_table()
    bm.verts.index_update()
    bmesh.update_edit_mesh(mesh.data) 
    mesh.data.update()    
    return
    """

def bad_iter(blenderCrap):
    i = 0
    while (True):
        try:
            yield(blenderCrap[i])
            i+=1
        except:
            return
            
def selectRepeated(bm):
    bm.verts.index_update()
    bm.verts.ensure_lookup_table()
    targetVert = set()
    for uv_layer in bad_iter(bm.loops.layers.uv):
        uvMap = {}
        for face in bm.faces:
            for loop in face.loops:
                uvPoint = tuple(loop[uv_layer].uv)
                if loop.vert.index in uvMap and uvMap[loop.vert.index] != uvPoint:
                    targetVert.add(bm.verts[loop.vert.index])
                else:
                    uvMap[loop.vert.index] = uvPoint
    return targetVert

def solveRepeatedVertex(op,mesh):
    bpy.ops.mesh.select_all(action='DESELECT')
    bm = bmesh.from_edit_mesh(mesh.data)
    oldmode = bm.select_mode
    bm.select_mode = {'VERT'}    
    targets = selectRepeated(bm)
    for target in targets:
        bmesh.utils.vert_separate(target,target.link_edges)
        bm.verts.ensure_lookup_table()    
    bpy.ops.mesh.select_all(action='DESELECT')
    bm.select_mode = oldmode
    bm.verts.ensure_lookup_table()
    bm.verts.index_update()
    bmesh.update_edit_mesh(mesh.data) 
    mesh.data.update()       
    return

def solveRepeatedUV(op,mesh):
    solveRepeatedEdge(op,mesh)
    solveRepeatedVertex(op,mesh)

def cloneMesh(mesh):
    new_obj = mesh.copy()
    new_obj.data = mesh.data.copy()
    bpy.context.scene.collection.objects.link(new_obj)
    return new_obj

def transferNormals(clone,mesh):
    m = mesh.modifiers.new("Normals Transfer","DATA_TRANSFER")
    m.use_loop_data = True
    m.loop_mapping = "NEAREST_POLYNOR"#"POLYINTERP_NEAREST"#
    m.data_types_loops = {'CUSTOM_NORMAL'}
    m.object = clone
    bpy.ops.object.modifier_apply(modifier = m.name)
    

def deleteClone(clone):
    objs = bpy.data.objects
    objs.remove(objs[clone.name], do_unlink=True)

class solveUV(modTool):
    bl_idname = 'mod_tools.solve_uv_rep'
    bl_label = "Solve repeated UVs"
    #bl_description = 'Fixes the issue with Repeated UVs by Edge Splitting'
    bl_options = {"REGISTER", "PRESET", "UNDO"}    
    limit_application = bpy.props.BoolProperty(
                        name = 'Limit to selected obejcts',
                        description = 'Limit operator actions to current selected objects',
                        default = True
                        )
    smooth_normals = bpy.props.BoolProperty(
                        name = 'Tranfer old normals',
                        description = 'Transfers previous normals',
                        default = True
                        )
    solver = solveRepeatedUV
    
    def execute(self,context):
        old_active = bpy.context.view_layer.objects.active
        meshes = getSelection(self.limit_application)
        for mesh in meshes:
            repeatedVertices = detectRepeatedUV(mesh)
            if repeatedVertices:
                bpy.context.view_layer.objects.active = mesh  
                oldmode = mesh.mode
                bpy.ops.object.mode_set(mode='OBJECT')
                clone = cloneMesh(mesh)
                bpy.context.view_layer.objects.active = mesh  
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.context.scene.tool_settings.use_uv_select_sync = True
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.uv.seams_from_islands()
                self.solver(mesh)
                bpy.ops.object.mode_set(mode='OBJECT')
                
                transferNormals(clone,mesh)
                deleteClone(clone)
                bpy.ops.object.mode_set(mode=oldmode)            
        bpy.context.view_layer.objects.active = old_active
        self.report({'INFO'}, 'splitting completed')
        return {'FINISHED'}
    
        

def solveSharpUV(op,mesh):
    obj = mesh
    me = obj.data
    bpy.ops.mesh.select_all(action='DESELECT')
    bm = bmesh.from_edit_mesh(me)
    for e in bm.edges:
        if not e.smooth:
            e.select = True
    bpy.ops.mesh.edge_split()
    bpy.ops.mesh.select_all(action='DESELECT')
    bmesh.update_edit_mesh(me)   
    return
        
def solveSharpRepeatedUV(op,mesh):
    solveSharpUV(op,mesh)
    solveRepeatedUV(op,mesh)
    
    
class SplitSeamSharp(solveUV):
    bl_idname = 'mod_tools.split_seam_sharp'
    bl_label = "split seam"
    #bl_description = 'Pre-emptively splits Sharp Edges and Repeated Seams preserving shading.'
    bl_options = {'REGISTER', 'UNDO'}

    solver = solveSharpRepeatedUV        
        
    @classmethod
    def poll(cls, context):
        for obj in bpy.context.selected_objects:
            return bool( obj.type == "MESH" ) and bool(bpy.context.object.mode == "OBJECT") 