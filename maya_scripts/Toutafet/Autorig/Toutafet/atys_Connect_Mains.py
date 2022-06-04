import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm


#1 - Connect Fingers L

#Index

cmds.connectAttr('CTRL_Index_01_L.rotateX', 'Bind_Index_01_L.rotateX')
cmds.connectAttr('CTRL_Index_01_L.rotateY', 'Bind_Index_01_L.rotateY')
cmds.connectAttr('CTRL_Index_01_L.rotateZ', 'Bind_Index_01_L.rotateZ')

cmds.connectAttr('CTRL_Index_02_L.rotateX', 'Bind_Index_02_L.rotateX')
cmds.connectAttr('CTRL_Index_02_L.rotateY', 'Bind_Index_02_L.rotateY')
cmds.connectAttr('CTRL_Index_02_L.rotateZ', 'Bind_Index_02_L.rotateZ')

cmds.connectAttr('CTRL_Index_03_L.rotateX', 'Bind_Index_03_L.rotateX')
cmds.connectAttr('CTRL_Index_03_L.rotateY', 'Bind_Index_03_L.rotateY')
cmds.connectAttr('CTRL_Index_03_L.rotateZ', 'Bind_Index_03_L.rotateZ')

cmds.delete("CTRL_Index_04_L_Offset")


#Middle

cmds.connectAttr('CTRL_Middle_01_L.rotateX', 'Bind_Middle_01_L.rotateX')
cmds.connectAttr('CTRL_Middle_01_L.rotateY', 'Bind_Middle_01_L.rotateY')
cmds.connectAttr('CTRL_Middle_01_L.rotateZ', 'Bind_Middle_01_L.rotateZ')

cmds.connectAttr('CTRL_Middle_02_L.rotateX', 'Bind_Middle_02_L.rotateX')
cmds.connectAttr('CTRL_Middle_02_L.rotateY', 'Bind_Middle_02_L.rotateY')
cmds.connectAttr('CTRL_Middle_02_L.rotateZ', 'Bind_Middle_02_L.rotateZ')

cmds.connectAttr('CTRL_Middle_03_L.rotateX', 'Bind_Middle_03_L.rotateX')
cmds.connectAttr('CTRL_Middle_03_L.rotateY', 'Bind_Middle_03_L.rotateY')
cmds.connectAttr('CTRL_Middle_03_L.rotateZ', 'Bind_Middle_03_L.rotateZ')

cmds.delete("CTRL_Middle_04_L_Offset")


#Ring

cmds.connectAttr('CTRL_Ring_01_L.rotateX', 'Bind_Ring_01_L.rotateX')
cmds.connectAttr('CTRL_Ring_01_L.rotateY', 'Bind_Ring_01_L.rotateY')
cmds.connectAttr('CTRL_Ring_01_L.rotateZ', 'Bind_Ring_01_L.rotateZ')

cmds.connectAttr('CTRL_Ring_02_L.rotateX', 'Bind_Ring_02_L.rotateX')
cmds.connectAttr('CTRL_Ring_02_L.rotateY', 'Bind_Ring_02_L.rotateY')
cmds.connectAttr('CTRL_Ring_02_L.rotateZ', 'Bind_Ring_02_L.rotateZ')

cmds.connectAttr('CTRL_Ring_03_L.rotateX', 'Bind_Ring_03_L.rotateX')
cmds.connectAttr('CTRL_Ring_03_L.rotateY', 'Bind_Ring_03_L.rotateY')
cmds.connectAttr('CTRL_Ring_03_L.rotateZ', 'Bind_Ring_03_L.rotateZ')

cmds.delete("CTRL_Ring_04_L_Offset")


#Pinky

cmds.connectAttr('CTRL_Pinky_01_L.rotateX', 'Bind_Pinky_01_L.rotateX')
cmds.connectAttr('CTRL_Pinky_01_L.rotateY', 'Bind_Pinky_01_L.rotateY')
cmds.connectAttr('CTRL_Pinky_01_L.rotateZ', 'Bind_Pinky_01_L.rotateZ')

cmds.connectAttr('CTRL_Pinky_02_L.rotateX', 'Bind_Pinky_02_L.rotateX')
cmds.connectAttr('CTRL_Pinky_02_L.rotateY', 'Bind_Pinky_02_L.rotateY')
cmds.connectAttr('CTRL_Pinky_02_L.rotateZ', 'Bind_Pinky_02_L.rotateZ')

cmds.connectAttr('CTRL_Pinky_03_L.rotateX', 'Bind_Pinky_03_L.rotateX')
cmds.connectAttr('CTRL_Pinky_03_L.rotateY', 'Bind_Pinky_03_L.rotateY')
cmds.connectAttr('CTRL_Pinky_03_L.rotateZ', 'Bind_Pinky_03_L.rotateZ')

cmds.delete("CTRL_Pinky_04_L_Offset")


#Thumb

cmds.connectAttr('CTRL_Thumb_01_L.rotateX', 'Bind_Thumb_01_L.rotateX')
cmds.connectAttr('CTRL_Thumb_01_L.rotateY', 'Bind_Thumb_01_L.rotateY')
cmds.connectAttr('CTRL_Thumb_01_L.rotateZ', 'Bind_Thumb_01_L.rotateZ')

cmds.connectAttr('CTRL_Thumb_02_L.rotateX', 'Bind_Thumb_02_L.rotateX')
cmds.connectAttr('CTRL_Thumb_02_L.rotateY', 'Bind_Thumb_02_L.rotateY')
cmds.connectAttr('CTRL_Thumb_02_L.rotateZ', 'Bind_Thumb_02_L.rotateZ')

cmds.connectAttr('CTRL_Thumb_03_L.rotateX', 'Bind_Thumb_03_L.rotateX')
cmds.connectAttr('CTRL_Thumb_03_L.rotateY', 'Bind_Thumb_03_L.rotateY')
cmds.connectAttr('CTRL_Thumb_03_L.rotateZ', 'Bind_Thumb_03_L.rotateZ')

cmds.delete("CTRL_Thumb_04_L_Offset")



#1 - Connect Fingers R

#Index

cmds.connectAttr('CTRL_Index_01_R.rotateX', 'Bind_Index_01_R.rotateX')
cmds.connectAttr('CTRL_Index_01_R.rotateY', 'Bind_Index_01_R.rotateY')
cmds.connectAttr('CTRL_Index_01_R.rotateZ', 'Bind_Index_01_R.rotateZ')

cmds.connectAttr('CTRL_Index_02_R.rotateX', 'Bind_Index_02_R.rotateX')
cmds.connectAttr('CTRL_Index_02_R.rotateY', 'Bind_Index_02_R.rotateY')
cmds.connectAttr('CTRL_Index_02_R.rotateZ', 'Bind_Index_02_R.rotateZ')

cmds.connectAttr('CTRL_Index_03_R.rotateX', 'Bind_Index_03_R.rotateX')
cmds.connectAttr('CTRL_Index_03_R.rotateY', 'Bind_Index_03_R.rotateY')
cmds.connectAttr('CTRL_Index_03_R.rotateZ', 'Bind_Index_03_R.rotateZ')

cmds.delete("CTRL_Index_04_R_Offset")


#Middle

cmds.connectAttr('CTRL_Middle_01_R.rotateX', 'Bind_Middle_01_R.rotateX')
cmds.connectAttr('CTRL_Middle_01_R.rotateY', 'Bind_Middle_01_R.rotateY')
cmds.connectAttr('CTRL_Middle_01_R.rotateZ', 'Bind_Middle_01_R.rotateZ')

cmds.connectAttr('CTRL_Middle_02_R.rotateX', 'Bind_Middle_02_R.rotateX')
cmds.connectAttr('CTRL_Middle_02_R.rotateY', 'Bind_Middle_02_R.rotateY')
cmds.connectAttr('CTRL_Middle_02_R.rotateZ', 'Bind_Middle_02_R.rotateZ')

cmds.connectAttr('CTRL_Middle_03_R.rotateX', 'Bind_Middle_03_R.rotateX')
cmds.connectAttr('CTRL_Middle_03_R.rotateY', 'Bind_Middle_03_R.rotateY')
cmds.connectAttr('CTRL_Middle_03_R.rotateZ', 'Bind_Middle_03_R.rotateZ')

cmds.delete("CTRL_Middle_04_R_Offset")


#Ring

cmds.connectAttr('CTRL_Ring_01_R.rotateX', 'Bind_Ring_01_R.rotateX')
cmds.connectAttr('CTRL_Ring_01_R.rotateY', 'Bind_Ring_01_R.rotateY')
cmds.connectAttr('CTRL_Ring_01_R.rotateZ', 'Bind_Ring_01_R.rotateZ')

cmds.connectAttr('CTRL_Ring_02_R.rotateX', 'Bind_Ring_02_R.rotateX')
cmds.connectAttr('CTRL_Ring_02_R.rotateY', 'Bind_Ring_02_R.rotateY')
cmds.connectAttr('CTRL_Ring_02_R.rotateZ', 'Bind_Ring_02_R.rotateZ')

cmds.connectAttr('CTRL_Ring_03_R.rotateX', 'Bind_Ring_03_R.rotateX')
cmds.connectAttr('CTRL_Ring_03_R.rotateY', 'Bind_Ring_03_R.rotateY')
cmds.connectAttr('CTRL_Ring_03_R.rotateZ', 'Bind_Ring_03_R.rotateZ')

cmds.delete("CTRL_Ring_04_R_Offset")


#Pinky

cmds.connectAttr('CTRL_Pinky_01_R.rotateX', 'Bind_Pinky_01_R.rotateX')
cmds.connectAttr('CTRL_Pinky_01_R.rotateY', 'Bind_Pinky_01_R.rotateY')
cmds.connectAttr('CTRL_Pinky_01_R.rotateZ', 'Bind_Pinky_01_R.rotateZ')

cmds.connectAttr('CTRL_Pinky_02_R.rotateX', 'Bind_Pinky_02_R.rotateX')
cmds.connectAttr('CTRL_Pinky_02_R.rotateY', 'Bind_Pinky_02_R.rotateY')
cmds.connectAttr('CTRL_Pinky_02_R.rotateZ', 'Bind_Pinky_02_R.rotateZ')

cmds.connectAttr('CTRL_Pinky_03_R.rotateX', 'Bind_Pinky_03_R.rotateX')
cmds.connectAttr('CTRL_Pinky_03_R.rotateY', 'Bind_Pinky_03_R.rotateY')
cmds.connectAttr('CTRL_Pinky_03_R.rotateZ', 'Bind_Pinky_03_R.rotateZ')

cmds.delete("CTRL_Pinky_04_R_Offset")


#Thumb

cmds.connectAttr('CTRL_Thumb_01_R.rotateX', 'Bind_Thumb_01_R.rotateX')
cmds.connectAttr('CTRL_Thumb_01_R.rotateY', 'Bind_Thumb_01_R.rotateY')
cmds.connectAttr('CTRL_Thumb_01_R.rotateZ', 'Bind_Thumb_01_R.rotateZ')

cmds.connectAttr('CTRL_Thumb_02_R.rotateX', 'Bind_Thumb_02_R.rotateX')
cmds.connectAttr('CTRL_Thumb_02_R.rotateY', 'Bind_Thumb_02_R.rotateY')
cmds.connectAttr('CTRL_Thumb_02_R.rotateZ', 'Bind_Thumb_02_R.rotateZ')

cmds.connectAttr('CTRL_Thumb_03_R.rotateX', 'Bind_Thumb_03_R.rotateX')
cmds.connectAttr('CTRL_Thumb_03_R.rotateY', 'Bind_Thumb_03_R.rotateY')
cmds.connectAttr('CTRL_Thumb_03_R.rotateZ', 'Bind_Thumb_03_R.rotateZ')

cmds.delete("CTRL_Thumb_04_R_Offset")