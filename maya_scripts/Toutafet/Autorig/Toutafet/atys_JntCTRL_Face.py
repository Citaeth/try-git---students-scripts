import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm



#1-Create Joint

cmds.select('LocF*')
shapeList = cmds.ls(sl=True)
loc = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(loc)
cmds.select(clear=True)
for x in range (0, y):
    cmds.select(clear=True)
    jnt=cmds.joint(n='Bind'+loc[x])
    cmds.matchTransform(jnt,loc[x])

cmds.select("Bind_LocF_*")
cmds.makeIdentity( apply=True )
cmds.select(all=True, hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('Bind_LocF_', 'Bind_'))

cmds.select(clear=True)



#2-Hierarchy
cmds.createNode('transform',n ='Joint_Face')
cmds.parent('Bind_Nostril_End_L','Bind_Nostril_01_L')
cmds.parent('Bind_Nostril_End_R','Bind_Nostril_01_R')
cmds.parent('Bind_Nose_Tip', 'Bind_Nose_Base')
cmds.parent('Bind_Ear_End_L', 'Bind_Ear_01_L')
cmds.parent('Bind_Ear_End_R', 'Bind_Ear_01_R')
cmds.parent('Bind_Jaw_Down_End','Bind_Jaw_Down_01')
cmds.parent('Bind_Jaw_Down_01','Bind_Head_Pivot_02')
cmds.parent('Bind_Head_Pivot_02','Bind_Head_Pivot_01')
cmds.parent('Bind_Neck_End','Bind_Neck_01')
cmds.parent('Bind_Head_Pivot_01', 'Joint_Face')
cmds.parent('Bind_Jaw_Up_End', 'Bind_Jaw_Up_01')
cmds.parent('Bind_Jaw_Up_01','Bind_Head_Pivot_02')
cmds.parent('Bind_Nose_Base', 'Bind_Jaw_Up_01')



#3-Orient Joint

#Orient Neck

cmds.joint("Bind_Neck_01" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Neck_End" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Neck_01" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Neck_End" ,e=True,zso=True,oj="none")

#Orient Head Pivot to Jaw Down

cmds.joint("Bind_Head_Pivot_01" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Head_Pivot_02" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Jaw_Down_01" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Jaw_Down_End" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Head_Pivot_01" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Head_Pivot_02" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Jaw_Down_01" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Jaw_Down_End" ,e=True,zso=True,oj="none")

#Orient Jaw Up

cmds.joint("Bind_Jaw_Up_01" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Jaw_Up_End" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Jaw_Up_01" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Jaw_Up_End" ,e=True,zso=True,oj="none")

#Orient Ear L

cmds.joint("Bind_Ear_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ear_End_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Ear_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ear_End_L" ,e=True,zso=True,oj="none")

#Orient Ear R

cmds.joint("Bind_Ear_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ear_End_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Ear_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ear_End_R" ,e=True,zso=True,oj="none")

#Orient Nose

cmds.joint("Bind_Nose_Base" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Nose_Tip" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Nose_Base" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Nose_Tip" ,e=True,zso=True,oj="none")

#Orient Nostril_L

cmds.joint("Bind_Nostril_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Nostril_End_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Nostril_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Nostril_End_L" ,e=True,zso=True,oj="none")

#Orient Nostril_R

cmds.joint("Bind_Nostril_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Nostril_End_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Nostril_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Nostril_End_R" ,e=True,zso=True,oj="none")

cmds.parent('Bind_Nostril_01_L', 'Bind_Nose_Base')
cmds.parent('Bind_Nostril_01_R', 'Bind_Nose_Base')
cmds.parent('Bind_Ear_01_L', 'Bind_Jaw_Up_01')
cmds.parent('Bind_Ear_01_R', 'Bind_Jaw_Up_01')


#3-Create controleurs and match position and orientation

cmds.select("Bind_Head_Pivot_01",hi=True)
cmds.select("*_End*", deselect=True)
cmds.select("Bind_Neck_01", add=True)
face = cmds.ls(sl=True)
x=0
y=len(face)
cmds.select(clear=True)
for x in range (0, y):
    ctrlf=cmds.circle(r=1, n="CTRLf_"+face[x])
    cmds.matchTransform(ctrlf,face[x])

cmds.select("CTRLf*")
shapeList = cmds.ls(sl=True)
ctrlf = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(ctrlf)
cmds.select(clear=True)
for x in range (0, y):
    cmds.createNode('transform',n ='Offset1')
    grp1 = ['Offset1']
    offset1 = cmds.ls(sl=True)
    cmds.matchTransform(offset1, ctrlf[x])
    cmds.parent(ctrlf[x], grp1)
    cmds.rename('Offset1', ctrlf[x]+"_Offset")

cmds.select("CTRLf*",hi=True)
cmds.select("*_Offset*", deselect=True)
shapeList = cmds.ls(sl=True)
ctrlf = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(ctrlf)
cmds.select(clear=True)

cmds.select("CTRLf*",hi=True)
cmds.select("*_Offset*", deselect=True)
shapeList = cmds.ls(sl=True)
ctrlf = cmds.listRelatives(shapeList, fullPath=False)
x=0
y=len(ctrlf)
for x in range (0, y):
    cmds.createNode('transform',n ='Master1')
    grp1 = ['Master1']
    Master1 = cmds.ls(sl=True)
    cmds.matchTransform(Master1, ctrlf[x])
    cmds.parent(Master1, ctrlf[x])
    cmds.rename('Master1', ctrlf[x]+"_Master")
    
cmds.select(all=True,hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('CTRLf_Bind_', 'CTRL_'))
    item.rename(item.name().replace('Shape_Master', '_Master'))
    item.rename(item.name().replace('CTRL_Jaw_Up_01', 'CTRL_Crane'))
    item.rename(item.name().replace('CTRL_Neck_01', 'CTRL_Neck'))
cmds.select(clear=True)



#4-Hierarchy

cmds.parent("CTRL_Head_Pivot_02_Offset", 'CTRL_Head_Pivot_01_Master')
cmds.parent("CTRL_Crane_Offset", 'CTRL_Head_Pivot_01_Master')
cmds.parent("CTRL_Jaw_Down_01_Offset", 'CTRL_Head_Pivot_01_Master')
cmds.parent("CTRL_Nose_Base_Offset", "CTRL_Crane_Master")
cmds.parent("CTRL_Nose_Tip_Offset", "CTRL_Nose_Base_Master")
cmds.parent("CTRL_Nostril_01_L_Offset", "CTRL_Nose_Base_Master")
cmds.parent("CTRL_Nostril_01_R_Offset", "CTRL_Nose_Base_Master")
cmds.parent("CTRL_Ear_01_R_Offset", "CTRL_Crane_Master")
cmds.parent("CTRL_Ear_01_L_Offset", "CTRL_Crane_Master")
cmds.parent("CTRL_Head_Pivot_01_Offset", "Ctrl_01")
cmds.parent("CTRL_Neck_Offset", "Ctrl_01")
cmds.parent("Joint_Face", "Joint_01")
cmds.parent('Bind_Neck_01', 'Bind_Spine_06')

cmds.select(clear=True)
cmds.select('LocF*')
cmds.group(n="Locators_Face")
cmds.parent('Locators_Face', 'Locators_Place')
cmds.select(all=True, hi=True)
for item in pm.selected():
    item.rename(item.name().replace('LocF_', 'Loc_Pl_'))

cmds.select(clear=True)



#5-Because I totally forgot

cmds.parentConstraint('CTRL_Jaw_Down_01_Master', 'Bind_Jaw_Down_01')
cmds.parentConstraint('CTRL_Ear_01_L_Master', 'Bind_Ear_01_L')
cmds.parentConstraint('CTRL_Ear_01_R_Master', 'Bind_Ear_01_R')
cmds.parentConstraint('CTRL_Nostril_01_L_Master', 'Bind_Nostril_01_L')
cmds.parentConstraint('CTRL_Nostril_01_R_Master', 'Bind_Nostril_01_R')
cmds.parentConstraint('CTRL_Nose_Tip_Master', 'Bind_Nose_Tip')
cmds.parentConstraint('CTRL_Nose_Base_Master', 'Bind_Nose_Base')
cmds.parentConstraint('CTRL_Crane_Master', 'Bind_Jaw_Up_01')
cmds.parentConstraint('CTRL_Head_Pivot_02_Master', 'Bind_Head_Pivot_02')
cmds.parentConstraint('CTRL_Head_Pivot_01_Master', 'Bind_Head_Pivot_01')
cmds.parentConstraint('CTRL_Neck', 'Bind_Neck_01')





