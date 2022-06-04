import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm

"""
________________________________________________________________________________________________________________________________________
Pour Babouche

Script by Juliette Gueydan

Et le rangement alors ?!
  
________________________________________________________________________________________________________________________________________
"""


#Scene_Set_Up
def setup(*args):

    name = cmds.textField(textFieldEntry, editable = True, q = True, text=True, w = 249)
    cmds.createNode('transform',n="GlobalMove_01")
    cmds.createNode('transform',n="Ctrl_01")
    cmds.createNode('transform',n="Joint_01")
    cmds.createNode('transform',n="IKs_01")
    cmds.createNode('transform',n="ExtraNodes_01")
    cmds.createNode('transform',n="ExtraNodes_To_Show")
    cmds.createNode('transform',n="ExtraNodes_To_Hide")
    cmds.createNode('transform',n="Locators_Place")
    cmds.createNode('transform',n="Mesh_01")
    cmds.parent("ExtraNodes_To_Show","ExtraNodes_01")
    cmds.parent("ExtraNodes_To_Hide","ExtraNodes_01")
    cmds.parent("Ctrl_01","GlobalMove_01")
    cmds.parent("Joint_01","GlobalMove_01")
    cmds.parent("IKs_01","GlobalMove_01")
    cmds.parent("Locators_Place", "ExtraNodes_To_Hide")
    cmds.createNode('transform',n=name)
    cmds.parent("GlobalMove_01",name)
    cmds.parent("ExtraNodes_01",name)
    cmds.parent("Mesh_01",name)

#Finish



#window___________________________________________________________________________________________________________
    
	
window= cmds.window( t="Scene Set-up",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 193) )
mainw = cmds.formLayout()
nm = cmds.frameLayout( label='Name Character', labelAlign='center')
cmds.columnLayout()
textFieldEntry = cmds.textField(w = 248, editable = True)
cmds.button(l='Allons-y, Lets go !', align='center', c=setup)

cmds.showWindow(window)