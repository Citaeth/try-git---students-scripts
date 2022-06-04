import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math

def createloc(*args):

    radc = cmds.radioCollection(rc, q = True, sl= True)
    
    if radc == 'right' :
        side = '_R'
    if radc == 'left' :
        side = '_L'

    cmds.spaceLocator(n='LocH_Hand'+side)
    cmds.spaceLocator(n='LocH_Clamp'+side)
    cmds.spaceLocator(n='LocH_Palm'+side)

    cmds.spaceLocator(n='LocH_Thumb_01'+side)
    cmds.spaceLocator(n='LocH_Thumb_02'+side)
    cmds.spaceLocator(n='LocH_Thumb_03'+side)
    cmds.spaceLocator(n='LocH_Thumb_04'+side)

    cmds.spaceLocator(n='LocH_Index_01')
    cmds.spaceLocator(n='LocH_Index_02'+side)
    cmds.spaceLocator(n='LocH_Index_03'+side)
    cmds.spaceLocator(n='LocH_Index_04'+side)

    cmds.spaceLocator(n='LocH_Middle_01'+side)
    cmds.spaceLocator(n='LocH_Middle_02'+side)
    cmds.spaceLocator(n='LocH_Middle_03'+side)
    cmds.spaceLocator(n='LocH_Middle_04'+side)

    cmds.spaceLocator(n='LocH_Ring_01'+side)
    cmds.spaceLocator(n='LocH_Ring_02'+side)
    cmds.spaceLocator(n='LocH_Ring_03'+side)
    cmds.spaceLocator(n='LocH_Ring_04'+side)

    cmds.spaceLocator(n='LocH_Pinky_01'+side)
    cmds.spaceLocator(n='LocH_Pinky_02'+side)
    cmds.spaceLocator(n='LocH_Pinky_03'+side)
    cmds.spaceLocator(n='LocH_Pinky_04'+side)
    
#window___________________________________________________________________________________________________________
    
	
window= cmds.window( t="Scene Set-up",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 125) )
mainw = cmds.formLayout()
nm = cmds.frameLayout( label='Select Side', labelAlign='center')
cmds.rowColumnLayout( p = nm, numberOfColumns=2, columnWidth=[(1, 125), (2, 125)] )

rc = cmds.radioCollection()
r = cmds.radioButton("right", label='Right', align='left' )
l = cmds.radioButton('left', label='Left', align='right' )
eylup = cmds.frameLayout( p= nm, label="Create Locators", labelAlign='center' )
cmds.button(l='Allons-y, Lets go !', align='center', c=createloc)

cmds.showWindow(window)