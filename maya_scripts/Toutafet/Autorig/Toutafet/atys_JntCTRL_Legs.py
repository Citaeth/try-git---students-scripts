import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm



#1-Create Joint

cmds.select('LocLD*')
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
    item.rename(item.name().replace('DrvJnt_LocLD_', 'DrvJnt_'))

cmds.select('LocL_*')
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
    item.rename(item.name().replace('Bind_LocL_', 'Bind_'))


cmds.select(clear=True)



#2-Hierarchy
cmds.select("DrvJnt_Ankle*", "DrvJnt_Knee*", "DrvJnt_Leg*", "Bind_Toes*", "Bind_Ball*", "Bind_Feet*")
cmds.makeIdentity( apply=True )

cmds.parent('DrvJnt_Ankle_R','DrvJnt_Knee_R')
cmds.parent('DrvJnt_Knee_R','DrvJnt_Leg_R')
cmds.parent('DrvJnt_Ankle_L','DrvJnt_Knee_L')
cmds.parent('DrvJnt_Knee_L','DrvJnt_Leg_L')
cmds.parent('Bind_Toes_L','Bind_Ball_L')
cmds.parent('Bind_Ball_L','Bind_Feet_L')
cmds.parent('Bind_Toes_R','Bind_Ball_R')
cmds.parent('Bind_Ball_R','Bind_Feet_R')



#3-Orient Joint

#Orient DrvJnt_Leg_L

cmds.joint("DrvJnt_Leg_L" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Knee_L" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Ankle_L" ,e=True,zso=True,oj="none")

cmds.joint("DrvJnt_Leg_L" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("DrvJnt_Knee_L" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("DrvJnt_Ankle_L" ,e=True,zso=True,oj="none")

#Orient DrvJnt_Leg_R

cmds.joint("DrvJnt_Leg_R" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Knee_R" ,e=True,zso=True,oj="none")
cmds.joint("DrvJnt_Ankle_L" ,e=True,zso=True,oj="none")

cmds.joint("DrvJnt_Leg_R" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("DrvJnt_Knee_R" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("DrvJnt_Ankle_R" ,e=True,zso=True,oj="none")

#Orient Thigh

cmds.matchTransform("Bind_Thigh_L", "DrvJnt_Leg_L")
cmds.matchTransform("Bind_Thigh_R", "DrvJnt_Leg_R")
cmds.matchTransform("Bind_Hips", "Jnt_Root")

#Orient DrvJnt_Feet_R

cmds.joint("Bind_Feet_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ball_R" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Toes_R" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Feet_R" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("Bind_Ball_R" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("Bind_Toes_R" ,e=True,zso=True,oj="none")

#Orient DrvJnt_Feet_L

cmds.joint("Bind_Feet_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Ball_L" ,e=True,zso=True,oj="none")
cmds.joint("Bind_Toes_L" ,e=True,zso=True,oj="none")

cmds.joint("Bind_Feet_L" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("Bind_Ball_L" ,e=True,zso=True,oj="xyz", sao="xup")
cmds.joint("Bind_Toes_L" ,e=True,zso=True,oj="none")

cmds.parent('Bind_Thigh_L','Bind_Hips')
cmds.parent('Bind_Thigh_R','Bind_Hips')



#3-Create controleurs and match position and orientation

cmds.select("DrvJnt_Leg_L",hi=True)
leg = cmds.ls(sl=True)
x=0
y=len(leg)
cmds.select(clear=True)
for x in range (0, y):
    ctrll=cmds.circle(r=3.5, n="CTRLl_"+leg[x])
    cmds.matchTransform(ctrll,leg[x])

cmds.select("CTRLl_DrvJnt_Leg_L")      
for item in pm.selected():
    item.rename(item.name().replace('_Leg_L', '_Thigh_L'))

cmds.duplicate("CTRLl_DrvJnt_Ankle_L", n="CTRL_Leg_L")

cmds.select("DrvJnt_Leg_R",hi=True)
leg = cmds.ls(sl=True)
x=0
y=len(leg)
cmds.select(clear=True)
for x in range (0, y):
    ctrll=cmds.circle(r=3.5, n="CTRLl_"+leg[x])
    cmds.matchTransform(ctrll,leg[x])

cmds.select("CTRLl_DrvJnt_Leg_R")      
for item in pm.selected():
    item.rename(item.name().replace('_Leg_R', '_Thigh_R'))

cmds.duplicate("CTRLl_DrvJnt_Ankle_R", n="CTRL_Leg_R")

cmds.circle(r=2.5, n="CTRLl_Toe_L")
cmds.circle(r=2.5, n="CTRLl_Toe_R")
cmds.circle(r=5, n="CTRLl_Hips")
cmds.matchTransform("CTRLl_Hips", "Bind_Hips")
cmds.matchTransform("CTRLl_Toe_R","Bind_Ball_R")
cmds.matchTransform("CTRLl_Toe_L","Bind_Ball_L")

cmds.select("CTRLl*")
shapeList = cmds.ls(sl=True)
ctrll = cmds.listRelatives(shapeList, parent=True, fullPath=True)
x=0
y=len(ctrll)
cmds.select(clear=True)
for x in range (0, y):
    cmds.createNode('transform',n ='Offset1')
    grp1 = ['Offset1']
    offset1 = cmds.ls(sl=True)
    cmds.matchTransform(offset1, ctrll[x])
    cmds.parent(ctrll[x], grp1)
    cmds.rename('Offset1', ctrll[x]+"_Offset")

cmds.select("CTRLl_Toe_R", "CTRLl_Toe_L", "CTRLl_DrvJnt_Ankle_R", "CTRLl_DrvJnt_Ankle_L", "CTRLl_DrvJnt_Knee_R", "CTRLl_DrvJnt_Knee_L", "CTRLl_DrvJnt_Thigh_R", "CTRLl_DrvJnt_Thigh_L","CTRLl_Hips")
ctrll = cmds.ls(sl=True)
x=0
y=len(ctrll)
cmds.select(clear=True)

for x in range (0, y):
    cmds.createNode('transform',n ='Master1')
    grp1 = ['Master1']
    Master1 = cmds.ls(sl=True)
    cmds.matchTransform(Master1, ctrll[x])
    cmds.parent(Master1, ctrll[x])
    cmds.rename('Master1', ctrll[x]+"_Master")
    
cmds.select(all=True,hi=True)      
for item in pm.selected():
    item.rename(item.name().replace('CTRLl_DrvJnt_', 'CTRL_'))
    item.rename(item.name().replace('CTRLl_', 'CTRL_'))
cmds.select(clear=True)



#4-Hierarchy

#1-Create offset_Joint

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "DrvJnt_Leg_L")
cmds.parent("DrvJnt_Leg_L", grp1)
cmds.rename('Offset1', "DrvJnt_Leg_L_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "DrvJnt_Leg_R")
cmds.parent("DrvJnt_Leg_R", grp1)
cmds.rename('Offset1', "DrvJnt_Leg_R_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Feet_R")
cmds.parent("Bind_Feet_R", grp1)
cmds.rename('Offset1', "Bind_Feet_R_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Feet_L")
cmds.parent("Bind_Feet_L", grp1)
cmds.rename('Offset1', "Bind_Feet_L_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Hips")
cmds.parent("Bind_Hips", grp1)
cmds.rename('Offset1', "Bind_Hips_Offset")

#2- Ranges ta chambre

#Joint 

cmds.createNode('transform',n ='Joint_Hip_Leg')
cmds.createNode('transform',n ='Grp_FK_Leg_L')
cmds.createNode('transform',n ='Grp_FK_Leg_R')
cmds.createNode('transform',n ='Joint_Foot')
cmds.parent('Grp_FK_Leg_L', 'Joint_Hip_Leg')
cmds.parent('Grp_FK_Leg_R', 'Joint_Hip_Leg')
cmds.parent("Bind_Hips_Offset", 'Joint_Hip_Leg')
cmds.parent("DrvJnt_Leg_R_Offset", 'Joint_Hip_Leg')
cmds.parent("DrvJnt_Leg_L_Offset", 'Joint_Hip_Leg')
cmds.parent("Bind_Feet_R_Offset", 'Joint_Foot')
cmds.parent("Bind_Feet_L_Offset", 'Joint_Foot')
cmds.parent('Joint_Foot', "Joint_01")
cmds.parent('Joint_Hip_Leg', "Joint_01")

#Ctrl

cmds.parent("CTRL_Hips_Offset", "CTRL_Root_Master")
cmds.parent("CTRL_Ankle_L_Offset", "CTRL_Knee_L_Master")
cmds.parent("CTRL_Knee_L_Offset" , "CTRL_Thigh_L_Master")
cmds.parent("CTRL_Ankle_R_Offset", "CTRL_Knee_R_Master")
cmds.parent("CTRL_Knee_R_Offset" , "CTRL_Thigh_R_Master")
cmds.parent("CTRL_Thigh_R_Offset", 'Grp_FK_Leg_R')
cmds.parent("CTRL_Thigh_L_Offset", 'Grp_FK_Leg_L')
cmds.parent("CTRL_Toe_R_Offset", 'Grp_FK_Leg_R')
cmds.parent("CTRL_Toe_L_Offset", 'Grp_FK_Leg_L')
cmds.parent("CTRL_Leg_L", 'Ctrl_01')
cmds.parent("CTRL_Leg_R", 'Ctrl_01')
cmds.select("CTRL_Leg_R", "CTRL_Leg_L")
cmds.makeIdentity( apply=True )

#Bind_Knee_Preserve
cmds.select(clear=True)
cmds.joint(n="Bind_Knee_Preserve_R")
cmds.joint(n="Bind_Knee_Preserve_L")
cmds.matchTransform("Bind_Knee_Preserve_R", "DrvJnt_Knee_R")
cmds.matchTransform("Bind_Knee_Preserve_L", "DrvJnt_Knee_L")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Knee_Preserve_R")
cmds.parent("Bind_Knee_Preserve_R", grp1)
cmds.rename('Offset1', "Bind_Knee_Preserve_R_Offset")

cmds.createNode('transform',n ='Offset1')
grp1 = ['Offset1']
offset1 = cmds.ls(sl=True)
cmds.matchTransform(offset1, "Bind_Knee_Preserve_L")
cmds.parent("Bind_Knee_Preserve_L", grp1)
cmds.rename('Offset1', "Bind_Knee_Preserve_L_Offset")

cmds.select("Bind_Knee_Preserve_L_Offset")
cmds.group(n="Bind_Knee_Preserve_L_Move_01")
cmds.select("Bind_Knee_Preserve_R_Offset")
cmds.group(n="Bind_Knee_Preserve_R_Move_01")

cmds.parent("Bind_Knee_Preserve_R_Move_01", "Joint_Hip_Leg")
cmds.parent("Bind_Knee_Preserve_L_Move_01", "Joint_Hip_Leg")


cmds.select(clear=True)
cmds.select('LocL*')
cmds.group(n="Locators_Legs")
cmds.parent('Locators_Legs', 'Locators_Place')
cmds.select(all=True, hi=True)
for item in pm.selected():
    item.rename(item.name().replace('LocL_', 'Loc_Pl_'))
    item.rename(item.name().replace('LocLD_', 'Loc_Pl_'))

cmds.select(clear=True)

#CTRL_Legs set up

cmds.select('CTRL_Leg_L', 'CTRL_Leg_R')

sl = cmds.ls(sl=True, sn=True)
Leg_L = sl[0]
Leg_R = sl[1]
print Leg_L
print Leg_R

#Leg_L

# 1-Premier separateur
cmds.addAttr(sl[0], longName='_______', attributeType='enum', enumName='____')
cmds.setAttr( Leg_L+'._______', channelBox=True )
cmds.setAttr( Leg_L+'._______', keyable=True )

#2-Twist Leg
cmds.addAttr(sl[0], longName='Twist_Leg_L', attributeType='float' )
cmds.setAttr( Leg_L+'.Twist_Leg_L', channelBox=True )
cmds.setAttr( Leg_L+'.Twist_Leg_L', keyable=True )

#3-Deuxieme separateur
cmds.addAttr(sl[0], longName='________', attributeType='enum', enumName='_____')
cmds.setAttr( Leg_L+'.________', channelBox=True )
cmds.setAttr( Leg_L+'.________', keyable=True )

#4-Footroll_L
cmds.addAttr(sl[0], longName='Foot_Roll_L', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_L+'.Foot_Roll_L', channelBox=True )
cmds.setAttr( Leg_L+'.Foot_Roll_L', keyable=True )

#5-Twist Heel
cmds.addAttr(sl[0], longName='Twist_Heel_L', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_L+'.Twist_Heel_L', channelBox=True )
cmds.setAttr( Leg_L+'.Twist_Heel_L', keyable=True )

#6-Twist Toe
cmds.addAttr(sl[0], longName='Twist_Toe_L', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_L+'.Twist_Toe_L', channelBox=True )
cmds.setAttr( Leg_L+'.Twist_Toe_L', keyable=True )

#7-Flex Toe
cmds.addAttr(sl[0], longName='Flex_Toe_L', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_L+'.Flex_Toe_L', channelBox=True )
cmds.setAttr( Leg_L+'.Flex_Toe_L', keyable=True )

#8-Bank
cmds.addAttr(sl[0], longName='Bank_L', attributeType='float', minValue=-30.0, maxValue=30.0 )
cmds.setAttr( Leg_L+'.Bank_L', channelBox=True )
cmds.setAttr( Leg_L+'.Bank_L', keyable=True )

#9-Twist Leg L -Constraint
cmds.addAttr(sl[0], longName='Twist_Constraint', attributeType='bool')
cmds.setAttr( Leg_L+'.Twist_Constraint', channelBox=True )
cmds.setAttr( Leg_L+'.Twist_Constraint', keyable=True)

#10-Troisieme separateur
cmds.addAttr(sl[0], longName='______', attributeType='enum', enumName='______')
cmds.setAttr( Leg_L+'.______', channelBox=True )
cmds.setAttr( Leg_L+'.______', keyable=True )

#11-Bend leg L
cmds.addAttr(sl[0], longName='Bend_Leg_L', attributeType='bool')
cmds.setAttr( Leg_L+'.Bend_Leg_L', channelBox=True )
cmds.setAttr( Leg_L+'.Bend_Leg_L', keyable=True)

#CTRL_Leg_R

# 1-Premier separateur
cmds.addAttr(sl[1], longName='_______', attributeType='enum', enumName='____')
cmds.setAttr( Leg_R+'._______', channelBox=True )
cmds.setAttr( Leg_R+'._______', keyable=True )

#2-Twist Leg
cmds.addAttr(sl[1], longName='Twist_Leg_R', attributeType='float' )
cmds.setAttr( Leg_R+'.Twist_Leg_R', channelBox=True )
cmds.setAttr( Leg_R+'.Twist_Leg_R', keyable=True )

#3-Deuxième separateur
cmds.addAttr(sl[1], longName='________', attributeType='enum', enumName='_____')
cmds.setAttr( Leg_R+'.________', channelBox=True )
cmds.setAttr( Leg_R+'.________', keyable=True )

#4-Footroll_R
cmds.addAttr(sl[1], longName='Foot_Roll_R', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_R+'.Foot_Roll_R', channelBox=True )
cmds.setAttr( Leg_R+'.Foot_Roll_R', keyable=True )

#5-Twist Heel
cmds.addAttr(sl[1], longName='Twist_Heel_R', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_R+'.Twist_Heel_R', channelBox=True )
cmds.setAttr( Leg_R+'.Twist_Heel_R', keyable=True )

#6-Twist Toe
cmds.addAttr(sl[1], longName='Twist_Toe_R', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_R+'.Twist_Toe_R', channelBox=True )
cmds.setAttr( Leg_R+'.Twist_Toe_R', keyable=True )

#7-Flex Toe
cmds.addAttr(sl[1], longName='Flex_Toe_R', attributeType='float', minValue=-1.0, maxValue=1.0 )
cmds.setAttr( Leg_R+'.Flex_Toe_R', channelBox=True )
cmds.setAttr( Leg_R+'.Flex_Toe_R', keyable=True )

#8-Bank
cmds.addAttr(sl[1], longName='Bank_R', attributeType='float', minValue=-30.0, maxValue=30.0 )
cmds.setAttr( Leg_R+'.Bank_R', channelBox=True )
cmds.setAttr( Leg_R+'.Bank_R', keyable=True )

#9-Twist Leg R -Constraint
cmds.addAttr(sl[1], longName='Twist_Constraint', attributeType='bool')
cmds.setAttr( Leg_R+'.Twist_Constraint', channelBox=True )
cmds.setAttr( Leg_R+'.Twist_Constraint', keyable=True)

#10-Troisieme separateur
cmds.addAttr(sl[1], longName='______', attributeType='enum', enumName='______')
cmds.setAttr( Leg_R+'.______', channelBox=True )
cmds.setAttr( Leg_R+'.______', keyable=True )

#11-Bend leg R
cmds.addAttr(sl[1], longName='Bend_Leg_R', attributeType='bool')
cmds.setAttr( Leg_R+'.Bend_Leg_R', channelBox=True )
cmds.setAttr( Leg_R+'.Bend_Leg_R', keyable=True)



#END