import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm



#1-Create Joint

cmds.select('LocH*')
shapeList = cmds.ls(sl=True)
loc = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(loc)
cmds.select(clear=True)
for x in range (0, y):
    cmds.select(clear=True)
    jnt=cmds.joint(n='Bind'+loc[x])
    cmds.matchTransform(jnt,loc[x])
 
cmds.select("Bind_LocH*")
cmds.makeIdentity( apply=True)   
cmds.select(all=True)  
for item in pm.selected():
    item.rename(item.name().replace('Bind_LocH_', 'Bind_'))




#2-Hierarchy

cmds.parent('Bind_Palm_L','Bind_Hand_L')
cmds.parent('Bind_Thumb_04_L','Bind_Thumb_03_L')
cmds.parent('Bind_Thumb_03_L','Bind_Thumb_02_L')
cmds.parent('Bind_Thumb_02_L','Bind_Thumb_01_L')
cmds.parent('Bind_Thumb_01_L','Bind_Hand_L')
cmds.parent('Bind_Ring_04_L','Bind_Ring_03_L')
cmds.parent('Bind_Ring_03_L','Bind_Ring_02_L')
cmds.parent('Bind_Ring_02_L','Bind_Ring_01_L')
cmds.parent('Bind_Ring_01_L','Bind_Palm_L')
cmds.parent('Bind_Middle_04_L','Bind_Middle_03_L')
cmds.parent('Bind_Middle_03_L','Bind_Middle_02_L')
cmds.parent('Bind_Middle_02_L','Bind_Middle_01_L')
cmds.parent('Bind_Middle_01_L','Bind_Palm_L')
cmds.parent('Bind_Index_04_L','Bind_Index_03_L')
cmds.parent('Bind_Index_03_L','Bind_Index_02_L')
cmds.parent('Bind_Index_02_L','Bind_Index_01_L')
cmds.parent('Bind_Index_01_L','Bind_Palm_L')
cmds.parent('Bind_Pinky_04_L','Bind_Pinky_03_L')
cmds.parent('Bind_Pinky_03_L','Bind_Pinky_02_L')
cmds.parent('Bind_Pinky_02_L','Bind_Pinky_01_L')
cmds.parent('Bind_Pinky_01_L','Bind_Clamp_L')
cmds.parent('Bind_Clamp_L','Bind_Hand_L')


cmds.parent('Bind_Palm_R','Bind_Hand_R')
cmds.parent('Bind_Thumb_04_R','Bind_Thumb_03_R')
cmds.parent('Bind_Thumb_03_R','Bind_Thumb_02_R')
cmds.parent('Bind_Thumb_02_R','Bind_Thumb_01_R')
cmds.parent('Bind_Thumb_01_R','Bind_Hand_R')
cmds.parent('Bind_Ring_04_R','Bind_Ring_03_R')
cmds.parent('Bind_Ring_03_R','Bind_Ring_02_R')
cmds.parent('Bind_Ring_02_R','Bind_Ring_01_R')
cmds.parent('Bind_Ring_01_R','Bind_Palm_R')
cmds.parent('Bind_Middle_04_R','Bind_Middle_03_R')
cmds.parent('Bind_Middle_03_R','Bind_Middle_02_R')
cmds.parent('Bind_Middle_02_R','Bind_Middle_01_R')
cmds.parent('Bind_Middle_01_R','Bind_Palm_R')
cmds.parent('Bind_Index_04_R','Bind_Index_03_R')
cmds.parent('Bind_Index_03_R','Bind_Index_02_R')
cmds.parent('Bind_Index_02_R','Bind_Index_01_R')
cmds.parent('Bind_Index_01_R','Bind_Palm_R')
cmds.parent('Bind_Pinky_04_R','Bind_Pinky_03_R')
cmds.parent('Bind_Pinky_03_R','Bind_Pinky_02_R')
cmds.parent('Bind_Pinky_02_R','Bind_Pinky_01_R')
cmds.parent('Bind_Pinky_01_R','Bind_Clamp_R')
cmds.parent('Bind_Clamp_R','Bind_Hand_R')


#3-Orient Joint

#Orient Joint Pinky

cmds.joint("Bind_Pinky_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Pinky_02_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Pinky_03_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Pinky_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Pinky_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Pinky_02_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Pinky_03_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Pinky_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Pinky_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Pinky_02_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Pinky_03_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Pinky_04_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Pinky_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Pinky_02_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Pinky_03_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Pinky_04_R" ,e=True,zso=True,oj="none")

#Orient Joint Index

cmds.joint("Bind_Index_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Index_02_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Index_03_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Index_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Index_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Index_02_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Index_03_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Index_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Index_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Index_02_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Index_03_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Index_04_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Index_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Index_02_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Index_03_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Index_04_R" ,e=True,zso=True,oj="none")

#Orient Joint Middle

cmds.joint("Bind_Middle_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Middle_02_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Middle_03_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Middle_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Middle_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Middle_02_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Middle_03_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Middle_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Middle_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Middle_02_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Middle_03_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Middle_04_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Middle_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Middle_02_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Middle_03_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Middle_04_R" ,e=True,zso=True,oj="none")

#Orient Joint Ring

cmds.joint("Bind_Ring_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ring_02_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ring_03_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ring_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Ring_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ring_02_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ring_03_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ring_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Ring_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ring_02_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ring_03_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ring_04_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Ring_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ring_02_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ring_03_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Ring_04_R" ,e=True,zso=True,oj="none")

#Orient Joint Thumb

cmds.joint("Bind_Thumb_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Thumb_02_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Thumb_03_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Thumb_04_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Thumb_01_L" ,e=True,zso=True,oj="xyz", sao="zup")
cmds.joint("Bind_Thumb_02_L" ,e=True,zso=True,oj="xyz", sao="zup")
cmds.joint("Bind_Thumb_03_L" ,e=True,zso=True,oj="xyz", sao="zup")
cmds.joint("Bind_Thumb_04_L" ,e=True,zso=True,oj="none", sao="zup")

cmds.joint("Bind_Thumb_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Thumb_02_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Thumb_03_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Thumb_04_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Thumb_01_R" ,e=True,zso=True,oj="xyz", sao="zup")
cmds.joint("Bind_Thumb_02_R" ,e=True,zso=True,oj="xyz", sao="zup")
cmds.joint("Bind_Thumb_03_R" ,e=True,zso=True,oj="xyz", sao="zup")
cmds.joint("Bind_Thumb_04_R" ,e=True,zso=True,oj="none", sao="zup")

#Orient Joint Hand

cmds.joint("Bind_Hand_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Palm_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Clamp_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Hand_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Palm_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Clamp_L" ,e=True,zso=True,oj="xyz", sao="yup")

cmds.joint("Bind_Hand_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Palm_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Clamp_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Hand_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Palm_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Clamp_R" ,e=True,zso=True,oj="xyz", sao="yup")



#4-Create offset

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Hand_L")
cmds.parent("Bind_Hand_L", grp1)
cmds.rename('Offset1', 'Bind_Hand_L_Offset')

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Hand_R")
cmds.parent("Bind_Hand_R", grp1)
cmds.rename('Offset1', 'Bind_Hand_R_Offset')



#5-Create controleurs and match position and orientation

cmds.select("Bind_Hand_L",hi=True)
hand = cmds.ls(sl=True)
x=0
y=len(hand)
cmds.select(clear=True)
for x in range (0, y):
    ctrlh=cmds.circle(r=0.25, n="CTRLh_"+hand[x])
    cmds.matchTransform(ctrlh,hand[x])

cmds.select("Bind_Hand_R",hi=True)
hand = cmds.ls(sl=True)
x=0
y=len(hand)
cmds.select(clear=True)
for x in range (0, y):
    ctrlh=cmds.circle(r=0.5, n="CTRLh_"+hand[x])
    cmds.matchTransform(ctrlh,hand[x])
    
cmds.select("CTRLh*")
shapeList = cmds.ls(sl=True)
ctrlh = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(ctrlh)
cmds.select(clear=True)

for x in range (0, y):
    cmds.createNode('transform',n ='Offset1')
    grp1 = ['Offset1']
    offset1 = cmds.ls(sl=True)
    cmds.matchTransform(offset1, ctrlh[x])
    cmds.parent(ctrlh[x], grp1)
    cmds.rename('Offset1', ctrlh[x]+"_Offset")

cmds.select("CTRLh_Bind_Hand_L_Offset|CTRLh_Bind_Hand_L", "CTRLh_Bind_Palm_L_Offset|CTRLh_Bind_Palm_L", "CTRLh_Bind_Ring_01_L_Offset|CTRLh_Bind_Ring_01_L", "CTRLh_Bind_Ring_02_L_Offset|CTRLh_Bind_Ring_02_L", "CTRLh_Bind_Ring_03_L_Offset|CTRLh_Bind_Ring_03_L", "CTRLh_Bind_Ring_04_L_Offset|CTRLh_Bind_Ring_04_L", "CTRLh_Bind_Middle_01_L_Offset|CTRLh_Bind_Middle_01_L", "CTRLh_Bind_Middle_02_L_Offset|CTRLh_Bind_Middle_02_L", "CTRLh_Bind_Middle_03_L_Offset|CTRLh_Bind_Middle_03_L", "CTRLh_Bind_Middle_04_L_Offset|CTRLh_Bind_Middle_04_L", "CTRLh_Bind_Index_01_L_Offset|CTRLh_Bind_Index_01_L", "CTRLh_Bind_Index_02_L_Offset|CTRLh_Bind_Index_02_L", "CTRLh_Bind_Index_03_L_Offset|CTRLh_Bind_Index_03_L", "CTRLh_Bind_Index_04_L_Offset|CTRLh_Bind_Index_04_L", "CTRLh_Bind_Thumb_01_L_Offset|CTRLh_Bind_Thumb_01_L", "CTRLh_Bind_Thumb_02_L_Offset|CTRLh_Bind_Thumb_02_L", "CTRLh_Bind_Thumb_03_L_Offset|CTRLh_Bind_Thumb_03_L", "CTRLh_Bind_Pinky_03_L_Offset|CTRLh_Bind_Pinky_03_L", "CTRLh_Bind_Thumb_04_L_Offset|CTRLh_Bind_Thumb_04_L", "CTRLh_Bind_Clamp_L_Offset|CTRLh_Bind_Clamp_L", "CTRLh_Bind_Pinky_01_L_Offset|CTRLh_Bind_Pinky_01_L", "CTRLh_Bind_Pinky_02_L_Offset|CTRLh_Bind_Pinky_02_L", "CTRLh_Bind_Pinky_04_L_Offset|CTRLh_Bind_Pinky_04_L")
ctrlh = cmds.ls(sl=True)
x=0
y=len(ctrlh)
cmds.select(clear=True)

for x in range (0, y):
    cmds.createNode('transform',n ='Master1')
    grp1 = ['Master1']
    Master1 = cmds.ls(sl=True)
    cmds.matchTransform(Master1, ctrlh[x])
    cmds.parent(Master1, ctrlh[x])
    cmds.rename('Master1', ctrlh[x]+"_Master")

cmds.select("CTRLh_Bind_Hand_R_Offset|CTRLh_Bind_Hand_R", "CTRLh_Bind_Palm_R_Offset|CTRLh_Bind_Palm_R", "CTRLh_Bind_Ring_01_R_Offset|CTRLh_Bind_Ring_01_R", "CTRLh_Bind_Ring_02_R_Offset|CTRLh_Bind_Ring_02_R", "CTRLh_Bind_Ring_03_R_Offset|CTRLh_Bind_Ring_03_R", "CTRLh_Bind_Ring_04_R_Offset|CTRLh_Bind_Ring_04_R", "CTRLh_Bind_Middle_01_R_Offset|CTRLh_Bind_Middle_01_R", "CTRLh_Bind_Middle_02_R_Offset|CTRLh_Bind_Middle_02_R", "CTRLh_Bind_Middle_03_R_Offset|CTRLh_Bind_Middle_03_R", "CTRLh_Bind_Middle_04_R_Offset|CTRLh_Bind_Middle_04_R", "CTRLh_Bind_Index_01_R_Offset|CTRLh_Bind_Index_01_R", "CTRLh_Bind_Index_02_R_Offset|CTRLh_Bind_Index_02_R", "CTRLh_Bind_Index_03_R_Offset|CTRLh_Bind_Index_03_R", "CTRLh_Bind_Index_04_R_Offset|CTRLh_Bind_Index_04_R", "CTRLh_Bind_Thumb_01_R_Offset|CTRLh_Bind_Thumb_01_R", "CTRLh_Bind_Thumb_02_R_Offset|CTRLh_Bind_Thumb_02_R", "CTRLh_Bind_Thumb_03_R_Offset|CTRLh_Bind_Thumb_03_R", "CTRLh_Bind_Pinky_03_R_Offset|CTRLh_Bind_Pinky_03_R", "CTRLh_Bind_Thumb_04_R_Offset|CTRLh_Bind_Thumb_04_R", "CTRLh_Bind_Clamp_R_Offset|CTRLh_Bind_Clamp_R", "CTRLh_Bind_Pinky_01_R_Offset|CTRLh_Bind_Pinky_01_R", "CTRLh_Bind_Pinky_02_R_Offset|CTRLh_Bind_Pinky_02_R", "CTRLh_Bind_Pinky_04_R_Offset|CTRLh_Bind_Pinky_04_R")
ctrlh = cmds.ls(sl=True)
x=0
y=len(ctrlh)
cmds.select(clear=True)

for x in range (0, y):
    cmds.createNode('transform',n ='Master1')
    grp1 = ['Master1']
    Master1 = cmds.ls(sl=True)
    cmds.matchTransform(Master1, ctrlh[x])
    cmds.parent(Master1, ctrlh[x])
    cmds.rename('Master1', ctrlh[x]+"_Master")
    

cmds.select(all=True,hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('CTRLh_Bind_', 'CTRL_'))
cmds.select(clear=True)



#Hierarchy

cmds.parent('CTRL_Palm_L_Offset','CTRL_Hand_L_Master')
cmds.parent('CTRL_Thumb_04_L_Offset','CTRL_Thumb_03_L_Master')
cmds.parent('CTRL_Thumb_03_L_Offset','CTRL_Thumb_02_L_Master')
cmds.parent('CTRL_Thumb_02_L_Offset','CTRL_Thumb_01_L_Master')
cmds.parent('CTRL_Thumb_01_L_Offset','CTRL_Hand_L_Master')
cmds.parent('CTRL_Ring_04_L_Offset','CTRL_Ring_03_L_Master')
cmds.parent('CTRL_Ring_03_L_Offset','CTRL_Ring_02_L_Master')
cmds.parent('CTRL_Ring_02_L_Offset','CTRL_Ring_01_L_Master')
cmds.parent('CTRL_Ring_01_L_Offset','CTRL_Palm_L_Master')
cmds.parent('CTRL_Middle_04_L_Offset','CTRL_Middle_03_L_Master')
cmds.parent('CTRL_Middle_03_L_Offset','CTRL_Middle_02_L_Master')
cmds.parent('CTRL_Middle_02_L_Offset','CTRL_Middle_01_L_Master')
cmds.parent('CTRL_Middle_01_L_Offset','CTRL_Palm_L_Master')
cmds.parent('CTRL_Index_04_L_Offset','CTRL_Index_03_L_Master')
cmds.parent('CTRL_Index_03_L_Offset','CTRL_Index_02_L_Master')
cmds.parent('CTRL_Index_02_L_Offset','CTRL_Index_01_L_Master')
cmds.parent('CTRL_Index_01_L_Offset','CTRL_Palm_L_Master')
cmds.parent('CTRL_Pinky_04_L_Offset','CTRL_Pinky_03_L_Master')
cmds.parent('CTRL_Pinky_03_L_Offset','CTRL_Pinky_02_L_Master')
cmds.parent('CTRL_Pinky_02_L_Offset','CTRL_Pinky_01_L_Master')
cmds.parent('CTRL_Pinky_01_L_Offset','CTRL_Clamp_L_Master')
cmds.parent('CTRL_Clamp_L_Offset','CTRL_Hand_L_Master')

cmds.parent('CTRL_Palm_R_Offset','CTRL_Hand_R_Master')
cmds.parent('CTRL_Thumb_04_R_Offset','CTRL_Thumb_03_R_Master')
cmds.parent('CTRL_Thumb_03_R_Offset','CTRL_Thumb_02_R_Master')
cmds.parent('CTRL_Thumb_02_R_Offset','CTRL_Thumb_01_R_Master')
cmds.parent('CTRL_Thumb_01_R_Offset','CTRL_Hand_R_Master')
cmds.parent('CTRL_Ring_04_R_Offset','CTRL_Ring_03_R_Master')
cmds.parent('CTRL_Ring_03_R_Offset','CTRL_Ring_02_R_Master')
cmds.parent('CTRL_Ring_02_R_Offset','CTRL_Ring_01_R_Master')
cmds.parent('CTRL_Ring_01_R_Offset','CTRL_Palm_R_Master')
cmds.parent('CTRL_Middle_04_R_Offset','CTRL_Middle_03_R_Master')
cmds.parent('CTRL_Middle_03_R_Offset','CTRL_Middle_02_R_Master')
cmds.parent('CTRL_Middle_02_R_Offset','CTRL_Middle_01_R_Master')
cmds.parent('CTRL_Middle_01_R_Offset','CTRL_Palm_R_Master')
cmds.parent('CTRL_Index_04_R_Offset','CTRL_Index_03_R_Master')
cmds.parent('CTRL_Index_03_R_Offset','CTRL_Index_02_R_Master')
cmds.parent('CTRL_Index_02_R_Offset','CTRL_Index_01_R_Master')
cmds.parent('CTRL_Index_01_R_Offset','CTRL_Palm_R_Master')
cmds.parent('CTRL_Pinky_04_R_Offset','CTRL_Pinky_03_R_Master')
cmds.parent('CTRL_Pinky_03_R_Offset','CTRL_Pinky_02_R_Master')
cmds.parent('CTRL_Pinky_02_R_Offset','CTRL_Pinky_01_R_Master')
cmds.parent('CTRL_Pinky_01_R_Offset','CTRL_Clamp_R_Master')
cmds.parent('CTRL_Clamp_R_Offset','CTRL_Hand_R_Master')
cmds.createNode('transform',n ='Ctrl_Fingers_L')
cmds.createNode('transform',n ='Ctrl_Fingers_R')
cmds.parent('CTRL_Index_01_R_Offset', 'Ctrl_Fingers_R')
cmds.parent('CTRL_Index_01_L_Offset', 'Ctrl_Fingers_L')
cmds.parent('CTRL_Pinky_01_R_Offset', 'Ctrl_Fingers_R')
cmds.parent('CTRL_Pinky_01_L_Offset', 'Ctrl_Fingers_L')
cmds.parent('CTRL_Thumb_01_R_Offset', 'Ctrl_Fingers_R')
cmds.parent('CTRL_Thumb_01_L_Offset', 'Ctrl_Fingers_L')
cmds.parent('CTRL_Middle_01_R_Offset','Ctrl_Fingers_R')
cmds.parent('CTRL_Middle_01_L_Offset','Ctrl_Fingers_L')
cmds.parent('CTRL_Ring_01_R_Offset','Ctrl_Fingers_R')
cmds.parent('CTRL_Ring_01_L_Offset','Ctrl_Fingers_L')
cmds.parent('Ctrl_Fingers_R', 'Ctrl_01')
cmds.parent('Ctrl_Fingers_L', 'Ctrl_01')
cmds.delete('CTRL_Hand_R_Offset')
cmds.delete('CTRL_Hand_L_Offset')
cmds.createNode('transform',n ='Joint_Hand_L')
cmds.createNode('transform',n ='Joint_Hand_R')
cmds.createNode('transform',n ='Joints_Hands')
cmds.parent('Bind_Hand_R_Offset', 'Joint_Hand_R')
cmds.parent('Bind_Hand_L_Offset', 'Joint_Hand_L')
cmds.parent('Joint_Hand_R', 'Joints_Hands')
cmds.parent('Joint_Hand_L', 'Joints_Hands')
cmds.parent('Joints_Hands', 'Joint_01')

cmds.select(clear=True)
cmds.select('LocH*')
cmds.group(n="Locators_Hands")
cmds.parent('Locators_Hands', 'Locators_Place')
cmds.select(all=True, hi=True)
for item in pm.selected():
    item.rename(item.name().replace('LocH_', 'Loc_Pl_'))


cmds.select(clear=True)