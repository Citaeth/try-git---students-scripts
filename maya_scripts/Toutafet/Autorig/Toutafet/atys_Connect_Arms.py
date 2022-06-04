import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm




#1-Create CTRL_Switch

cmds.circle(r=5,n ='CTRL_Switch_R')
cmds.circle(r=5,n ='CTRL_Switch_L')
cmds.matchTransform('CTRL_Switch_L', 'DrvJnt_Elbow_L')
cmds.matchTransform('CTRL_Switch_R', 'DrvJnt_Elbow_R')

cmds.select(clear=True)
cmds.select('CTRL_Switch_R', 'CTRL_Switch_L')
cmds.makeIdentity( apply=True) 

#Set_Up CTRL_Switch

# 1-Premier separateur
cmds.addAttr('CTRL_Switch_R', longName='_______', attributeType='enum', enumName='____')
cmds.setAttr('CTRL_Switch_R._______', channelBox=True )
cmds.setAttr('CTRL_Switch_R._______', keyable=True )

cmds.addAttr('CTRL_Switch_L', longName='_______', attributeType='enum', enumName='____')
cmds.setAttr('CTRL_Switch_L._______', channelBox=True )
cmds.setAttr('CTRL_Switch_L._______', keyable=True )


# 2-IK/FK
cmds.addAttr('CTRL_Switch_R', longName='IK_FK_R_Arm', attributeType='enum', enumName='IK:FK')
cmds.setAttr('CTRL_Switch_R.IK_FK_R_Arm', channelBox=True )
cmds.setAttr('CTRL_Switch_R.IK_FK_R_Arm', keyable=True )

cmds.addAttr('CTRL_Switch_L', longName='IK_FK_L_Arm', attributeType='enum', enumName='IK:FK')
cmds.setAttr('CTRL_Switch_L.IK_FK_L_Arm', channelBox=True )
cmds.setAttr('CTRL_Switch_L.IK_FK_L_Arm', keyable=True )


# 3-Stretchy
cmds.addAttr('CTRL_Switch_R', longName='Stretchy_R_Arm', attributeType='bool')
cmds.setAttr('CTRL_Switch_R.Stretchy_R_Arm', channelBox=True )
cmds.setAttr('CTRL_Switch_R.Stretchy_R_Arm', keyable=True)

cmds.addAttr('CTRL_Switch_L', longName='Stretchy_L_Arm', attributeType='bool')
cmds.setAttr('CTRL_Switch_L.Stretchy_L_Arm', channelBox=True )
cmds.setAttr('CTRL_Switch_L.Stretchy_L_Arm', keyable=True)


# 4-Blend
cmds.addAttr('CTRL_Switch_R', longName='IK_FK_R_Blend', attributeType='float',  minValue=0, maxValue=1.0 )
cmds.setAttr('CTRL_Switch_R.IK_FK_R_Blend', channelBox=True )
cmds.setAttr('CTRL_Switch_R.IK_FK_R_Blend', keyable=True )

cmds.addAttr('CTRL_Switch_L', longName='IK_FK_L_Blend', attributeType='float',  minValue=0, maxValue=1.0 )
cmds.setAttr('CTRL_Switch_L.IK_FK_L_Blend', channelBox=True )
cmds.setAttr('CTRL_Switch_L.IK_FK_L_Blend', keyable=True )

cmds.select(clear=True)



#2-Parent CTRL Switch

#CTRL_Switch_L

cmds.parentConstraint('DrvJnt_Elbow_L', 'CTRL_Switch_L', mo=True, sr=["x","y","z"])

cmds.parent('CTRL_Switch_L', 'Ctrl_01')

#CTRL_Switch_R

cmds.parentConstraint('DrvJnt_Elbow_R', 'CTRL_Switch_R', mo=True, sr=["x","y","z"])
cmds.parent('CTRL_Switch_R', 'Ctrl_01')



# 3-Parent first pass


#CTRL_Clavicle_L to Bind

cmds.select(clear=True)
cmds.parentConstraint('CTRL_Clavicle_L_Master', 'Bind_Clavicle_01_L_Offset', mo=True)


#CTRL_Clavicle_R to Bind

cmds.select(clear=True)
cmds.parentConstraint('CTRL_Clavicle_R_Master', 'Bind_Clavicle_01_R_Offset', mo=True)


#Bind Clavicle to Drv Shoulder L

cmds.select(clear=True)
cmds.parentConstraint('Bind_Clavicle_End_L', 'DrvJnt_Shoulder_L_Offset', mo=True)


#Bind Clavicle to Drv Shoulder R

cmds.select(clear=True)
cmds.parentConstraint('Bind_Clavicle_End_R', 'DrvJnt_Shoulder_R_Offset', mo=True)


#Bind Clavicle to FK Shoulder L

cmds.select(clear=True)
cmds.parentConstraint('Bind_Clavicle_End_L', 'CTRL_Shoulder_L_Offset', mo=True)


#Bind Clavicle to FK Shoulder R

cmds.select(clear=True)
cmds.parentConstraint('Bind_Clavicle_End_R', 'CTRL_Shoulder_R_Offset', mo=True)



# 4-Create IK

cmds.ikHandle(name='IK_Arm_L', 
                  startJoint='DrvJnt_Shoulder_L', 
                  endEffector='DrvJnt_Wrist_L',)

cmds.rename('effector1', 'eff_Arm_L')


cmds.ikHandle(name='IK_Arm_R', 
                  startJoint='DrvJnt_Shoulder_R', 
                  endEffector='DrvJnt_Wrist_R',)

cmds.rename('effector1', 'eff_Arm_R')

#Parent IK_Arm_L

cmds.select(clear=True)
cmds.parentConstraint('CTRL_Arm_L', 'IK_Arm_L', mo=True)

#Parent IK_Arm_R

cmds.select(clear=True)
cmds.parentConstraint('CTRL_Arm_R', 'IK_Arm_R', mo=True)

cmds.circle(n='PoleVector_Arm_L')
cmds.circle(n='PoleVector_Arm_R')
cmds.matchTransform('PoleVector_Arm_L','DrvJnt_Elbow_L')
cmds.matchTransform('PoleVector_Arm_R','DrvJnt_Elbow_R')
cmds.select('PoleVector_Arm_L', 'PoleVector_Arm_R')
cmds.xform( r=True, t=(0, 0, -10) )
cmds.select('PoleVector_Arm_L', 'PoleVector_Arm_R')
cmds.makeIdentity( apply=True )
cmds.poleVectorConstraint('PoleVector_Arm_L', 'IK_Arm_L', w=1)
cmds.poleVectorConstraint('PoleVector_Arm_R', 'IK_Arm_R', w=1)
cmds.parent('PoleVector_Arm_L', 'Ctrl_01')
cmds.parent('PoleVector_Arm_R', 'Ctrl_01')


# 5-Parent Second pass


#DrvJnt Wrist to Bind hand L

cmds.select(clear=True)
cmds.parentConstraint('DrvJnt_Wrist_L', 'Bind_Hand_L_Offset', mo=True, sr=["x","y","z"])


#DrvJnt Wrist to Bind hand R

cmds.select(clear=True)
cmds.parentConstraint('DrvJnt_Wrist_R', 'Bind_Hand_R_Offset', mo=True, sr=["x","y","z"])


#Bind Hand L to Ctrl_Finger_L

cmds.select(clear=True)
cmds.parentConstraint('Bind_Hand_L_Offset', 'Ctrl_Fingers_L', mo=True)


#Bind Hand R to Ctrl_Finger_R

cmds.select(clear=True)
cmds.parentConstraint('Bind_Hand_R_Offset', 'Ctrl_Fingers_R', mo=True)


#CTRL Arm and CTRL_Wrist to bind hand offset L

cmds.select(clear=True)
cmds.parentConstraint('CTRL_Arm_L', 'Bind_Hand_L_Offset', mo=True, st=["x","y","z"])
cmds.parentConstraint('CTRL_Wrist_L', 'Bind_Hand_L_Offset', mo=True, st=["x","y","z"])


#CTRL Arm and CTRL_Wrist to bind hand offset R

cmds.select(clear=True)
cmds.parentConstraint('CTRL_Arm_R', 'Bind_Hand_R_Offset', mo=True, st=["x","y","z"])
cmds.parentConstraint('CTRL_Wrist_R', 'Bind_Hand_R_Offset', mo=True, st=["x","y","z"])


#Range ta chambre

cmds.parent('IK_Arm_L', 'IKs_01')
cmds.parent('IK_Arm_R', 'IKs_01')



# 6-La partie qui casse un peu les couilles

#Stretchy Arm L

#Create Nodes

DistBetween  = cmds.shadingNode('distanceBetween', asUtility=True, n='Dist_Stretchy_IK_Arm_L')
GlobalMult = cmds.shadingNode('multiplyDivide', asUtility=True, n='Global_Relative_Scale_Arm_L_Mult')
StretchyArmDiv = cmds.shadingNode('multiplyDivide', asUtility=True, n='Stretchy_IK_Arm_L_Div')
CondStretchy = cmds.shadingNode('condition', asUtility=True, n='Cond_Stretchy_IK_Arm_L')
CondEnable = cmds.shadingNode('condition', asUtility=True, n='Cond_Enable_Stretchy_IK_Arm_L')

#Connect Nodes

cmds.pointConstraint('CTRL_Shoulder_L_Master', 'Loc_Pl_Shoulder_L')
cmds.pointConstraint('CTRL_Arm_L_Master', 'Loc_Pl_Wrist_L')
cmds.connectAttr('Loc_Pl_Shoulder_L.translate', DistBetween+'.point1')
cmds.connectAttr('Loc_Pl_Wrist_L.translate', DistBetween+'.point2')

x=cmds.getAttr(DistBetween+'.distance')
cmds.setAttr(GlobalMult+'.input1X',x)
cmds.connectAttr('GlobalMove_01.scaleY', GlobalMult+'.input2X')

cmds.connectAttr(DistBetween+'.distance', StretchyArmDiv+'.input1X')
cmds.connectAttr(GlobalMult+'.outputX', StretchyArmDiv+'.input2X')

cmds.connectAttr(DistBetween+'.distance', CondStretchy+'.firstTerm')
cmds.connectAttr(GlobalMult+'.outputX', CondStretchy+'.secondTerm')
cmds.connectAttr(StretchyArmDiv+'.outputX', CondStretchy+'.colorIfTrueR')

cmds.connectAttr(CondStretchy+'.outColorR', CondEnable+'.colorIfTrueR')
cmds.connectAttr('CTRL_Switch_L.Stretchy_L_Arm', CondEnable+'.firstTerm') 

cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Shoulder_L.scaleX')
cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Elbow_L.scaleX')

cmds.setAttr(GlobalMult+'.operation',1)
cmds.setAttr(StretchyArmDiv+'.operation',2)
cmds.setAttr(CondStretchy+'.operation',2)
cmds.setAttr(CondEnable+'.operation',3)
cmds.setAttr(CondEnable+'.secondTerm',1)



#Switch IK/FK L

#Create Nodes

RevRotWrist = cmds.shadingNode('reverse', asUtility=True, n='Reverse_Rot_DrvJnt_Wrist_L')
RevRotElbow = cmds.shadingNode('multiplyDivide', asUtility=True, n='multiplyDivide_Rotate_Elbow_L')
RevRotShoulder = cmds.shadingNode('multiplyDivide', asUtility=True, n='multiplyDivide_DrivJnt_Shoulder_L')

SetRSwitch = cmds.shadingNode('setRange', asUtility=True, n='setR_Switch_FK_Arm_L')
SetRReverseValue = cmds.shadingNode('setRange', asUtility=True, n='setR_Reverse_Values_Arm_L')

PBElbow = cmds.shadingNode('pairBlend', asUtility=True, n='PB_Switch_FK_Elbow_L')
PBShoulder = cmds.shadingNode('pairBlend', asUtility=True, n='PB_Switch_FK_Shoulder_L')

SetRikBlend = cmds.shadingNode('setRange', asUtility=True, n='SetRange_IK_Blend_L')
PMAikBlend = cmds.shadingNode('plusMinusAverage', asUtility=True, n='PMA_IK_Blend_L')

cmds.setAttr(PMAikBlend+'.operation',1)


#Connect Nodes

cmds.connectAttr('CTRL_Elbow_L.rotate', PBElbow+'.inRotate1')
cmds.connectAttr('CTRL_Switch_L.IK_FK_L_Arm', SetRSwitch+'.valueX')
cmds.connectAttr(PBElbow+'.outRotate', 'DrvJnt_Elbow_L.rotate')
cmds.setAttr(SetRSwitch+'.minX', 1)
cmds.setAttr(SetRSwitch+'.oldMaxX', 1)
cmds.connectAttr(SetRSwitch+'.outValueX', PBElbow+'.weight')

cmds.connectAttr('CTRL_Shoulder_L.rotate', PBShoulder+'.inRotate1')
cmds.connectAttr(PBShoulder+'.outRotate', 'DrvJnt_Shoulder_L.rotate')
cmds.connectAttr(SetRSwitch+'.outValueX', PBShoulder+'.weight')

cmds.connectAttr(SetRSwitch+'.outValueX', PMAikBlend+'.input1D[0]')
cmds.connectAttr('CTRL_Switch_L.IK_FK_L_Blend', PMAikBlend+'.input1D[1]')
cmds.connectAttr(PMAikBlend+'.output1D', 'IK_Arm_L.ikBlend')

cmds.connectAttr(SetRSwitch+'.outValueX', 'CTRL_Arm_L.visibility')
cmds.connectAttr(SetRSwitch+'.outValueX', 'PoleVector_Arm_L.visibility')
cmds.connectAttr('CTRL_Switch_L.IK_FK_L_Arm', 'CTRL_Shoulder_L.visibility')
cmds.connectAttr('CTRL_Switch_L.IK_FK_L_Arm', 'CTRL_Wrist_L.visibility')
cmds.connectAttr('CTRL_Switch_L.IK_FK_L_Arm', 'CTRL_Elbow_L.visibility')
cmds.connectAttr('CTRL_Switch_L.IK_FK_L_Arm', 'CTRL_Shoulder_L_Offset_parentConstraint1.Bind_Clavicle_End_LW0')
cmds.connectAttr(SetRSwitch+'.outValueX', 'Bind_Hand_L_Offset_parentConstraint2.CTRL_Arm_LW0')



# 6-La partie qui casse un peu les couilles (other side)


#Stretchy Arm R

#Create Nodes

DistBetween  = cmds.shadingNode('distanceBetween', asUtility=True, n='Dist_Stretchy_IK_Arm_R')
GlobalMult = cmds.shadingNode('multiplyDivide', asUtility=True, n='Global_Relative_Scale_Arm_R_Mult')
StretchyArmDiv = cmds.shadingNode('multiplyDivide', asUtility=True, n='Stretchy_IK_Arm_R_Div')
CondStretchy = cmds.shadingNode('condition', asUtility=True, n='Cond_Stretchy_IK_Arm_R')
CondEnable = cmds.shadingNode('condition', asUtility=True, n='Cond_Enable_Stretchy_IK_Arm_R')

#Connect Nodes

cmds.pointConstraint('CTRL_Shoulder_R_Master', 'Loc_Pl_Shoulder_R')
cmds.pointConstraint('CTRL_Arm_R_Master', 'Loc_Pl_Wrist_R')
cmds.connectAttr('Loc_Pl_Shoulder_R.translate', DistBetween+'.point1')
cmds.connectAttr('Loc_Pl_Wrist_R.translate', DistBetween+'.point2')

x= cmds.getAttr(DistBetween+'.distance')
cmds.setAttr(GlobalMult+'.input1X', x)
cmds.connectAttr('GlobalMove_01.scaleY', GlobalMult+'.input2X')

cmds.connectAttr(DistBetween+'.distance', StretchyArmDiv+'.input1X')
cmds.connectAttr(GlobalMult+'.outputX', StretchyArmDiv+'.input2X')

cmds.connectAttr(DistBetween+'.distance', CondStretchy+'.firstTerm')
cmds.connectAttr(GlobalMult+'.outputX', CondStretchy+'.secondTerm')
cmds.connectAttr(StretchyArmDiv+'.outputX', CondStretchy+'.colorIfTrueR')

cmds.connectAttr(CondStretchy+'.outColorR', CondEnable+'.colorIfTrueR')
cmds.connectAttr('CTRL_Switch_R.Stretchy_R_Arm', CondEnable+'.firstTerm') 

cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Shoulder_R.scaleX')
cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Elbow_R.scaleX')

cmds.setAttr(GlobalMult+'.operation',1)
cmds.setAttr(StretchyArmDiv+'.operation',2)
cmds.setAttr(CondStretchy+'.operation',2)
cmds.setAttr(CondEnable+'.operation',3)
cmds.setAttr(CondEnable+'.secondTerm',1)



#Switch IK/FK R

#Create Nodes

RevRotWrist = cmds.shadingNode('reverse', asUtility=True, n='Reverse_Rot_DrvJnt_Wrist_R')
RevRotElbow = cmds.shadingNode('multiplyDivide', asUtility=True, n='multiplyDivide_Rotate_Elbow_R')
RevRotShoulder = cmds.shadingNode('multiplyDivide', asUtility=True, n='multiplyDivide_DrivJnt_Shoulder_R')

SetRSwitch = cmds.shadingNode('setRange', asUtility=True, n='setR_Switch_FK_Arm_R')
SetRReverseValue = cmds.shadingNode('setRange', asUtility=True, n='setR_Reverse_Values_Arm_R')

PBElbow = cmds.shadingNode('pairBlend', asUtility=True, n='PB_Switch_FK_Elbow_R')
PBShoulder = cmds.shadingNode('pairBlend', asUtility=True, n='PB_Switch_FK_Shoulder_R')

SetRikBlend = cmds.shadingNode('setRange', asUtility=True, n='SetRange_IK_Blend_R')
PMAikBlend = cmds.shadingNode('plusMinusAverage', asUtility=True, n='PMA_IK_Blend_R')

cmds.setAttr(PMAikBlend+'.operation',1)


#Connect Nodes

cmds.connectAttr('CTRL_Elbow_R.rotate', PBElbow+'.inRotate1')
cmds.connectAttr('CTRL_Switch_R.IK_FK_R_Arm', SetRSwitch+'.valueX')
cmds.connectAttr(PBElbow+'.outRotate', 'DrvJnt_Elbow_R.rotate')
cmds.setAttr(SetRSwitch+'.minX', 1)
cmds.setAttr(SetRSwitch+'.oldMaxX', 1)
cmds.connectAttr(SetRSwitch+'.outValueX', PBElbow+'.weight')

cmds.connectAttr('CTRL_Shoulder_R.rotate', PBShoulder+'.inRotate1')
cmds.connectAttr(PBShoulder+'.outRotate', 'DrvJnt_Shoulder_R.rotate')
cmds.connectAttr(SetRSwitch+'.outValueX', PBShoulder+'.weight')

cmds.connectAttr(SetRSwitch+'.outValueX', PMAikBlend+'.input1D[0]')
cmds.connectAttr('CTRL_Switch_R.IK_FK_R_Blend', PMAikBlend+'.input1D[1]')
cmds.connectAttr(PMAikBlend+'.output1D', 'IK_Arm_R.ikBlend')

cmds.connectAttr(SetRSwitch+'.outValueX', 'CTRL_Arm_R.visibility')
cmds.connectAttr(SetRSwitch+'.outValueX', 'PoleVector_Arm_R.visibility')
cmds.connectAttr('CTRL_Switch_R.IK_FK_R_Arm', 'CTRL_Shoulder_R.visibility')
cmds.connectAttr('CTRL_Switch_R.IK_FK_R_Arm', 'CTRL_Wrist_R.visibility')
cmds.connectAttr('CTRL_Switch_R.IK_FK_R_Arm', 'CTRL_Shoulder_R_Offset_parentConstraint1.Bind_Clavicle_End_RW0')
cmds.connectAttr('CTRL_Switch_R.IK_FK_R_Arm', 'CTRL_Elbow_R.visibility')
cmds.connectAttr(SetRSwitch+'.outValueX', 'Bind_Hand_R_Offset_parentConstraint2.CTRL_Arm_RW0')



#CTRL Arm Follow

cmds.parentConstraint('CTRL_Shoulders_Master', 'CTRL_Arm_L_Move_01', mo=True)
cmds.parentConstraint('CTRL_Root_Master', 'CTRL_Arm_L_Move_01', mo=True)
cmds.parentConstraint('CTRL_Shoulders_Master', 'CTRL_Arm_R_Move_01', mo=True)
cmds.parentConstraint('CTRL_Root_Master', 'CTRL_Arm_R_Move_01', mo=True)

CondChestL = cmds.shadingNode('condition', asUtility=True, n='Cond_Follow_Chest_Arm_L')
CondRootL = cmds.shadingNode('condition', asUtility=True, n='Cond_Follow_Root_Arm_L')
cmds.setAttr(CondChestL+'.secondTerm', 1)
cmds.setAttr(CondRootL+'.secondTerm', 2)
cmds.setAttr(CondChestL+'.colorIfTrueR', 1)
cmds.setAttr(CondRootL+'.colorIfTrueR', 1)
cmds.setAttr(CondChestL+'.colorIfFalseR', 0)
cmds.setAttr(CondRootL+'.colorIfFalseR', 0)
cmds.connectAttr('CTRL_Arm_L.Follow_Arm_L', CondChestL+'.firstTerm')
cmds.connectAttr('CTRL_Arm_L.Follow_Arm_L', CondRootL+'.firstTerm')
cmds.connectAttr(CondChestL+'.outColorR', 'CTRL_Arm_L_Move_01_parentConstraint1.CTRL_Shoulders_MasterW0')
cmds.connectAttr(CondRootL+'.outColorR', 'CTRL_Arm_L_Move_01_parentConstraint1.CTRL_Root_MasterW1')

CondChestR = cmds.shadingNode('condition', asUtility=True, n='Cond_Follow_Chest_Arm_R')
CondRootR = cmds.shadingNode('condition', asUtility=True, n='Cond_Follow_Root_Arm_R')
cmds.setAttr(CondChestR+'.secondTerm', 1)
cmds.setAttr(CondRootR+'.secondTerm', 2)
cmds.setAttr(CondChestR+'.colorIfTrueR', 1)
cmds.setAttr(CondRootR+'.colorIfTrueR', 1)
cmds.setAttr(CondChestR+'.colorIfFalseR', 0)
cmds.setAttr(CondRootR+'.colorIfFalseR', 0)
cmds.connectAttr('CTRL_Arm_R.Follow_Arm_R', CondChestR+'.firstTerm')
cmds.connectAttr('CTRL_Arm_R.Follow_Arm_R', CondRootR+'.firstTerm')
cmds.connectAttr(CondChestR+'.outColorR', 'CTRL_Arm_R_Move_01_parentConstraint1.CTRL_Shoulders_MasterW0')
cmds.connectAttr(CondRootR+'.outColorR', 'CTRL_Arm_R_Move_01_parentConstraint1.CTRL_Root_MasterW1')



#CTRL_Arm_Twist

cmds.connectAttr('CTRL_Arm_L.Twist_Arm_L', 'IK_Arm_L.twist')
cmds.connectAttr('CTRL_Arm_R.Twist_Arm_R', 'IK_Arm_R.twist')
