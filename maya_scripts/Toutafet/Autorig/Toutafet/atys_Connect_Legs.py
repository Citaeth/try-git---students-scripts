import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math


#___________________Connect Attributs____________________:     

def connectAttributs (*args):

    radc = cmds.radioCollection(rc, q = True, sl= True)
    
    if radc == 'right' :
        side = '_R'
    if radc == 'left' :
        side = '_L'

    
    #1-Create CTRL_Switch

    cmds.circle(r=5,n ='CTRL_Switch_Leg'+side)
    cmds.matchTransform('CTRL_Switch_Leg'+side, 'DrvJnt_Knee'+side)

    cmds.select(clear=True)
    cmds.select('CTRL_Switch_Leg'+side)
    cmds.makeIdentity( apply=True) 

    #Set_Up CTRL_Switch

    # 1-Premier separateur

    cmds.addAttr('CTRL_Switch_Leg'+side, longName='_______', attributeType='enum', enumName='____')
    cmds.setAttr('CTRL_Switch_Leg'+side+'._______', channelBox=True )
    cmds.setAttr('CTRL_Switch_Leg'+side+'._______', keyable=True )


    # 2-IK/FK

    cmds.addAttr('CTRL_Switch_Leg'+side, longName='IK_FK'+side+'_Leg', attributeType='enum', enumName='IK:FK')
    cmds.setAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg', channelBox=True )
    cmds.setAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg', keyable=True )


    # 3-Stretchy
    
    cmds.addAttr('CTRL_Switch_Leg'+side, longName='Stretchy'+side+'_Leg', attributeType='bool')
    cmds.setAttr('CTRL_Switch_Leg'+side+'.Stretchy'+side+'_Leg', channelBox=True )
    cmds.setAttr('CTRL_Switch_Leg'+side+'.Stretchy'+side+'_Leg', keyable=True)
    
#____Create Nodes Connect Leg____:
    cmds.ikHandle( sj='DrvJnt_Leg'+side, ee='DrvJnt_Ankle'+side, n='IK_Leg'+side)

    cmds.parentConstraint('DrvJnt_Ankle'+side,'Bind_Feet'+side+'_Offset', mo=True)
    
    cmds.parentConstraint('CTRL_Thigh'+side,'DrvJnt_Leg'+side, mo=True)
    cmds.connectAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg','DrvJnt_Leg'+side+'_parentConstraint1'+'.CTRL_Thigh'+side+'W0')
    cmds.parentConstraint('CTRL_Knee'+side,'DrvJnt_Knee'+side, mo=True)
    cmds.connectAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg','DrvJnt_Knee'+side+'_parentConstraint1'+'.CTRL_Knee'+side+'W0')
    cmds.parentConstraint('CTRL_Ankle'+side,'DrvJnt_Ankle'+side, mo=True)
    cmds.connectAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg','DrvJnt_Ankle'+side+'_parentConstraint1'+'.CTRL_Ankle'+side+'W0')
    cmds.parent('IK_Leg'+side,'IKs_01')
    cmds.parent('CTRL_Switch_Leg'+side,'Ctrl_01')
    cmds.circle(n='PoleVector_Leg'+side)
    cmds.matchTransform('PoleVector_Leg'+side,'DrvJnt_Knee'+side)
    cmds.xform( r=True, t=(0, 0, 10) )
    cmds.makeIdentity('PoleVector_Leg'+side, apply=True, t=1, r=1, s=1, n=2 )
    cmds.poleVectorConstraint('PoleVector_Leg'+side,'IK_Leg'+side, w=1)
    cmds.parent('PoleVector_Leg'+side, 'Ctrl_01')

    
#____Create Nodes Attributs Foot____:
    cmds.parent('Loc_Pl_Bank_Ext'+side,'Loc_Pl_Bank_Int'+side)
    cmds.parent('Loc_Pl_Ball'+side,'Loc_Pl_Bank_Ext'+side)
    cmds.parent('Loc_Pl_Toes'+side,'Loc_Pl_Ball'+side)
    cmds.parent('Loc_Pl_Heel'+side,'Loc_Pl_Toes'+side)
    
    cmds.createNode("transform", n='Pivot_Ball'+side)
    cmds.createNode("transform", n='Pivot_Toe'+side)
    cmds.matchTransform('Pivot_Ball'+side,'Loc_Pl_Ball'+side)
    cmds.makeIdentity('Pivot_Ball'+side, apply=True, t=1, r=1, s=1, n=2 )
    cmds.matchTransform('Pivot_Toe'+side,'Loc_Pl_Ball'+side)
    cmds.makeIdentity('Pivot_Toe'+side, apply=True, t=1, r=1, s=1, n=2 )
    
    cmds.ikHandle( sj='Bind_Feet'+side, ee='Bind_Ball'+side, n='IK_Ball'+side)
    cmds.ikHandle( sj='Bind_Ball'+side, ee='Bind_Toes'+side, n='IK_Toe'+side )
        
    cmds.parent('Pivot_Ball'+side, 'Loc_Pl_Heel'+side)
    cmds.createNode('transform', n='Pivot_Toe'+side+'_Offset')
    cmds.matchTransform('Pivot_Toe'+side+'_Offset','Pivot_Toe'+side)
    cmds.parent('Pivot_Toe'+side, 'Pivot_Toe'+side+'_Offset')
    cmds.parent('Pivot_Toe'+side+'_Offset','Loc_Pl_Heel'+side)
    cmds.parent('IK_Toe'+side,'Pivot_Toe'+side)
    cmds.parent('IK_Ball'+side,'Loc_Pl_Heel'+side)
    cmds.parent('Loc_Pl_Bank_Int'+side,'CTRL_Leg'+side)
    
    
    #____Creation Nodes Bank______:
    CondBankInt = cmds.shadingNode('condition', asUtility=True, n='Cond_Bank_Int'+side)
    CondBankExt = cmds.shadingNode('condition', asUtility=True, n='Cond_Bank_Ext'+side)   
    #____Creation Nodes Flex Toe__:
    SetRFlexFalse = cmds.shadingNode('setRange', asUtility=True, n='SetR_FlexToe_False'+side)
    SetRFlexTrue = cmds.shadingNode('setRange', asUtility=True, n='SetR_FlexToe_True'+side)
    CondFlexToe = cmds.shadingNode('condition', asUtility=True, n='Cond_Flex_Toe'+side) 
    MultFlexToe= cmds.createNode('multiplyDivide', n='Flex_Toe'+side+'_Mult') 

    
    #____Creation Nodes Foot Rool_:
    SetRFootRoll_Heel = cmds.shadingNode('setRange', asUtility=True, n='SetR_Foot_Roll_Heel'+side)
    SetRFootRoll_Ball_T = cmds.shadingNode('setRange', asUtility=True, n='SetR_Foot_Roll_Ball_True'+side)
    SetRFootRoll_Ball_F = cmds.shadingNode('setRange', asUtility=True, n='SetR_Foot_Roll_Ball_False'+side)
    SetRFootRoll_Toe = cmds.shadingNode('setRange', asUtility=True, n='setR_Foot_Roll_Toe'+side)
    CondFootRoll_Heel = cmds.shadingNode('condition', asUtility=True, n='Cond_Foot_Roll_Heel'+side)
    CondFootRoll_Ball = cmds.shadingNode('condition', asUtility=True, n='Cond_Foot_Roll_Ball'+side)
    CondFootRoll_Toe = cmds.shadingNode('condition', asUtility=True, n='Cond_Foot_Roll_Toe'+side)
    #____Creation Nodes Twist Hell:
    SetRTwist_Heel_F = cmds.shadingNode('setRange', asUtility=True, n='SetR_Twist_Heel_False'+side)    
    SetRTwist_Heel_T = cmds.shadingNode('setRange', asUtility=True, n='SetR_Twist_Heel_True'+side)    
    CondTwistHeel = cmds.shadingNode('condition', asUtility=True, n='Cond_Twist_Heel'+side)
    
    
    #____Creation Nodes Twist Toe_:
    SetRTwist_Toe_F = cmds.shadingNode('setRange', asUtility=True, n='SetR_Twist_Toe_False'+side)    
    SetRTwist_Toe_T = cmds.shadingNode('setRange', asUtility=True, n='SetR_Twist_Toe_True'+side)    
    CondTwistToe = cmds.shadingNode('condition', asUtility=True, n='Cond_Twist_Toe'+side)
    
   
    #____Connect Nodes Bank_______:
    if side == '_R':
        cmds.setAttr (CondBankInt+'.operation', 5)
        cmds.setAttr (CondBankExt+'.operation', 3)
    if side == '_L':
        cmds.setAttr (CondBankInt+'.operation', 3)
        cmds.setAttr (CondBankExt+'.operation', 5)
        
    cmds.connectAttr('CTRL_Leg'+side+'.Bank'+side, CondBankInt+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Bank'+side, CondBankInt+'.colorIfTrueR')
    cmds.connectAttr(CondBankInt+'.outColorR', 'Loc_Pl_Bank_Int'+side+'.rotateZ')
    cmds.connectAttr('CTRL_Leg'+side+'.Bank'+side, CondBankExt+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Bank'+side, CondBankExt+'.colorIfTrueR')
    cmds.connectAttr(CondBankExt+'.outColorR', 'Loc_Pl_Bank_Ext'+side+'.rotateZ')
    
    #____Connect Nodes Flex Toe___:
    if side == '_R':
        cmds.setAttr (CondFlexToe+'.operation', 3)
        cmds.setAttr (SetRFlexFalse+'.minX', -30)
        cmds.setAttr (SetRFlexFalse+'.oldMinX', -1)
        cmds.setAttr (SetRFlexTrue+'.maxX', 30)
        cmds.setAttr (SetRFlexTrue+'.oldMaxX', 1)
    if side == '_L':
        cmds.setAttr (CondFlexToe+'.operation', 3)
        cmds.setAttr (SetRFlexFalse+'.minX', -30)
        cmds.setAttr (SetRFlexFalse+'.oldMinX', -1)
        cmds.setAttr (SetRFlexTrue+'.maxX', 30)
        cmds.setAttr (SetRFlexTrue+'.oldMaxX', 1)
    
    cmds.connectAttr('CTRL_Leg'+side+'.Flex_Toe'+side, CondFlexToe+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Flex_Toe'+side, SetRFlexFalse+'.valueX')
    cmds.connectAttr('CTRL_Leg'+side+'.Flex_Toe'+side, SetRFlexTrue+'.valueX')
    cmds.connectAttr(SetRFlexFalse+'.outValueX', CondFlexToe+'.colorIfFalseR')
    cmds.connectAttr(SetRFlexTrue+'.outValueX', CondFlexToe+'.colorIfTrueR')
    cmds.connectAttr(CondFlexToe+'.outColorR',MultFlexToe+'.input1X')
    cmds.setAttr(MultFlexToe+'.input2X', -1)
    cmds.connectAttr(MultFlexToe+'.outputX','Pivot_Toe'+side+'.rotateX')
    
    #____Connect Nodes Foot Roll__:
    if side == '_R':
        cmds.setAttr (SetRFootRoll_Heel+'.minX', -25)
        cmds.setAttr (SetRFootRoll_Heel+'.oldMinX', -1)
        cmds.setAttr (SetRFootRoll_Toe+'.maxX', 70)
        cmds.setAttr (SetRFootRoll_Toe+'.oldMaxX', 1)
        cmds.setAttr (SetRFootRoll_Toe+'.oldMinX', 0.5)
        cmds.setAttr (SetRFootRoll_Ball_F+'.minX', 50)
        cmds.setAttr (SetRFootRoll_Ball_F+'.oldMinX', 0.5)
        cmds.setAttr (SetRFootRoll_Ball_F+'.oldMaxX', 1)
        cmds.setAttr (SetRFootRoll_Ball_T+'.maxX', 50)
        cmds.setAttr (SetRFootRoll_Ball_T+'.oldMaxX', 0.5)
        cmds.setAttr (CondFootRoll_Heel+'.operation', 4)
        cmds.setAttr (CondFootRoll_Ball+'.operation', 5)
        cmds.setAttr (CondFootRoll_Toe+'.operation', 2)
    if side == '_L':
        cmds.setAttr (SetRFootRoll_Heel+'.minX', -25)
        cmds.setAttr (SetRFootRoll_Heel+'.oldMinX', -1)
        cmds.setAttr (SetRFootRoll_Toe+'.maxX', 70)
        cmds.setAttr (SetRFootRoll_Toe+'.oldMaxX', 1)
        cmds.setAttr (SetRFootRoll_Toe+'.oldMinX', 0.5)
        cmds.setAttr (SetRFootRoll_Ball_F+'.minX', 50)
        cmds.setAttr (SetRFootRoll_Ball_F+'.oldMinX', 0.5)
        cmds.setAttr (SetRFootRoll_Ball_F+'.oldMaxX', 1)
        cmds.setAttr (SetRFootRoll_Ball_T+'.maxX', 50)
        cmds.setAttr (SetRFootRoll_Ball_T+'.oldMaxX', 0.5)
        cmds.setAttr (CondFootRoll_Heel+'.operation', 4)
        cmds.setAttr (CondFootRoll_Ball+'.operation', 5)
        cmds.setAttr (CondFootRoll_Toe+'.operation', 2)        
    
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, CondFootRoll_Heel+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, CondFootRoll_Ball+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, CondFootRoll_Toe+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, SetRFootRoll_Heel+'.valueX')
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, SetRFootRoll_Ball_F+'.valueX')
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, SetRFootRoll_Ball_T+'.valueX')
    cmds.connectAttr('CTRL_Leg'+side+'.Foot_Roll'+side, SetRFootRoll_Toe+'.valueX')
    cmds.connectAttr(SetRFootRoll_Heel+'.outValueX', CondFootRoll_Heel+'.colorIfTrueR')
    cmds.connectAttr(SetRFootRoll_Ball_F+'.outValueX', CondFootRoll_Ball+'.colorIfFalseR')
    cmds.connectAttr(SetRFootRoll_Ball_T+'.outValueX', CondFootRoll_Ball+'.colorIfTrueR')
    cmds.connectAttr(SetRFootRoll_Toe+'.outValueX', CondFootRoll_Toe+'.colorIfTrueR')
    cmds.connectAttr(CondFootRoll_Ball+'.outColorR', 'Pivot_Ball'+side+'.rotateX')
    cmds.connectAttr(CondFootRoll_Heel+'.outColorR', 'Loc_Pl_Heel'+side+'.rotateX')
    cmds.connectAttr(CondFootRoll_Toe+'.outColorR', 'Loc_Pl_Toes'+side+'.rotateX')
    cmds.parentConstraint('Pivot_Ball'+side,'IK_Leg'+side, mo=True)
    
    #____Conect Nodes Twist Hell__:
    if side == '_R':
        cmds.setAttr (SetRTwist_Heel_T+'.maxX', 60)
        cmds.setAttr (SetRTwist_Heel_T+'.oldMaxX', 1)
        cmds.setAttr (SetRTwist_Heel_F+'.minX', -20)
        cmds.setAttr (SetRTwist_Heel_F+'.oldMinX', -1)
        cmds.setAttr (CondTwistHeel+'.operation', 3)
        ReverseTwistHeelR= cmds.createNode('multiplyDivide', n='Reverse_Twist_Heel'+side+'_Mult')
        cmds.setAttr (ReverseTwistHeelR+'.input2X', -1)
        cmds.connectAttr('Cond_Twist_Heel'+side+'.outColorR',ReverseTwistHeelR+'.input1X')
        cmds.connectAttr(ReverseTwistHeelR+'.outputX','Loc_Pl_Heel'+side+'.rotateY')
        
        
    if side == '_L':
        cmds.setAttr (SetRTwist_Heel_T+'.maxX', 60)
        cmds.setAttr (SetRTwist_Heel_T+'.oldMaxX', 1)
        cmds.setAttr (SetRTwist_Heel_F+'.minX', -20)
        cmds.setAttr (SetRTwist_Heel_F+'.oldMinX', -1)
        cmds.setAttr (CondTwistHeel+'.operation', 3)
        cmds.connectAttr(CondTwistHeel+'.outColorR', 'Loc_Pl_Heel'+side+'.rotateY')
        
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Heel'+side, CondTwistHeel+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Heel'+side, SetRTwist_Heel_T+'.valueX')
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Heel'+side, SetRTwist_Heel_F+'.valueX')
    cmds.connectAttr(SetRTwist_Heel_T+'.outValueX', CondTwistHeel+'.colorIfTrueR')
    cmds.connectAttr(SetRTwist_Heel_F+'.outValueX', CondTwistHeel+'.colorIfFalseR')

 
    #____Connect Nodes Twist Toe__:
    if side == '_R':
        cmds.setAttr (SetRTwist_Toe_T+'.maxX', 30)
        cmds.setAttr (SetRTwist_Toe_T+'.oldMaxX', 1)
        cmds.setAttr (SetRTwist_Toe_F+'.minX', -30)
        cmds.setAttr (SetRTwist_Toe_F+'.oldMinX', -1)
        cmds.setAttr (CondTwistToe+'.operation', 3)
    if side == '_L':
        cmds.setAttr (SetRTwist_Toe_T+'.maxX', 30)
        cmds.setAttr (SetRTwist_Toe_T+'.oldMaxX', 1)
        cmds.setAttr (SetRTwist_Toe_F+'.minX', -30)
        cmds.setAttr (SetRTwist_Toe_F+'.oldMinX', -1)
        cmds.setAttr (CondTwistToe+'.operation', 3)
      
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Toe'+side, CondTwistToe+'.firstTerm')
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Toe'+side, SetRTwist_Toe_T+'.valueX')
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Toe'+side, SetRTwist_Toe_F+'.valueX')
    cmds.connectAttr(SetRTwist_Toe_T+'.outValueX', CondTwistToe+'.colorIfTrueR')
    cmds.connectAttr(SetRTwist_Toe_F+'.outValueX', CondTwistToe+'.colorIfFalseR')
    cmds.connectAttr(CondTwistToe+'.outColorR', 'Loc_Pl_Toes'+side+'.rotateY')
    
    
#____Ctrl FK Toe____:
    cmds.matchTransform('CTRL_Toe'+side+'_Offset','Bind_Ball'+side)
    cmds.parentConstraint('CTRL_Ankle'+side,'CTRL_Toe'+side+'_Offset', mo=True)
    cmds.group('Bind_Ball'+side,n='Bind_Ball'+side+'_Offset')
    cmds.parentConstraint('CTRL_Toe'+side, 'Bind_Ball'+side+'_Offset', mo=True)
    cmds.connectAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg','Bind_Ball'+side+'_Offset_parentConstraint1.CTRL_Toe'+side+'W0')
    
#____Visibility IF/FK____:

    cmds.connectAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg','CTRL_Thigh'+side+'.visibility')
    cmds.connectAttr('CTRL_Switch_Leg'+side+'.IK_FK'+side+'_Leg','CTRL_Toe'+side+'.visibility')

    cmds.createNode('setRange', n='SetR_Reverse_Switch_IK_Leg')
    cmds.setAttr('SetR_Reverse_Switch_IK_Leg'+'.minX', 1)
    cmds.setAttr('SetR_Reverse_Switch_IK_Leg'+'.minY', 1)
    cmds.setAttr('SetR_Reverse_Switch_IK_Leg'+'.oldMaxX', 1)
    cmds.setAttr('SetR_Reverse_Switch_IK_Leg'+'.oldMaxY', 1)
    
    if side == '_L':
        cmds.connectAttr('CTRL_Switch_Leg_L.IK_FK_L_Leg','SetR_Reverse_Switch_IK_Leg.valueX')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueX','IK_Leg_L.ikBlend')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueX','IK_Ball_L.ikBlend')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueX','IK_Toe_L.ikBlend')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueX','CTRL_Leg_L.visibility')
        
    if side=='_R':
        cmds.connectAttr('CTRL_Switch_Leg_R.IK_FK_R_Leg','SetR_Reverse_Switch_IK_Leg.valueY')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueY','IK_Leg_R.ikBlend')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueY','IK_Ball_R.ikBlend')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueY','IK_Toe_R.ikBlend')
        cmds.connectAttr('SetR_Reverse_Switch_IK_Leg'+'.outValueY','CTRL_Leg_R.visibility')
    
#____Stretchy Legs____:
    
    #Stretchy Leg L
    if side=='_L':
#Create Nodes

        DistBetween  = cmds.shadingNode('distanceBetween', asUtility=True, n='Dist_Stretchy_IK_Leg_L')
        GlobalMult = cmds.shadingNode('multiplyDivide', asUtility=True, n='Global_Relative_Scale_Leg_L_Mult')
        StretchyLegDiv = cmds.shadingNode('multiplyDivide', asUtility=True, n='Stretchy_IK_Leg_L_Div')
        CondStretchy = cmds.shadingNode('condition', asUtility=True, n='Cond_Stretchy_IK_Leg_L')
        CondEnable = cmds.shadingNode('condition', asUtility=True, n='Cond_Enable_Stretchy_IK_Leg_L')

    #Connect Nodes

        cmds.createNode('transform',n='CTRL_Leg_L_Master')
        cmds.parent('CTRL_Leg_L_Master','CTRL_Leg_L')
        cmds.matchTransform('CTRL_Leg_L_Master','CTRL_Leg_L')
        cmds.makeIdentity('CTRL_Leg_L_Master', apply=True, t=1, r=1, s=1, n=2 )
        cmds.pointConstraint('CTRL_Thigh_L_Master', 'Loc_Pl_Leg_L')
        cmds.pointConstraint('CTRL_Leg_L_Master', 'Loc_Pl_Ankle_L')
        cmds.connectAttr('Loc_Pl_Leg_L.translate', DistBetween+'.point1')
        cmds.connectAttr('Loc_Pl_Ankle_L.translate', DistBetween+'.point2')

        x=cmds.getAttr(DistBetween+'.distance')
        cmds.setAttr(GlobalMult+'.input1X',x)
        cmds.connectAttr('GlobalMove_01.scaleY', GlobalMult+'.input2X')

        cmds.connectAttr(DistBetween+'.distance', StretchyLegDiv+'.input1X')
        cmds.connectAttr(GlobalMult+'.outputX', StretchyLegDiv+'.input2X')

        cmds.connectAttr(DistBetween+'.distance', CondStretchy+'.firstTerm')
        cmds.connectAttr(GlobalMult+'.outputX', CondStretchy+'.secondTerm')
        cmds.connectAttr(StretchyLegDiv+'.outputX', CondStretchy+'.colorIfTrueR')

        cmds.connectAttr(CondStretchy+'.outColorR', CondEnable+'.colorIfTrueR')
        cmds.connectAttr('CTRL_Switch_Leg_L.Stretchy_L_Leg', CondEnable+'.firstTerm') 

        cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Leg_L.scaleX')
        cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Knee_L.scaleX')

        cmds.setAttr(GlobalMult+'.operation',1)
        cmds.setAttr(StretchyLegDiv+'.operation',2)
        cmds.setAttr(CondStretchy+'.operation',2)
        cmds.setAttr(CondEnable+'.operation',3)
        cmds.setAttr(CondEnable+'.secondTerm',1)


    #Stretchy Leg R
    if side=='_R':
#Create Nodes

        DistBetween  = cmds.shadingNode('distanceBetween', asUtility=True, n='Dist_Stretchy_IK_Leg_L')
        GlobalMult = cmds.shadingNode('multiplyDivide', asUtility=True, n='Global_Relative_Scale_Leg_L_Mult')
        StretchyLegDiv = cmds.shadingNode('multiplyDivide', asUtility=True, n='Stretchy_IK_Leg_L_Div')
        CondStretchy = cmds.shadingNode('condition', asUtility=True, n='Cond_Stretchy_IK_Leg_L')
        CondEnable = cmds.shadingNode('condition', asUtility=True, n='Cond_Enable_Stretchy_IK_Leg_L')

    #Connect Nodes

        cmds.createNode('transform',n='CTRL_Leg_R_Master')
        cmds.parent('CTRL_Leg_R_Master','CTRL_Leg_R')
        cmds.matchTransform('CTRL_Leg_R_Master','CTRL_Leg_R')
        cmds.makeIdentity('CTRL_Leg_R_Master', apply=True, t=1, r=1, s=1, n=2 )
        cmds.pointConstraint('CTRL_Thigh_R_Master', 'Loc_Pl_Leg_R')
        cmds.pointConstraint('CTRL_Leg_R_Master', 'Loc_Pl_Ankle_R')
        cmds.connectAttr('Loc_Pl_Leg_R.translate', DistBetween+'.point1')
        cmds.connectAttr('Loc_Pl_Ankle_R.translate', DistBetween+'.point2')

        x=cmds.getAttr(DistBetween+'.distance')
        cmds.setAttr(GlobalMult+'.input1X',x)
        cmds.connectAttr('GlobalMove_01.scaleY', GlobalMult+'.input2X')

        cmds.connectAttr(DistBetween+'.distance', StretchyLegDiv+'.input1X')
        cmds.connectAttr(GlobalMult+'.outputX', StretchyLegDiv+'.input2X')

        cmds.connectAttr(DistBetween+'.distance', CondStretchy+'.firstTerm')
        cmds.connectAttr(GlobalMult+'.outputX', CondStretchy+'.secondTerm')
        cmds.connectAttr(StretchyLegDiv+'.outputX', CondStretchy+'.colorIfTrueR')

        cmds.connectAttr(CondStretchy+'.outColorR', CondEnable+'.colorIfTrueR')
        cmds.connectAttr('CTRL_Switch_Leg_R.Stretchy_R_Leg', CondEnable+'.firstTerm') 

        cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Leg_R.scaleX')
        cmds.connectAttr(CondEnable+'.outColorR', 'DrvJnt_Knee_R.scaleX')

        cmds.setAttr(GlobalMult+'.operation',1)
        cmds.setAttr(StretchyLegDiv+'.operation',2)
        cmds.setAttr(CondStretchy+'.operation',2)
        cmds.setAttr(CondEnable+'.operation',3)
        cmds.setAttr(CondEnable+'.secondTerm',1)
    
    cmds.connectAttr('CTRL_Leg'+side+'.Twist_Leg'+side,'IK_Leg'+side+'.twist')  
    
    #Parent_Last_Pass

    cmds.parentConstraint("Bind_Thigh_L", "Grp_FK_Leg_L", mo=True)
    cmds.parentConstraint("Bind_Thigh_R", "Grp_FK_Leg_R", mo=True)
    cmds.parentConstraint("Bind_Thigh_L", "DrvJnt_Leg_L_Offset", mo=True)
    cmds.parentConstraint("Bind_Thigh_R", "DrvJnt_Leg_R_Offset", mo=True)
    cmds.parentConstraint("CTRL_Hips_Master", "Bind_Hips_Offset", mo=True)


#window___________________________________________________________________________________________________________
    
	
window= cmds.window( t="Auto_Attribut_Foot",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 193) )
mainw = cmds.formLayout()

nm = cmds.frameLayout( label='Side?', labelAlign='center')
cmds.rowColumnLayout( p = nm, numberOfColumns=2, columnWidth=[(1, 125), (2, 125)] )

rc = cmds.radioCollection()
r = cmds.radioButton("right", label='Right', align='left', sl=1 )
l = cmds.radioButton('left', label='Left', align='right' )

eylup = cmds.frameLayout( p= nm, label="Connections", labelAlign='center' )
cmds.button(l='Connect Attributs', align='center', c=connectAttributs)





cmds.showWindow(window)