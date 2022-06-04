import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math

def locHead (*args):
    cmds.spaceLocator(n='LocF_Neck_01')
    cmds.spaceLocator(n='LocF_Neck_End')
    cmds.spaceLocator(n='LocF_Neck_Pivot_01')
    cmds.spaceLocator(n='LocF_Neck_Pivot_02')
    cmds.spaceLocator(n='LocF_Jaw_Up_01')
    cmds.spaceLocator(n='LocF_Jaw_Up_End')
    cmds.spaceLocator(n='LocF_Jaw_Down_01')
    cmds.spaceLocator(n='LocF_Jaw_Down_End')
    cmds.spaceLocator(n='LocF_Nose_Base')
    cmds.spaceLocator(n='LocF_Nose_Tip')
    cmds.spaceLocator(n='LocF_Nostril_01_L')
    cmds.spaceLocator(n='LocF_Nostril_End_L')
    cmds.spaceLocator(n='LocF_Ear_01_L')
    cmds.spaceLocator(n='LocF_Ear_End_L')

    
#window___________________________________________________________________________________________________________
    
	
window= cmds.window( t="Scene Set-up",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 125) )
mainw = cmds.formLayout()

cmds.columnLayout()
nm = cmds.frameLayout( label='Locator Head', labelAlign='center')
cmds.button(l='Create Locators', align='center', c=locHead)

cmds.showWindow(window)