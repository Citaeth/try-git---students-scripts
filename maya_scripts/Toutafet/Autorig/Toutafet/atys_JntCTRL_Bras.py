import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm



#1-Create Joint

cmds.select('LocAD*')
shapeList = cmds.ls(sl=True)
loc = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(loc)
cmds.select(clear=True)
for x in range (0, y):
    cmds.select(clear=True)
    jnt=cmds.joint(n='DrvJnt'+loc[x])
    cmds.matchTransform(jnt,loc[x])
cmds.select(all=True, hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('DrvJnt_LocAD_', 'DrvJnt_'))


cmds.select('LocA_*')
shapeList = cmds.ls(sl=True)
loc = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(loc)
cmds.select(clear=True)
for x in range (0, y):
    cmds.select(clear=True)
    jnt=cmds.joint(n='Bind'+loc[x])
    cmds.matchTransform(jnt,loc[x])
cmds.select(all=True, hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('Bind_LocA_', 'Bind_'))

cmds.select(clear=True)



#2-Hierarchy
cmds.select("DrvJnt_Elbow*", "DrvJnt_Shoulder*", "DrvJnt_Wrist*", "Bind_Clavicle*")
cmds.makeIdentity( apply=True )

cmds.parent('DrvJnt_Wrist_L','DrvJnt_Elbow_L')
cmds.parent('DrvJnt_Elbow_L','DrvJnt_Shoulder_L')
cmds.parent('DrvJnt_Wrist_R','DrvJnt_Elbow_R')
cmds.parent('DrvJnt_Elbow_R','DrvJnt_Shoulder_R')
cmds.parent('Bind_Clavicle_End_L','Bind_Clavicle_01_L')
cmds.parent('Bind_Clavicle_End_R','Bind_Clavicle_01_R')



#3-Orient Joint

#Orient DrvJnt_L

cmds.joint("DrvJnt_Shoulder_L" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Elbow_L" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Wrist_L" ,e=True,zso=True,oj="none")

cmds.joint("DrvJnt_Shoulder_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("DrvJnt_Elbow_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("DrvJnt_Wrist_L" ,e=True,zso=True,oj="none")

#Orient DrvJnt_R

cmds.joint("DrvJnt_Shoulder_R" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Elbow_R" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Wrist_R" ,e=True,zso=True,oj="none")

cmds.joint("DrvJnt_Shoulder_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("DrvJnt_Elbow_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("DrvJnt_Wrist_R" ,e=True,zso=True,oj="none")

#Orient Clavicle_L

cmds.joint("Bind_Clavicle_01_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Clavicle_End_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Clavicle_01_L" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Clavicle_End_L" ,e=True,zso=True,oj="none")

cmds.matchTransform("Bind_Clavicle_End_L", "DrvJnt_Shoulder_L")

#Orient Clavicle_R

cmds.joint("Bind_Clavicle_01_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Clavicle_End_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Clavicle_01_R" ,e=True,zso=True,oj="xyz", sao="yup")
cmds.joint("Bind_Clavicle_End_R" ,e=True,zso=True,oj="none")

cmds.matchTransform("Bind_Clavicle_End_R", "DrvJnt_Shoulder_R")



#3-Create controleurs and match position and orientation

cmds.select("DrvJnt_Shoulder_L",hi=True)
arm = cmds.ls(sl=True)
x=0
y=len(arm)
cmds.select(clear=True)
for x in range (0, y):
    ctrla=cmds.circle(r=2.5, n="CTRLa_"+arm[x])
    cmds.matchTransform(ctrla,arm[x])
cmds.duplicate("CTRLa_DrvJnt_Wrist_L", n="CTRLa_DrvJnt_Arm_L")

cmds.select("DrvJnt_Shoulder_R",hi=True)
arm = cmds.ls(sl=True)
x=0
y=len(arm)
cmds.select(clear=True)
for x in range (0, y):
    ctrla=cmds.circle(r=2.5, n="CTRLa_"+arm[x])
    cmds.matchTransform(ctrla,arm[x])
cmds.duplicate("CTRLa_DrvJnt_Wrist_R", n="CTRLa_DrvJnt_Arm_R")

cmds.circle(r=2.5, n="CTRLa_Clavicle_L")
cmds.circle(r=2.5, n="CTRLa_Clavicle_R")
cmds.matchTransform("CTRLa_Clavicle_R","Bind_Clavicle_01_R")
cmds.matchTransform("CTRLa_Clavicle_L","Bind_Clavicle_01_L")

cmds.select("CTRLa*")
shapeList = cmds.ls(sl=True)
ctrla = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(ctrla)
cmds.select(clear=True)
for x in range (0, y):
    cmds.createNode('transform',n ='Offset1')
    grp1 = ['Offset1']
    offset1 = cmds.ls(sl=True)
    cmds.matchTransform(offset1, ctrla[x])
    cmds.parent(ctrla[x], grp1)
    cmds.rename('Offset1', ctrla[x]+"_Offset")

cmds.select("CTRLa_Clavicle_L", "CTRLa_Clavicle_R", "CTRLa_DrvJnt_Arm_R", "CTRLa_DrvJnt_Arm_L", "CTRLa_DrvJnt_Wrist_L", "CTRLa_DrvJnt_Wrist_R", "CTRLa_DrvJnt_Elbow_L", "CTRLa_DrvJnt_Elbow_R", "CTRLa_DrvJnt_Shoulder_L", "CTRLa_DrvJnt_Shoulder_R")
ctrla = cmds.ls(sl=True)
x=0
y=len(ctrla)
cmds.select(clear=True)

for x in range (0, y):
    cmds.createNode('transform',n ='Master1')
    grp1 = ['Master1']
    Master1 = cmds.ls(sl=True)
    cmds.matchTransform(Master1, ctrla[x])
    cmds.parent(Master1, ctrla[x])
    cmds.rename('Master1', ctrla[x]+"_Master")
    
cmds.select(all=True,hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('CTRLa_DrvJnt_', 'CTRL_'))
    item.rename(item.name().replace('CTRLa_', 'CTRL_'))
cmds.select(clear=True)



#4-Hierarchy

#1-Create offset_Joint

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, 'DrvJnt_Shoulder_L')
cmds.parent('DrvJnt_Shoulder_L', grp1)
cmds.rename('Offset1',"DrvJnt_Shoulder_L_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, 'DrvJnt_Shoulder_R')
cmds.parent('DrvJnt_Shoulder_R', grp1)
cmds.rename('Offset1',"DrvJnt_Shoulder_R_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, 'Bind_Clavicle_01_L')
cmds.parent('Bind_Clavicle_01_L', grp1)
cmds.rename('Offset1',"Bind_Clavicle_01_L_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, 'Bind_Clavicle_01_R')
cmds.parent('Bind_Clavicle_01_R', grp1)
cmds.rename('Offset1',"Bind_Clavicle_01_R_Offset")

cmds.createNode('transform',n ='Joint_Clavicles_Arms')
cmds.parent("Bind_Clavicle_01_R_Offset", 'Joint_Clavicles_Arms')
cmds.parent("Bind_Clavicle_01_L_Offset", 'Joint_Clavicles_Arms')
cmds.parent("DrvJnt_Shoulder_R_Offset", 'Joint_Clavicles_Arms')
cmds.parent("DrvJnt_Shoulder_L_Offset", 'Joint_Clavicles_Arms')
cmds.parent("CTRL_Wrist_L_Offset", "CTRL_Elbow_L_Master")
cmds.parent("CTRL_Elbow_L_Offset", "CTRL_Shoulder_L_Master")
cmds.createNode('transform',n ='FK_Arm_L')
cmds.createNode('transform',n ='CTRL_Arms')
cmds.parent("CTRL_Shoulder_L_Offset", "FK_Arm_L")
cmds.parent("FK_Arm_L", "CTRL_Arms")
cmds.parent("CTRL_Wrist_R_Offset", "CTRL_Elbow_R_Master")
cmds.parent("CTRL_Elbow_R_Offset", "CTRL_Shoulder_R_Master")
cmds.createNode('transform',n ='FK_Arm_R')
cmds.parent("CTRL_Shoulder_R_Offset", "FK_Arm_R")
cmds.parent("FK_Arm_R", "CTRL_Arms")
cmds.parent("CTRL_Arms","Joint_Clavicles_Arms")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, 'CTRL_Arm_L_Offset')
cmds.parent('CTRL_Arm_L_Offset', grp1)
cmds.rename('Offset1',"CTRL_Arm_L_Move_01")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, 'CTRL_Arm_R_Offset')
cmds.parent('CTRL_Arm_R_Offset', grp1)
cmds.rename('Offset1',"CTRL_Arm_R_Move_01")

cmds.parent("CTRL_Arm_L_Move_01", "Ctrl_01")
cmds.parent("CTRL_Arm_R_Move_01", "Ctrl_01")
cmds.parent("CTRL_Clavicle_L_Offset", "CTRL_Shoulders_Master")
cmds.parent("CTRL_Clavicle_R_Offset", "CTRL_Shoulders_Master")
cmds.parent("Joint_Clavicles_Arms", "Joint_01")




#5-Bind_Elbow_Preserve

cmds.select(clear=True)
cmds.joint(n="Bind_Elbow_Preserve_R")
cmds.joint(n="Bind_Elbow_Preserve_L")
cmds.matchTransform("Bind_Elbow_Preserve_R", "DrvJnt_Elbow_R")
cmds.matchTransform("Bind_Elbow_Preserve_L", "DrvJnt_Elbow_L")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Elbow_Preserve_R")
cmds.parent("Bind_Elbow_Preserve_R", grp1)
cmds.rename('Offset1', "Bind_Elbow_Preserve_R_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Elbow_Preserve_L")
cmds.parent("Bind_Elbow_Preserve_L", grp1)
cmds.rename('Offset1', "Bind_Elbow_Preserve_L_Offset")

cmds.select("Bind_Elbow_Preserve_L_Offset")
cmds.group(n="Bind_Elbow_Preserve_L_Move_01")
cmds.select("Bind_Elbow_Preserve_R_Offset")
cmds.group(n="Bind_Elbow_Preserve_R_Move_01")

cmds.parent("Bind_Elbow_Preserve_R_Move_01", "Joint_01")
cmds.parent("Bind_Elbow_Preserve_L_Move_01", "Joint_01")

cmds.select(clear=True)
cmds.select('LocA*')
cmds.group(n="Locators_Arms")
cmds.parent('Locators_Arms', 'Locators_Place')
cmds.select(all=True, hi=True)
for item in pm.selected():
    item.rename(item.name().replace('LocA_', 'Loc_Pl_'))
    item.rename(item.name().replace('LocAD_', 'Loc_Pl_'))

cmds.select(clear=True)


#6- Set Up CTRL Arm

cmds.select("CTRL_Arm_L", "CTRL_Arm_R")
sl = cmds.ls(sl=True, sn=True)
Arm_L = sl[0]
Arm_R = sl[1]
print Arm_L
print Arm_R

#1 Arm_L

# 1-Premier separateur
cmds.addAttr(sl[0], longName='_______', attributeType='enum', enumName='____')
cmds.setAttr( Arm_L+'._______', channelBox=True )
cmds.setAttr( Arm_L+'._______', keyable=True )

#2-Twist Arm
cmds.addAttr(sl[0], longName='Twist_Arm_L', attributeType='float' )
cmds.setAttr( Arm_L+'.Twist_Arm_L', channelBox=True )
cmds.setAttr( Arm_L+'.Twist_Arm_L', keyable=True )


#3-Deuxieme separateur
cmds.addAttr(sl[0], longName='________', attributeType='enum', enumName='_____')
cmds.setAttr( Arm_L+'.________', channelBox=True )
cmds.setAttr( Arm_L+'.________', keyable=True )

#4-Bend Arm L
cmds.addAttr(sl[0], longName='Bend_Arm_L', attributeType='bool')
cmds.setAttr( Arm_L+'.Bend_Arm_L', channelBox=True )
cmds.setAttr( Arm_L+'.Bend_Arm_L', keyable=True)

#5-Troisieme separateur
cmds.addAttr(sl[0], longName='______', attributeType='enum', enumName='_____')
cmds.setAttr( Arm_L+'.______', channelBox=True )
cmds.setAttr( Arm_L+'.______', keyable=True )

#5-Follow
cmds.addAttr(sl[0], longName='Follow_Arm_L', attributeType='enum', enumName='Chest:Root:World')
cmds.setAttr( Arm_L+'.Follow_Arm_L', channelBox=True )
cmds.setAttr( Arm_L+'.Follow_Arm_L', keyable=True )
	

#1 Arm_R

# 1-Premier separateur
cmds.addAttr(sl[1], longName='_______', attributeType='enum', enumName='____')
cmds.setAttr( Arm_R+'._______', channelBox=True )
cmds.setAttr( Arm_R+'._______', keyable=True )

#2-Twist Arm
cmds.addAttr(sl[1], longName='Twist_Arm_R', attributeType='float' )
cmds.setAttr( Arm_R+'.Twist_Arm_R', channelBox=True )
cmds.setAttr( Arm_R+'.Twist_Arm_R', keyable=True )


#3-Deuxieme separateur
cmds.addAttr(sl[1], longName='________', attributeType='enum', enumName='_____')
cmds.setAttr( Arm_R+'.________', channelBox=True )
cmds.setAttr( Arm_R+'.________', keyable=True )

#4-Bend Arm L
cmds.addAttr(sl[1], longName='Bend_Arm_R', attributeType='bool')
cmds.setAttr( Arm_R+'.Bend_Arm_R', channelBox=True )
cmds.setAttr( Arm_R+'.Bend_Arm_R', keyable=True)

#5-Troisieme separateur
cmds.addAttr(sl[1], longName='______', attributeType='enum', enumName='_____')
cmds.setAttr( Arm_R+'.______', channelBox=True )
cmds.setAttr( Arm_R+'.______', keyable=True )

#5-Follow
cmds.addAttr(sl[1], longName='Follow_Arm_R', attributeType='enum', enumName='Chest:Root:World')
cmds.setAttr( Arm_R+'.Follow_Arm_R', channelBox=True )
cmds.setAttr( Arm_R+'.Follow_Arm_R', keyable=True )

cmds.select(clear=True)
