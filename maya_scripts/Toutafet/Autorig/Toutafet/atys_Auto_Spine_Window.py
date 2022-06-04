#Auto_spine
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math


"""
________________________________________________________________________________________________________________________________________
Pour Babouche

Script by Juliette Gueydan

Creation automatique de la spine a partir d'une curve
  
________________________________________________________________________________________________________________________________________
"""


#Help

def help_def (*args):
	cmds.window(title="Aled!", w = 350, h = 160, minimizeButton=False, maximizeButton=False)
	cmds.frameLayout(l="O scour!", marginHeight=10, marginWidth=10)
	cmds.setParent()
	cmds.text(("""Safekoi
	    Set up tes groupes (GlobalMove_01 / Joint_01 / Ctrl_01 / IKs_01 / ExtraNodes_01 /ExtraNodes_To_Show	/ ExtraNodes_To_Hide)
	    - Selectionne ta curve qui va te ton root aux shoulders (droite et raf des cvs)
	    - Le script va creer les chaines de joints : 
			-la bind sur laquelle va se creer une ik spline
			-la Jnt qui skinne la curve
			-et la FK et ses parent shape
	    - Creer des ctrl pour le root et les shoulders, les nommes pas et laisse les au centre du monde

	    - Selectionne Jnt_Root puis son ctrl, Jnt_Shoulders puis son ctrl"""), align="left", ww=True)
	cmds.showWindow()

def SetUp1(*args):

    #1 Create FK joints

    #Selectionner la curve

    cv=cmds.ls(sl=True)
    cmds.rename(cv, "Crv")
    cmds.select("Crv")

    #Create joints on curve
    import maya.mel as mel
    mel.eval("bonesOnCurve 3 0 0;")

    #Rename joints

    cmds.rename('joint1', 'FK_Root')
    cmds.rename('joint2', 'FK_Spine_01')
    cmds.rename('joint3', 'FK_Spine_02')
    cmds.rename('joint4', 'FK_Shoulders')
    cmds.joint("FK_Root" ,e=True,zso=True,oj="none")
    cmds.joint("FK_Spine_01" ,e=True,zso=True,oj="none")
    cmds.joint("FK_Spine_02" ,e=True,zso=True,oj="none")
    cmds.joint("FK_Shoulders" ,e=True,zso=True,oj="none")
    cmds.joint("FK_Root" ,e=True,zso=True,oj="xyz")
    cmds.joint("FK_Spine_01" ,e=True,zso=True,oj="xyz")
    cmds.joint("FK_Spine_02" ,e=True,zso=True,oj="xyz")
    cmds.joint("FK_Shoulders" ,e=True,zso=True,oj="none")

    #2 Create Bind joints

    #Selectionner la curve

    cmds.select("Crv")

    #Create joints on curve
    import maya.mel as mel
    mel.eval("bonesOnCurve 6 0 0;")

    #Rename joints

    cmds.rename('joint1', 'Bind_Spine_Root')
    cmds.rename('joint2', 'Bind_Spine_01')
    cmds.rename('joint3', 'Bind_Spine_02')
    cmds.rename('joint4', 'Bind_Spine_03')
    cmds.rename('joint5', 'Bind_Spine_04')
    cmds.rename('joint6', 'Bind_Spine_05')
    cmds.rename('joint7', 'Bind_Spine_06')
    cmds.joint("Bind_Spine_Root" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_01" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_02" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_03" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_04" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_05" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_06" ,e=True,zso=True,oj="none")
    cmds.joint("Bind_Spine_Root" ,e=True,zso=True,oj="xyz")
    cmds.joint("Bind_Spine_01" ,e=True,zso=True,oj="xyz")
    cmds.joint("Bind_Spine_02" ,e=True,zso=True,oj="xyz")
    cmds.joint("Bind_Spine_03" ,e=True,zso=True,oj="xyz")
    cmds.joint("Bind_Spine_04" ,e=True,zso=True,oj="xyz")
    cmds.joint("Bind_Spine_05" ,e=True,zso=True,oj="xyz")
    cmds.joint("Bind_Spine_06" ,e=True,zso=True,oj="none")

    #3 Create Jnt

    cmds.duplicate('FK_Root' ,po=True)
    cmds.rename('FK_Root1', 'Jnt_Root')
    cmds.duplicate('FK_Shoulders' ,po=True)
    cmds.rename('FK_Shoulders1', 'Jnt_Shoulders')
    cmds.parent('Jnt_Shoulders',world=True)



    #4 Create Ik Spline and skin curve

    cmds.ikHandle(name='IK_Spine', 
                  solver='ikSplineSolver',
                  startJoint='Bind_Spine_Root', 
                  endEffector='Bind_Spine_06',
                  rootOnCurve=True, 
                  parentCurve=False,
                  simplifyCurve=False)
    cmds.setAttr("IK_Spine.dTwistControlEnable",True)
    cmds.setAttr("IK_Spine.dWorldUpType",4)
    cmds.connectAttr('Jnt_Root.worldMatrix[0]', 'IK_Spine.dWorldUpMatrix')
    cmds.connectAttr('Jnt_Shoulders.worldMatrix[0]', 'IK_Spine.dWorldUpMatrixEnd')
    cmds.rename('effector1', 'eff_Spine')
    cmds.rename('curve1', 'Crv_Spine')
    cmds.skinCluster('Jnt_Root', 'Jnt_Shoulders', 'Crv_Spine')

    #5 Create FK controllers and parent shape

    cmds.circle(n="CTRL_FK_Spine_01")
    cmds.circle(n="CTRL_FK_Spine_02")
    cmds.select("CTRL_FK_Spine_01","FK_Spine_01","CTRL_FK_Spine_02","FK_Spine_02")
    sel=cmds.ls(sl=True)
    shp=cmds.listRelatives(sel[0], s=True)[0]
    cmds.parent(shp, sel[1], r=True, s=True)
    shap=cmds.listRelatives(sel[2], s=True)[0]
    cmds.parent(shap, sel[3], r=True, s=True)

    ## Hierarchy
    cmds.parent("CTRL_FK_Spine_01","Ctrl_01")
    cmds.parent("CTRL_FK_Spine_02","Ctrl_01")
    cmds.select("Bind_Spine_Root","FK_Root","Jnt_Root","Jnt_Shoulders","Crv_Spine")
    a=cmds.ls(sl=True)
    cmds.group(n="Joint_Spine")
    cmds.parent('Joint_Spine','Joint_01')
    cmds.parent("IK_Spine","IKs_01")

def SetUp2(*args):

    # 1 - Selectionner le JointRoot_Ctrl_JointShoulders_Ctrl
    cmds.circle(r=6, n='Root')
    cmds.circle(r=6, n='Shoulders')
    cmds.select('Jnt_Root', 'Root', 'Jnt_Shoulders', 'Shoulders')
    sl = cmds.ls(sl=True, sn=True)
    selected1 = sl[0]
    ctrl1= sl[1]
    selected2 = sl[2]
    ctrl2 = sl[3]

    # 2 - MatchTransform

    cmds.matchTransform(sl[1] , sl[0])
    cmds.matchTransform(sl[3] , sl[2])
    cmds.rename(sl[1] , 'CTRL_Root')
    cmds.rename(sl[3] , 'CTRL_Shouders')

    # 3 - Creation de l'Offset_Master
    ctrl1 = ['CTRL_Root'] 
    ctrl2 = ['CTRL_Shouders']

    cmds.createNode('transform',n ='Offset1')
    grp1 = ['Offset1']
    offset1 = cmds.ls(sl=True)
    cmds.matchTransform(offset1, ctrl1)
    cmds.parent(ctrl1, grp1)
    cmds.rename('Offset1', 'CTRL_Root_Offset')

    cmds.createNode('transform',n ='Offset2')
    grp2 = ['Offset2']
    offset2 = cmds.ls(sl=True)
    cmds.matchTransform(offset2, ctrl2)
    cmds.parent(ctrl2, grp2)
    cmds.rename('Offset2', 'CTRL_Shoulders_Offset')

    cmds.createNode('transform',n ='Master1')
    grp1 = ['Master1']
    Master1 = cmds.ls(sl=True)
    cmds.matchTransform(Master1, ctrl1)
    cmds.parent(Master1, ctrl1)
    cmds.rename('Master1', 'CTRL_Root_Master')

    cmds.createNode('transform',n ='Master2')
    grp1 = ['Master2']
    Master2 = cmds.ls(sl=True)
    cmds.matchTransform(Master2, ctrl2)
    cmds.parent(Master2, ctrl2)
    cmds.rename('Master2', 'CTRL_Shoulders_Master')

    #4 - Parent Ctrl to joint

    cmds.parentConstraint('CTRL_Root_Master', 'Jnt_Root')
    cmds.parentConstraint('CTRL_Shoulders_Master', 'Jnt_Shoulders')
    cmds.parentConstraint('FK_Shoulders', 'CTRL_Shoulders_Offset')
    cmds.parentConstraint('CTRL_Root_Master', 'FK_Spine_01', mo=True, sr=["x","y","z"])
    cmds.parentConstraint('CTRL_Root_Master', 'FK_Spine_02', mo=True, sr=["x","y","z"])

    cmds.addAttr('CTRL_Root', longName='_______', attributeType='enum', enumName='____')
    cmds.setAttr('CTRL_Root._______', channelBox=True )
    cmds.setAttr('CTRL_Root._______', keyable=True )
    cmds.addAttr('CTRL_Root', longName='Stretchy_Column', attributeType='bool')
    cmds.setAttr('CTRL_Root.Stretchy_Column', channelBox=True )
    cmds.setAttr('CTRL_Root.Stretchy_Column', keyable=True)

    #5 - Condition
    cmds.select("Crv_Spine")
    sl = cmds.ls(sl=True, sn=True)
    Crv = sl[0]

    # Creation Nodes#

    CrvInfo = cmds.shadingNode('curveInfo', asUtility=True, n='curveInfo_'+Crv)
    PourcentDiv = cmds.shadingNode('multiplyDivide', asUtility=True, n='Spine_Stretch_Pourcent_Div')
    StretchPow = cmds.shadingNode('multiplyDivide', asUtility=True, n='Spine_Stretch_Pow')
    InvertDiv = cmds.shadingNode('multiplyDivide', asUtility=True, n='Spine_Stretch_Invert_Div')
    CondStretchy = cmds.shadingNode('condition', asUtility=True, n='Cond_Stretchy_Column_IK')
    GlobalScale = cmds.shadingNode('multiplyDivide', asUtility=True, n='Global_Relative_Scale_Column_01_Mult')

    # Connections Nodes#
    cmds.connectAttr(Crv+'.worldSpace[0]', CrvInfo+'.inputCurve')
    cmds.connectAttr(CrvInfo+'.arcLength', PourcentDiv+'.input1X')
    cmds.connectAttr('GlobalMove_01.scaleY', GlobalScale+'.input2X')
    x= cmds.getAttr(CrvInfo+'.arcLength')
    cmds.setAttr(GlobalScale+'.input1X',x)
    cmds.connectAttr(GlobalScale+'.outputX', PourcentDiv+'.input2X')
    cmds.connectAttr(PourcentDiv+'.outputX', StretchPow+'.input1X')
    cmds.connectAttr(StretchPow+'.outputX', InvertDiv+'.input2X')
    cmds.connectAttr(InvertDiv+'.outputX', CondStretchy+'.colorIfTrueG')
    cmds.connectAttr(InvertDiv+'.outputX', CondStretchy+'.colorIfTrueB')
    cmds.connectAttr(PourcentDiv+'.outputX', CondStretchy+'.colorIfTrueR')
    y=input()
    cmds.setAttr(StretchPow+'.input2X',y)
    cmds.setAttr(InvertDiv+'.input1X',1)
    cmds.setAttr(CondStretchy+'.secondTerm',1)
    cmds.connectAttr('CTRL_Root.Stretchy_Column', CondStretchy+'.firstTerm')
    cmds.setAttr(PourcentDiv+'.operation',2)
    cmds.setAttr(StretchPow+'.operation',3)
    cmds.setAttr(InvertDiv+'.operation',2)

    #Out Connections
    cmds.select('Bind_Spine_Root', 'Bind_Spine_01', 'Bind_Spine_02', 'Bind_Spine_03', 'Bind_Spine_04', 'Bind_Spine_05', 'Bind_Spine_06')
    jnt = cmds.ls(sl=True, sn=True)
    x=0
    for x in range(0,6):
        cmds.connectAttr(CondStretchy+'.outColorR', jnt[x]+'.scaleX')
        cmds.connectAttr(CondStretchy+'.outColorG', jnt[x]+'.scaleY')
        cmds.connectAttr(CondStretchy+'.outColorB', jnt[x]+'.scaleZ')

    #Hierarchy

    cmds.parent('CTRL_Root_Offset','Ctrl_01')
    cmds.parent('CTRL_Shoulders_Offset','Ctrl_01')
    cmds.parent('Crv', 'ExtraNodes_To_Hide')



#window___________________________________________________________________________________________________________
    
	
window= cmds.window( t="Spine AutoRigg",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 193) )
mainw = cmds.formLayout()
nm = cmds.frameLayout( label='Spine AutoRigg', labelAlign='center')
cmds.columnLayout()

cmds.menu( label='Help', tearOff=True )
cmds.menuItem( l='Koman on fai?', c=help_def )
cmds.menuItem( divider=True )
cmds.menuItem( label='Quit' )

cmds.rowColumnLayout( p = nm, numberOfColumns=2, columnWidth=[(1, 125), (2, 125)] )


eyecent = cmds.frameLayout(p= nm, label="Select the curve Root to Shoulders", labelAlign='center' )
cmds.button(l='Set up', align='Set Up', c=SetUp1)

eylup = cmds.frameLayout( p= nm, label="Finish", labelAlign='center' )
cmds.button(l='Set up', align='Set Up', c=SetUp2)

cmds.showWindow(window)