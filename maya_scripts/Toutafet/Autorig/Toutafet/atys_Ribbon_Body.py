    
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
    

def CreateRibbon (*args):

    radc = cmds.radioCollection(rc, q = True, sl= True)
    
    if radc == 'arm_right' :
        side_S = 'Shoulder_R'
        side_F = 'Forearm_R'
    if radc == 'arm_left' :
        side_S = 'Shoulder_L'
        side_F = 'Forearm_L'
    if radc == 'leg_right' :
        side_S = 'Leg_R'
        side_F = 'Knee_R'
    if radc == 'leg_left':
        side_S = 'Leg_L'
        side_F = 'Knee_L'
        
        #____Create Ribbon Haut____:
#____VARS___________________:
    RBN = 5
    RIB = side_S
    A = (1.0/float(RBN-1))
    
    
    #---  init    

    cmds.nurbsPlane (w = 10, lr = 0.2, u=5)
    cmds.select('nurbsPlane1')
    cmds.rotate ('90deg', 0, '90deg', r=True)

    
    sel = 'nurbsPlane1'
    loft = cmds.listRelatives(sel, s=True)[0]
    grp = cmds.createNode('transform', n = 'Grp_rivets_'+RIB+'_001')
        
    idx = 0
    
    for x in range(RBN):
    
        #--- Create Locator Rivet and joint under
        rivet = cmds.spaceLocator( n = 'rivet_'+RIB+'_0'+str(idx+1))[0]
        jnt = cmds.joint( n = 'Bind_rivet_'+RIB+'_0'+str(idx+1))
        
        #---  Create nodes
        nodes = []
        
        nodes.append( cmds.createNode('pointOnSurfaceInfo', n= rivet + '_pOnSurf'  ) )             # 3
        nodes.append( cmds.createNode('fourByFourMatrix', n= rivet + '_4by4_MTX'  ) )              # 4
        nodes.append( cmds.createNode('decomposeMatrix', n= rivet + '_dMTX') )                     # 5
        #- Point on surface info
        cmds.setAttr( nodes[0] + '.turnOnPercentage', True)
        cmds.connectAttr( str(loft) + '.worldSpace', nodes[0] + '.is', f=True) 
    
        #--- Four By Four Matrix
        cmds.connectAttr( nodes[0] + '.positionX', nodes[1] + '.in30' )
        cmds.connectAttr( nodes[0] + '.positionY', nodes[1] + '.in31' )
        cmds.connectAttr( nodes[0] + '.positionZ', nodes[1] + '.in32' )
        cmds.connectAttr( nodes[0] + '.normalX', nodes[1] + '.in00' )
        cmds.connectAttr( nodes[0] + '.normalY', nodes[1] + '.in01' )
        cmds.connectAttr( nodes[0] + '.normalZ', nodes[1] + '.in02' )
        cmds.connectAttr( nodes[0] + '.tangentUx', nodes[1] + '.in20' )
        cmds.connectAttr( nodes[0] + '.tangentUy', nodes[1] + '.in21' )
        cmds.connectAttr( nodes[0] + '.tangentUz', nodes[1] + '.in22' )
        cmds.connectAttr( nodes[0] + '.tangentVx', nodes[1] + '.in10' )
        cmds.connectAttr( nodes[0] + '.tangentVy', nodes[1] + '.in11' )
        cmds.connectAttr( nodes[0] + '.tangentVz', nodes[1] + '.in12' )
    
        #--- Decompose Matrix
        cmds.connectAttr( nodes[1] + '.output', nodes[2] + '.inputMatrix' )
    
        #--- Drive Rivet
        cmds.connectAttr( nodes[2] + '.outputTranslate', rivet + '.translate' )
        
        cmds.connectAttr( nodes[2] + '.outputRotate', rivet + '.rotate' )
    
        #--- Add Ctrl attributes to rivet
        cmds.addAttr(rivet, ln='posU', at='float', min=.0, max=1.0, dv=float(A)*float(idx), k=True)
        cmds.addAttr(rivet, ln='posV', at='float', min=.0, max=1.0, dv=.5, k=True)
        cmds.setAttr('rivet_'+RIB+'_0'+str(idx+1)+'_pOnSurf'+'.parameterV', 0.5)
        
    
        #--- Historical intereset
        for node in nodes :
            cmds.setAttr( node + '.ihi', 0)
        
        cmds.setAttr( rivet + 'Shape.ihi', 0)
    
        #--- Clean
        for attr in ['t', 'r', 's'] :
            for axis in ['x', 'y', 'z'] :
                cmds.setAttr('%s.%s%s' %(rivet, attr, axis), k=False)
        for axis in ['X', 'Y', 'Z'] :
            cmds.setAttr('%sShape.localPosition%s' %(rivet, axis), k=False, cb=False)
            cmds.setAttr('%sShape.localScale%s' %(rivet, axis), 0.01)
        
        
        cmds.parent( rivet, grp)
        idx+=1
    
    cmds.setAttr('rivet_'+RIB+'_01'+'_pOnSurf'+'.parameterU', 0.1)
    cmds.setAttr('rivet_'+RIB+'_02'+'_pOnSurf'+'.parameterU', 0.3)
    cmds.setAttr('rivet_'+RIB+'_03'+'_pOnSurf'+'.parameterU', 0.5)
    cmds.setAttr('rivet_'+RIB+'_04'+'_pOnSurf'+'.parameterU', 0.7)
    cmds.setAttr('rivet_'+RIB+'_05'+'_pOnSurf'+'.parameterU', 0.9)    
    cmds.parent( sel, grp)
    
    
    #___Range ta chambre!:
    cmds.createNode('transform', n='Ribbon_'+RIB)
    cmds.createNode('transform', n='GlobalMove_'+RIB)
    cmds.createNode('transform', n='ExtraNodes_Ribbon_'+RIB)
    cmds.createNode('transform', n='ExtraNodes_To_Show_'+RIB)
    cmds.createNode('transform', n='ExtraNodes_To_Hide_'+RIB)
    
    cmds.parent('ExtraNodes_To_Show_'+RIB, 'ExtraNodes_Ribbon_'+RIB)
    cmds.parent('ExtraNodes_To_Hide_'+RIB, 'ExtraNodes_Ribbon_'+RIB)

    cmds.rename('nurbsPlane1','Ribbon_Surface_'+RIB+'_01')
    cmds.parent('Ribbon_Surface_'+RIB+'_01', 'Ribbon_'+RIB)
    cmds.parent('Grp_rivets_'+RIB+'_001', 'ExtraNodes_To_Show_'+RIB)
    cmds.parent('GlobalMove_'+RIB, 'Ribbon_'+RIB)
    cmds.parent('ExtraNodes_Ribbon_'+RIB, 'Ribbon_'+RIB)
    
    #____Creation Ctrls:
        
    cmds.circle(n='CTRL_Ribbon_'+RIB+'_A01')
    cmds.circle(n='CTRL_Ribbon_'+RIB+'_B01')
    cmds.circle(n='CTRL_Ribbon_'+RIB+'_Mid')
    
    cmds.delete('CTRL_Ribbon_'+RIB+'_Mid', ch=True) 
    cmds.move( 5, 'CTRL_Ribbon_'+RIB+'_A01', x=True )
    cmds.FreezeTransformations('CTRL_Ribbon_'+RIB+'_A01')
    cmds.makeIdentity('CTRL_Ribbon_'+RIB+'_A01', apply=True, t=1, r=1, s=1, n=2 )
    cmds.delete('CTRL_Ribbon_'+RIB+'_A01', ch=True) 
    cmds.move( -5, 'CTRL_Ribbon_'+RIB+'_B01', x=True )
    cmds.FreezeTransformations('CTRL_Ribbon_'+RIB+'_B01') 
    cmds.makeIdentity('CTRL_Ribbon_'+RIB+'_B01', apply=True, t=1, r=1, s=1, n=2 )
    cmds.delete('CTRL_Ribbon_'+RIB+'_B01', ch=True)
    
    cmds.createNode('transform', n='Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.createNode('transform', n='CTRL_Ribbon_'+RIB+'_Mid_Master') 
    cmds.parent('CTRL_Ribbon_'+RIB+'_A01','Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.parent('CTRL_Ribbon_'+RIB+'_Mid','CTRL_Ribbon_'+RIB+'_Mid_Master')
    cmds.parent('CTRL_Ribbon_'+RIB+'_Mid_Master','Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.parent('CTRL_Ribbon_'+RIB+'_B01','Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.parent('Grp_CTRLs_Ribbon_'+RIB+'_01','GlobalMove_'+RIB)

    
    
    #____Creation BlendShape:
    
    cmds.duplicate('Ribbon_Surface_'+RIB+'_01')
    cmds.rename('Ribbon_Surface_'+RIB+'_02','Ribbon_BShp_Surface_'+RIB+'_01')
    cmds.blendShape('Ribbon_BShp_Surface_'+RIB+'_01', 'Ribbon_Surface_'+RIB+'_01', n='Rbn_BShp_'+RIB, en=1)
    cmds.setAttr ('Rbn_BShp_'+RIB+'.Ribbon_BShp_Surface_'+RIB+'_01', 1)
    cmds.parent('Ribbon_BShp_Surface_'+RIB+'_01', 'ExtraNodes_To_Hide_'+RIB)
    
    cmds.curve( d=2, p=[(-5,  0, 0), (0, 0, 0), (5, 0, 0)] )
    cmds.rename('curve1', 'Crv_Wire_Ribbon_Surface_'+RIB+'_01')
    cmds.parent('Crv_Wire_Ribbon_Surface_'+RIB+'_01', 'ExtraNodes_To_Hide_'+RIB)

    cmds.wire('Ribbon_BShp_Surface_'+RIB+'_01', w='Crv_Wire_Ribbon_Surface_'+RIB+'_01', n='wireAttr_'+RIB+'_01')
    cmds.wire( 'wireAttr_'+RIB+'_01', edit=True, en=1, dds=[(0, 20)] )


#____Create DrvJnts ____:
    
    cmds.createNode('transform', n='Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('Grp_DrvJnt_Ribbon_'+RIB+'_01', 'ExtraNodes_To_Hide_'+RIB)
    
    cmds.joint(n='DrvJnt_Ribbon_'+RIB+'_A01')
    cmds.joint(n='DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.joint(n='DrvJnt_Ribbon_'+RIB+'_B01')
  
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_Mid','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_B01','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    
    cmds.move( +5, 'DrvJnt_Ribbon_'+RIB+'_A01', x=True )
    cmds.move( 0, 'DrvJnt_Ribbon_'+RIB+'_Mid', x=True )  
    cmds.move( -5, 'DrvJnt_Ribbon_'+RIB+'_B01', x=True ) 
    
    cmds.createNode('transform', n='DrvJnt_Ribbon_'+RIB+'_A01_Offset')
    cmds.createNode('transform', n='Master_DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.createNode('transform', n='DrvJnt_Ribbon_'+RIB+'_B01_Offset')
    cmds.matchTransform('DrvJnt_Ribbon_'+RIB+'_A01_Offset','DrvJnt_Ribbon_'+RIB+'_A01')
    cmds.matchTransform('Master_DrvJnt_Ribbon_'+RIB+'_Mid','DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.matchTransform('DrvJnt_Ribbon_'+RIB+'_B01_Offset','DrvJnt_Ribbon_'+RIB+'_B01')
    
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_A01_Offset','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('Master_DrvJnt_Ribbon_'+RIB+'_Mid','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_B01_Offset','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_A01','DrvJnt_Ribbon_'+RIB+'_A01_Offset')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_Mid','Master_DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_B01','DrvJnt_Ribbon_'+RIB+'_B01_Offset')
    
    
#____Skin DrvJnt____:
    
    cmds.select('DrvJnt_Ribbon_'+RIB+'_A01','DrvJnt_Ribbon_'+RIB+'_Mid','DrvJnt_Ribbon_'+RIB+'_B01','Crv_Wire_Ribbon_Surface_'+RIB+'_01')
    cmds.skinCluster()
    
#____Connect CTRLs to DrvJnts____:
    
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_A01'+'.translate','DrvJnt_Ribbon_'+RIB+'_A01'+'.translate')
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_Mid'+'.translate','DrvJnt_Ribbon_'+RIB+'_Mid'+'.translate')
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_B01'+'.translate','DrvJnt_Ribbon_'+RIB+'_B01'+'.translate')
    
    
    
#____Connect Matrix Ctrls____:
    
    #____VARS___:
        
    A01='DrvJnt_Ribbon_'+RIB+'_A01'
    B01='DrvJnt_Ribbon_'+RIB+'_B01'
    Mid='CTRL_Ribbon_'+RIB+'_Mid_Master'
    
    #____Create Nodes____:
        
    AddMTX = cmds.shadingNode('wtAddMatrix', asUtility=True, n='wtAddMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    MultMTX = cmds.shadingNode('multMatrix',asUtility=True, n='blendMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    DecMTX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='decomposeMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    BlendMTX = cmds.shadingNode('addDoubleLinear', asUtility=True, n='blend_CTRL_Ribbon_'+RIB+'_Mid_01')
    
    #____Connect Matrix____:
    
    cmds.setAttr(BlendMTX+'.input1', 0.5)
    cmds.connectAttr(A01+'.worldMatrix[0]',AddMTX+'.wtMatrix[0].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[0].weightIn')
    cmds.connectAttr(B01+'.worldMatrix[0]',AddMTX+'.wtMatrix[1].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[1].weightIn')
    cmds.connectAttr(AddMTX+'.matrixSum',MultMTX+'.matrixIn[0]')
    cmds.connectAttr(MultMTX+'.matrixSum', DecMTX+'.inputMatrix')
    cmds.connectAttr(DecMTX+'.outputTranslate',Mid+'.translate')
    
    
#____Connect Matrix DrvJnts__:

    Mid='Master_DrvJnt_Ribbon_'+RIB+'_Mid'
    
    #____Create Nodes____:
        
    AddMTX = cmds.shadingNode('wtAddMatrix', asUtility=True, n='wtAddMTX_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    MultMTX = cmds.shadingNode('multMatrix',asUtility=True, n='blendMTX_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    DecMTX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='decomposeMTX_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    BlendMTX = cmds.shadingNode('addDoubleLinear', asUtility=True, n='blend_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    
    #____Connect Matrix____:
    
    cmds.setAttr(BlendMTX+'.input1', 0.5)
    cmds.connectAttr(A01+'.worldMatrix[0]',AddMTX+'.wtMatrix[0].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[0].weightIn')
    cmds.connectAttr(B01+'.worldMatrix[0]',AddMTX+'.wtMatrix[1].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[1].weightIn')
    cmds.connectAttr(AddMTX+'.matrixSum',MultMTX+'.matrixIn[0]')
    cmds.connectAttr(MultMTX+'.matrixSum', DecMTX+'.inputMatrix')
    cmds.connectAttr(DecMTX+'.outputTranslate',Mid+'.translate')
    

#____Twist____:
    
    cmds.select('Ribbon_BShp_Surface_'+RIB+'_01')
    cmds.nonLinear(typ='twist', n='Twist_Ribbon_'+RIB+'_01')
    cmds.select('Twist_Ribbon_'+RIB+'_01Handle')
    cmds.setAttr ('Twist_Ribbon_'+RIB+'_01Handle'+'.rotateX', 0)
    
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_B01'+'.rotateX', 'Twist_Ribbon_'+RIB+'_01HandleShape'+'.endAngle')
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_A01'+'.rotateX', 'Twist_Ribbon_'+RIB+'_01HandleShape'+'.startAngle')
    cmds.reorderDeformers('wireAttr_'+RIB+'_01', 'Twist_Ribbon_'+RIB+'_01', 'Ribbon_'+RIB+'|ExtraNodes_Ribbon_'+RIB+'|ExtraNodes_To_Hide_'+RIB+'|Ribbon_BShp_Surface_'+RIB+'_01')
    cmds.parent('Twist_Ribbon_'+RIB+'_01Handle', 'ExtraNodes_To_Hide_'+RIB)
    
#____CTRL General____:
  
    cmds.circle(n= 'CTRL_General_Ribbon_'+RIB+'_01')
    cmds.setAttr ('CTRL_General_Ribbon_'+RIB+'_01'+'.rotateX', 90)
    cmds.FreezeTransformations('CTRL_General_Ribbon_'+RIB+'_01')
    cmds.makeIdentity('CTRL_General_Ribbon_'+RIB+'_01', apply=True, t=1, r=1, s=1, n=2 )
    
    cmds.parent('CTRL_General_Ribbon_'+RIB+'_01','Ribbon_'+RIB)
    cmds.parent('Ribbon_Surface_'+RIB+'_01','CTRL_General_Ribbon_'+RIB+'_01')
    cmds.parent('GlobalMove_'+RIB,'CTRL_General_Ribbon_'+RIB+'_01')
    
    #____VARS____:
        
    rivet01='rivet_'+RIB+'_01'
    rivet02='rivet_'+RIB+'_02'
    rivet03='rivet_'+RIB+'_03'
    rivet04='rivet_'+RIB+'_04'
    rivet05='rivet_'+RIB+'_05'
    CTRL='CTRL_General_Ribbon_'+RIB+'_01'
    
    MultMTX = cmds.shadingNode('multMatrix',asUtility=True, n='blendMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    DecMTX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='decomposeMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    MultMTX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+rivet01)
    DecMTX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+rivet01)
    


                            
    #____Connect____:
    cmds.connectAttr(rivet01+'.worldMatrix[0]',MultMTX_Offset+'.matrixIn[0]')
    cmds.connectAttr(CTRL+'.worldInverseMatrix[0]',MultMTX_Offset+'.matrixIn[1]')
    cmds.connectAttr(MultMTX_Offset+'.matrixSum',DecMTX_Offset+'.inputMatrix')
    cmds.disconnectAttr (MultMTX_Offset+'.matrixSum',DecMTX_Offset+'.inputMatrix')
    cmds.delete(MultMTX_Offset)
    
    cmds.connectAttr(DecMTX_Offset+'.inputMatrix',MultMTX+'.matrixIn[0]')
    cmds.connectAttr(CTRL+'.worldMatrix[0]',MultMTX+'.matrixIn[1]')
    cmds.connectAttr(rivet01+'.parentInverseMatrix[0]',MultMTX+'.matrixIn[2]')
    cmds.connectAttr(MultMTX+'.matrixSum',DecMTX+'.inputMatrix')
    
    cmds.connectAttr(DecMTX+'.outputScale',rivet01+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet02+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet03+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet04+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet05+'.s')

    
    
    #____AN OTHER ONE____#
    
    
        #____Create Ribbon Bas____:
#____VARS___________________:
    RBN = 5
    RIB = side_F
    A = (1.0/float(RBN-1))
    
    
    #---  init    

    cmds.nurbsPlane (w = 10, lr = 0.2, u=5)
    cmds.select('nurbsPlane1')
    cmds.rotate ('90deg', 0, '90deg', r=True)

    
    sel = 'nurbsPlane1'
    loft = cmds.listRelatives(sel, s=True)[0]
    grp = cmds.createNode('transform', n = 'Grp_rivets_'+RIB+'_001')
        
    idx = 0
    
    for x in range(RBN):
    
        #--- Create Locator Rivet and joint under
        rivet = cmds.spaceLocator( n = 'rivet_'+RIB+'_0'+str(idx+1))[0]
        jnt = cmds.joint( n = 'Bind_rivet_'+RIB+'_0'+str(idx+1))
        
        #---  Create nodes
        nodes = []
        
        nodes.append( cmds.createNode('pointOnSurfaceInfo', n= rivet + '_pOnSurf'  ) )             # 3
        nodes.append( cmds.createNode('fourByFourMatrix', n= rivet + '_4by4_MTX'  ) )              # 4
        nodes.append( cmds.createNode('decomposeMatrix', n= rivet + '_dMTX') )                     # 5
        #- Point on surface info
        cmds.setAttr( nodes[0] + '.turnOnPercentage', True)
        cmds.connectAttr( str(loft) + '.worldSpace', nodes[0] + '.is', f=True) 
    
        #--- Four By Four Matrix
        cmds.connectAttr( nodes[0] + '.positionX', nodes[1] + '.in30' )
        cmds.connectAttr( nodes[0] + '.positionY', nodes[1] + '.in31' )
        cmds.connectAttr( nodes[0] + '.positionZ', nodes[1] + '.in32' )
        cmds.connectAttr( nodes[0] + '.normalX', nodes[1] + '.in00' )
        cmds.connectAttr( nodes[0] + '.normalY', nodes[1] + '.in01' )
        cmds.connectAttr( nodes[0] + '.normalZ', nodes[1] + '.in02' )
        cmds.connectAttr( nodes[0] + '.tangentUx', nodes[1] + '.in20' )
        cmds.connectAttr( nodes[0] + '.tangentUy', nodes[1] + '.in21' )
        cmds.connectAttr( nodes[0] + '.tangentUz', nodes[1] + '.in22' )
        cmds.connectAttr( nodes[0] + '.tangentVx', nodes[1] + '.in10' )
        cmds.connectAttr( nodes[0] + '.tangentVy', nodes[1] + '.in11' )
        cmds.connectAttr( nodes[0] + '.tangentVz', nodes[1] + '.in12' )
    
        #--- Decompose Matrix
        cmds.connectAttr( nodes[1] + '.output', nodes[2] + '.inputMatrix' )
    
        #--- Drive Rivet
        cmds.connectAttr( nodes[2] + '.outputTranslate', rivet + '.translate' )
        
        cmds.connectAttr( nodes[2] + '.outputRotate', rivet + '.rotate' )
    
        #--- Add Ctrl attributes to rivet
        cmds.addAttr(rivet, ln='posU', at='float', min=.0, max=1.0, dv=float(A)*float(idx), k=True)
        cmds.addAttr(rivet, ln='posV', at='float', min=.0, max=1.0, dv=.5, k=True)
        cmds.setAttr('rivet_'+RIB+'_0'+str(idx+1)+'_pOnSurf'+'.parameterV', 0.5)
        
    
        #--- Historical intereset
        for node in nodes :
            cmds.setAttr( node + '.ihi', 0)
        
        cmds.setAttr( rivet + 'Shape.ihi', 0)
    
        #--- Clean
        for attr in ['t', 'r', 's'] :
            for axis in ['x', 'y', 'z'] :
                cmds.setAttr('%s.%s%s' %(rivet, attr, axis), k=False)
        for axis in ['X', 'Y', 'Z'] :
            cmds.setAttr('%sShape.localPosition%s' %(rivet, axis), k=False, cb=False)
            cmds.setAttr('%sShape.localScale%s' %(rivet, axis), 0.01)
        
        
        cmds.parent( rivet, grp)
        idx+=1
    
    cmds.setAttr('rivet_'+RIB+'_01'+'_pOnSurf'+'.parameterU', 0.1)
    cmds.setAttr('rivet_'+RIB+'_02'+'_pOnSurf'+'.parameterU', 0.3)
    cmds.setAttr('rivet_'+RIB+'_03'+'_pOnSurf'+'.parameterU', 0.5)
    cmds.setAttr('rivet_'+RIB+'_04'+'_pOnSurf'+'.parameterU', 0.7)
    cmds.setAttr('rivet_'+RIB+'_05'+'_pOnSurf'+'.parameterU', 0.9)    
    cmds.parent( sel, grp)
    
    
    #___Range ta chambre!:
    cmds.createNode('transform', n='Ribbon_'+RIB)
    cmds.createNode('transform', n='GlobalMove_'+RIB)
    cmds.createNode('transform', n='ExtraNodes_Ribbon_'+RIB)
    cmds.createNode('transform', n='ExtraNodes_To_Show_'+RIB)
    cmds.createNode('transform', n='ExtraNodes_To_Hide_'+RIB)
    
    cmds.parent('ExtraNodes_To_Show_'+RIB, 'ExtraNodes_Ribbon_'+RIB)
    cmds.parent('ExtraNodes_To_Hide_'+RIB, 'ExtraNodes_Ribbon_'+RIB)

    cmds.rename('nurbsPlane1','Ribbon_Surface_'+RIB+'_01')
    cmds.parent('Ribbon_Surface_'+RIB+'_01', 'Ribbon_'+RIB)
    cmds.parent('Grp_rivets_'+RIB+'_001', 'ExtraNodes_To_Show_'+RIB)
    cmds.parent('GlobalMove_'+RIB, 'Ribbon_'+RIB)
    cmds.parent('ExtraNodes_Ribbon_'+RIB, 'Ribbon_'+RIB)
    
    #____Creation Ctrls:
        
    cmds.circle(n='CTRL_Ribbon_'+RIB+'_A01')
    cmds.circle(n='CTRL_Ribbon_'+RIB+'_B01')
    cmds.circle(n='CTRL_Ribbon_'+RIB+'_Mid')
    
    cmds.delete('CTRL_Ribbon_'+RIB+'_Mid', ch=True) 
    cmds.move( 5, 'CTRL_Ribbon_'+RIB+'_A01', x=True )
    cmds.FreezeTransformations('CTRL_Ribbon_'+RIB+'_A01')
    cmds.makeIdentity('CTRL_Ribbon_'+RIB+'_A01', apply=True, t=1, r=1, s=1, n=2 )
    cmds.delete('CTRL_Ribbon_'+RIB+'_A01', ch=True) 
    cmds.move( -5, 'CTRL_Ribbon_'+RIB+'_B01', x=True )
    cmds.FreezeTransformations('CTRL_Ribbon_'+RIB+'_B01') 
    cmds.makeIdentity('CTRL_Ribbon_'+RIB+'_B01', apply=True, t=1, r=1, s=1, n=2 )
    cmds.delete('CTRL_Ribbon_'+RIB+'_B01', ch=True)
    
    cmds.createNode('transform', n='Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.createNode('transform', n='CTRL_Ribbon_'+RIB+'_Mid_Master') 
    cmds.parent('CTRL_Ribbon_'+RIB+'_A01','Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.parent('CTRL_Ribbon_'+RIB+'_Mid','CTRL_Ribbon_'+RIB+'_Mid_Master')
    cmds.parent('CTRL_Ribbon_'+RIB+'_Mid_Master','Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.parent('CTRL_Ribbon_'+RIB+'_B01','Grp_CTRLs_Ribbon_'+RIB+'_01')
    cmds.parent('Grp_CTRLs_Ribbon_'+RIB+'_01','GlobalMove_'+RIB)

    
    
    #____Creation BlendShape:
    
    cmds.duplicate('Ribbon_Surface_'+RIB+'_01')
    cmds.rename('Ribbon_Surface_'+RIB+'_02','Ribbon_BShp_Surface_'+RIB+'_01')
    cmds.blendShape('Ribbon_BShp_Surface_'+RIB+'_01', 'Ribbon_Surface_'+RIB+'_01', n='Rbn_BShp_'+RIB, en=1)
    cmds.setAttr ('Rbn_BShp_'+RIB+'.Ribbon_BShp_Surface_'+RIB+'_01', 1)
    cmds.parent('Ribbon_BShp_Surface_'+RIB+'_01', 'ExtraNodes_To_Hide_'+RIB)
    
    cmds.curve( d=2, p=[(-5,  0, 0), (0, 0, 0), (5, 0, 0)] )
    cmds.rename('curve1', 'Crv_Wire_Ribbon_Surface_'+RIB+'_01')
    cmds.parent('Crv_Wire_Ribbon_Surface_'+RIB+'_01', 'ExtraNodes_To_Hide_'+RIB)

    cmds.wire('Ribbon_BShp_Surface_'+RIB+'_01', w='Crv_Wire_Ribbon_Surface_'+RIB+'_01', n='wireAttr_'+RIB+'_01')
    cmds.wire( 'wireAttr_'+RIB+'_01', edit=True, en=1, dds=[(0, 20)] )


#____Create DrvJnts ____:
    
    cmds.createNode('transform', n='Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('Grp_DrvJnt_Ribbon_'+RIB+'_01', 'ExtraNodes_To_Hide_'+RIB)
    
    cmds.joint(n='DrvJnt_Ribbon_'+RIB+'_A01')
    cmds.joint(n='DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.joint(n='DrvJnt_Ribbon_'+RIB+'_B01')
  
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_Mid','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_B01','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    
    cmds.move( +5, 'DrvJnt_Ribbon_'+RIB+'_A01', x=True )
    cmds.move( 0, 'DrvJnt_Ribbon_'+RIB+'_Mid', x=True )  
    cmds.move( -5, 'DrvJnt_Ribbon_'+RIB+'_B01', x=True ) 
    
    cmds.createNode('transform', n='DrvJnt_Ribbon_'+RIB+'_A01_Offset')
    cmds.createNode('transform', n='Master_DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.createNode('transform', n='DrvJnt_Ribbon_'+RIB+'_B01_Offset')
    cmds.matchTransform('DrvJnt_Ribbon_'+RIB+'_A01_Offset','DrvJnt_Ribbon_'+RIB+'_A01')
    cmds.matchTransform('Master_DrvJnt_Ribbon_'+RIB+'_Mid','DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.matchTransform('DrvJnt_Ribbon_'+RIB+'_B01_Offset','DrvJnt_Ribbon_'+RIB+'_B01')
    
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_A01_Offset','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('Master_DrvJnt_Ribbon_'+RIB+'_Mid','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_B01_Offset','Grp_DrvJnt_Ribbon_'+RIB+'_01')
    
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_A01','DrvJnt_Ribbon_'+RIB+'_A01_Offset')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_Mid','Master_DrvJnt_Ribbon_'+RIB+'_Mid')
    cmds.parent('DrvJnt_Ribbon_'+RIB+'_B01','DrvJnt_Ribbon_'+RIB+'_B01_Offset')
    
    
#____Skin DrvJnt____:
    
    cmds.select('DrvJnt_Ribbon_'+RIB+'_A01','DrvJnt_Ribbon_'+RIB+'_Mid','DrvJnt_Ribbon_'+RIB+'_B01','Crv_Wire_Ribbon_Surface_'+RIB+'_01')
    cmds.skinCluster()
    
#____Connect CTRLs to DrvJnts____:
    
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_A01'+'.translate','DrvJnt_Ribbon_'+RIB+'_A01'+'.translate')
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_Mid'+'.translate','DrvJnt_Ribbon_'+RIB+'_Mid'+'.translate')
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_B01'+'.translate','DrvJnt_Ribbon_'+RIB+'_B01'+'.translate')
    
    
    
#____Connect Matrix Ctrls____:
    
    #____VARS___:
        
    A01='DrvJnt_Ribbon_'+RIB+'_A01'
    B01='DrvJnt_Ribbon_'+RIB+'_B01'
    Mid='CTRL_Ribbon_'+RIB+'_Mid_Master'
    
    #____Create Nodes____:
        
    AddMTX = cmds.shadingNode('wtAddMatrix', asUtility=True, n='wtAddMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    MultMTX = cmds.shadingNode('multMatrix',asUtility=True, n='blendMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    DecMTX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='decomposeMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    BlendMTX = cmds.shadingNode('addDoubleLinear', asUtility=True, n='blend_CTRL_Ribbon_'+RIB+'_Mid_01')
    
    #____Connect Matrix____:
    
    cmds.setAttr(BlendMTX+'.input1', 0.5)
    cmds.connectAttr(A01+'.worldMatrix[0]',AddMTX+'.wtMatrix[0].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[0].weightIn')
    cmds.connectAttr(B01+'.worldMatrix[0]',AddMTX+'.wtMatrix[1].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[1].weightIn')
    cmds.connectAttr(AddMTX+'.matrixSum',MultMTX+'.matrixIn[0]')
    cmds.connectAttr(MultMTX+'.matrixSum', DecMTX+'.inputMatrix')
    cmds.connectAttr(DecMTX+'.outputTranslate',Mid+'.translate')
    
    
#____Connect Matrix DrvJnts__:

    Mid='Master_DrvJnt_Ribbon_'+RIB+'_Mid'
    
    #____Create Nodes____:
        
    AddMTX = cmds.shadingNode('wtAddMatrix', asUtility=True, n='wtAddMTX_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    MultMTX = cmds.shadingNode('multMatrix',asUtility=True, n='blendMTX_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    DecMTX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='decomposeMTX_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    BlendMTX = cmds.shadingNode('addDoubleLinear', asUtility=True, n='blend_DrvJnt_Ribbon_'+RIB+'_Mid_01')
    
    #____Connect Matrix____:
    
    cmds.setAttr(BlendMTX+'.input1', 0.5)
    cmds.connectAttr(A01+'.worldMatrix[0]',AddMTX+'.wtMatrix[0].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[0].weightIn')
    cmds.connectAttr(B01+'.worldMatrix[0]',AddMTX+'.wtMatrix[1].matrixIn')
    cmds.connectAttr(BlendMTX+'.output',AddMTX+'.wtMatrix[1].weightIn')
    cmds.connectAttr(AddMTX+'.matrixSum',MultMTX+'.matrixIn[0]')
    cmds.connectAttr(MultMTX+'.matrixSum', DecMTX+'.inputMatrix')
    cmds.connectAttr(DecMTX+'.outputTranslate',Mid+'.translate')
    

#____Twist____:
    
    cmds.select('Ribbon_BShp_Surface_'+RIB+'_01')
    cmds.nonLinear(typ='twist', n='Twist_Ribbon_'+RIB+'_01')
    cmds.select('Twist_Ribbon_'+RIB+'_01Handle')
    cmds.setAttr ('Twist_Ribbon_'+RIB+'_01Handle'+'.rotateX', 0)
    
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_B01'+'.rotateX', 'Twist_Ribbon_'+RIB+'_01HandleShape'+'.endAngle')
    cmds.connectAttr('CTRL_Ribbon_'+RIB+'_A01'+'.rotateX', 'Twist_Ribbon_'+RIB+'_01HandleShape'+'.startAngle')
    cmds.reorderDeformers('wireAttr_'+RIB+'_01', 'Twist_Ribbon_'+RIB+'_01', 'Ribbon_'+RIB+'|ExtraNodes_Ribbon_'+RIB+'|ExtraNodes_To_Hide_'+RIB+'|Ribbon_BShp_Surface_'+RIB+'_01')
    cmds.parent('Twist_Ribbon_'+RIB+'_01Handle', 'ExtraNodes_To_Hide_'+RIB)
    
#____CTRL General____:
  
    cmds.circle(n= 'CTRL_General_Ribbon_'+RIB+'_01')
    cmds.setAttr ('CTRL_General_Ribbon_'+RIB+'_01'+'.rotateX', 90)
    cmds.FreezeTransformations('CTRL_General_Ribbon_'+RIB+'_01')
    cmds.makeIdentity('CTRL_General_Ribbon_'+RIB+'_01', apply=True, t=1, r=1, s=1, n=2 )
    
    cmds.parent('CTRL_General_Ribbon_'+RIB+'_01','Ribbon_'+RIB)
    cmds.parent('Ribbon_Surface_'+RIB+'_01','CTRL_General_Ribbon_'+RIB+'_01')
    cmds.parent('GlobalMove_'+RIB,'CTRL_General_Ribbon_'+RIB+'_01')
    
    #____VARS____:
        
    rivet01='rivet_'+RIB+'_01'
    rivet02='rivet_'+RIB+'_02'
    rivet03='rivet_'+RIB+'_03'
    rivet04='rivet_'+RIB+'_04'
    rivet05='rivet_'+RIB+'_05'
    CTRL='CTRL_General_Ribbon_'+RIB+'_01'
    
    MultMTX = cmds.shadingNode('multMatrix',asUtility=True, n='blendMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    DecMTX = cmds.shadingNode('decomposeMatrix', asUtility=True, n='decomposeMTX_CTRL_Ribbon_'+RIB+'_Mid_01')
    MultMTX_Offset = cmds.shadingNode('multMatrix',asUtility=True, n='MultMatX_Offset_'+rivet01)
    DecMTX_Offset = cmds.shadingNode('decomposeMatrix', asUtility=True, n='DecMatX_Offset_'+rivet01)
    


                            
    #____Connect____:
    cmds.connectAttr(rivet01+'.worldMatrix[0]',MultMTX_Offset+'.matrixIn[0]')
    cmds.connectAttr(CTRL+'.worldInverseMatrix[0]',MultMTX_Offset+'.matrixIn[1]')
    cmds.connectAttr(MultMTX_Offset+'.matrixSum',DecMTX_Offset+'.inputMatrix')
    cmds.disconnectAttr (MultMTX_Offset+'.matrixSum',DecMTX_Offset+'.inputMatrix')
    cmds.delete(MultMTX_Offset)
    
    cmds.connectAttr(DecMTX_Offset+'.inputMatrix',MultMTX+'.matrixIn[0]')
    cmds.connectAttr(CTRL+'.worldMatrix[0]',MultMTX+'.matrixIn[1]')
    cmds.connectAttr(rivet01+'.parentInverseMatrix[0]',MultMTX+'.matrixIn[2]')
    cmds.connectAttr(MultMTX+'.matrixSum',DecMTX+'.inputMatrix')
    
    cmds.connectAttr(DecMTX+'.outputScale',rivet01+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet02+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet03+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet04+'.s')
    cmds.connectAttr(DecMTX+'.outputScale',rivet05+'.s')

    
    
    #____END MOTHER FUCKER____#
    
    #Eh non, c'etait un prank! On continu____#
    
    #____Connexion des Ribbons au body____#
  
#____Creation du Bend Ribbon:____#

#____VARS____:
    if radc == 'arm_right' :
        cmds.circle(n='CTRL_Bend_Elbow_R') 
        Bend = 'CTRL_Bend_Elbow_R'
        CtrlGUp = 'CTRL_General_Ribbon_Shoulder_R_01'
        CtrlUp1 = 'CTRL_Ribbon_Shoulder_R_A01'
        CtrlUp2 = 'CTRL_Ribbon_Shoulder_R_B01'
        CtrlGDown = 'CTRL_General_Ribbon_Forearm_R_01'
        CtrlDown1 = 'CTRL_Ribbon_Forearm_R_A01'
        CtrlDown2 = 'CTRL_Ribbon_Forearm_R_B01'
        DrvJntUp = 'DrvJnt_Shoulder_R'
        DrvJntMid = 'DrvJnt_Elbow_R'
        DrvJntEnd = 'DrvJnt_Wrist_R'
        PreservJnt = 'Bind_Elbow_Preserve_R'
        Ctrl = 'CTRL_Arm_R'
        CtrlFKUp = 'CTRL_Shoulder_R'
        CtrlFKEnd = 'CTRL_Wrist_R'
        Twist = 'CTRL_Arm_R.Twist_Arm_R'
        IKFK = 'CTRL_Switch_R.IK_FK_R_Arm'
        
    if radc == 'arm_left' :
        cmds.circle(n='CTRL_Bend_Elbow_L')
        Bend = 'CTRL_Bend_Elbow_L'
        CtrlGUp = 'CTRL_General_Ribbon_Shoulder_L_01'
        CtrlUp1 = 'CTRL_Ribbon_Shoulder_L_B01'
        CtrlUp2 = 'CTRL_Ribbon_Shoulder_L_A01'
        CtrlGDown = 'CTRL_General_Ribbon_Forearm_L_01'
        CtrlDown1 = 'CTRL_Ribbon_Forearm_L_B01'
        CtrlDown2 = 'CTRL_Ribbon_Forearm_L_A01'
        DrvJntUp = 'DrvJnt_Shoulder_L'
        DrvJntMid = 'DrvJnt_Elbow_L'
        DrvJntEnd = 'DrvJnt_Wrist_L'
        PreservJnt = 'Bind_Elbow_Preserve_L'
        Ctrl = 'CTRL_Arm_L'
        CtrlFKUp = 'CTRL_Shoulder_L'
        CtrlFKEnd = 'CTRL_Wrist_L'
        Twist = 'CTRL_Arm_L.Twist_Arm_L'
        IKFK = 'CTRL_Switch_L.IK_FK_L_Arm'
        
    
        
    if radc == 'arm_left' or radc == 'arm_right':
#____Connect Ribbon____:        
        cmds.matchTransform(Bend,DrvJntMid)
        cmds.createNode('transform', n=Bend+'Offset')
        cmds.matchTransform(Bend+'Offset',Bend)
        cmds.parent(Bend,Bend+'Offset')

        cmds.parentConstraint(DrvJntUp,Bend, mo=True)
        cmds.parentConstraint(Bend, PreservJnt, sr=["x","z"])
        
        #____Connect Ribbon Up____:
        cmds.pointConstraint(DrvJntMid, DrvJntUp, CtrlGUp)
        cmds.orientConstraint(DrvJntUp, CtrlGUp)
        cmds.pointConstraint(DrvJntUp,CtrlUp1)
        cmds.parentConstraint(PreservJnt,CtrlUp2, sr=["x","z"])
        #____Connect Ribbon Down____:
        cmds.pointConstraint(DrvJntEnd, DrvJntMid, CtrlGDown)
        cmds.orientConstraint(DrvJntMid, CtrlGDown)
        cmds.pointConstraint(DrvJntEnd,CtrlDown2)
        cmds.parentConstraint(PreservJnt,CtrlDown1, sr=["x","z"])
        
        #____Connect Twist Ribbon____: 
            #____Create Nodes____:
        
        MultFK_Up= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_FK_Mult_'+side_S)
        MultIK_Up= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_IK_Mult_'+side_S)
        Cond_Up= cmds.shadingNode('condition', asUtility=True, n='Cond_Ribbon_'+side_S)
        
        MultFK_Down= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_FK_Mult_'+side_F)
        MultIK_Down= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_IK_Mult_'+side_F)
        PMA_Down= cmds.shadingNode('plusMinusAverage',asUtility=True, n='PMA_Ribbon_'+side_F)
        Cond_Down= cmds.shadingNode('condition', asUtility=True, n='Cond_Ribbon_'+side_F)
        
        #____Set Nodes____:
        
        if radc== 'arm_left' :
            cmds.setAttr(MultFK_Up+'.input2X', -1)
            cmds.setAttr(MultIK_Up+'.input2X', -1)
            cmds.setAttr (Cond_Up+'.operation', 0)
            
            cmds.setAttr(MultIK_Down+'.input2X', -1)
            cmds.setAttr (Cond_Down+'.operation', 0)
            cmds.setAttr (PMA_Down+'.operation', 1)
            
        if radc== 'arm_right' :
            cmds.setAttr(MultFK_Up+'.input2X', 1)
            cmds.setAttr(MultIK_Up+'.input2X', 1)
            cmds.setAttr (Cond_Up+'.operation', 0)
            
            cmds.setAttr(MultIK_Down+'.input2X', -1)
            cmds.setAttr(MultFK_Down+'.input2X', -1)
            cmds.setAttr (Cond_Down+'.operation', 0)
            cmds.setAttr (PMA_Down+'.operation', 2)
        
        #Connect Nodes Up____:
            
        cmds.connectAttr(CtrlFKUp+'.rotateX', MultFK_Up+'.input1X')
        cmds.connectAttr(MultFK_Up+'.outputX', Cond_Up+'.colorIfFalseR')
        cmds.connectAttr(Twist,MultIK_Up+'.input1X')
        cmds.connectAttr(MultIK_Up+'.outputX',Cond_Up+'.colorIfTrueR')
        cmds.connectAttr(IKFK, Cond_Up+'.firstTerm')
        cmds.connectAttr(Cond_Up+'.outColorR',CtrlUp1+'.rotateX')
        
        #Connect Nodes Down____:
            
        cmds.connectAttr(CtrlFKEnd+'.rotateX', MultFK_Down+'.input1X')
        cmds.connectAttr(MultFK_Down+'.outputX', Cond_Down+'.colorIfFalseR')
        cmds.connectAttr(Twist,MultIK_Down+'.input1X')
        cmds.connectAttr(MultIK_Up+'.outputX',PMA_Down+'.input1D[0]')
        cmds.connectAttr(Ctrl+'.rotateX',PMA_Down+'.input1D[1]')
        cmds.connectAttr(PMA_Down+'.output1D',Cond_Down+'.colorIfTrueR')
        cmds.connectAttr(IKFK, Cond_Down+'.firstTerm')
        cmds.connectAttr(Cond_Down+'.outColorR',CtrlDown2+'.rotateX')

        if radc == 'arm_left':
            cmds.connectAttr(Ctrl+'.Bend_Arm_L', Bend+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Arm_L', 'CTRL_Ribbon_Shoulder_L_Mid'+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Arm_L', 'CTRL_Ribbon_Forearm_L_Mid'+'.visibility')
            cmds.setAttr('ExtraNodes_To_Hide_Shoulder_L.visibility',0)
            cmds.setAttr('ExtraNodes_To_Hide_Forearm_L.visibility',0)
            cmds.parent('Ribbon_Shoulder_L', 'ExtraNodes_To_Show')
            cmds.parent('Ribbon_Forearm_L', 'ExtraNodes_To_Show')
            cmds.parent('CTRL_Bend_Elbow_LOffset', 'Ctrl_01')
            
        if radc == 'arm_right':
            cmds.connectAttr(Ctrl+'.Bend_Arm_R', Bend+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Arm_R', 'CTRL_Ribbon_Shoulder_R_Mid'+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Arm_R', 'CTRL_Ribbon_Forearm_R_Mid'+'.visibility')
            cmds.setAttr('ExtraNodes_To_Hide_Shoulder_R.visibility',0)
            cmds.setAttr('ExtraNodes_To_Hide_Forearm_R.visibility',0)
            cmds.parent('Ribbon_Shoulder_R', 'ExtraNodes_To_Show')
            cmds.parent('Ribbon_Forearm_R', 'ExtraNodes_To_Show')
            cmds.parent('CTRL_Bend_Elbow_ROffset', 'Ctrl_01')
     


#____LEGS_________________________:
  
#____Creation du Bend Ribbon:____#

#____VARS____:
        
    if radc == 'leg_right' :
        cmds.circle(n='CTRL_Bend_Knee_R') 
        Bend = 'CTRL_Bend_Knee_R'
        CtrlGUp = 'CTRL_General_Ribbon_Leg_R_01'
        CtrlUp1 = 'CTRL_Ribbon_Leg_R_B01'
        CtrlUp2 = 'CTRL_Ribbon_Leg_R_A01'
        CtrlGDown = 'CTRL_General_Ribbon_Knee_R_01'
        CtrlDown1 = 'CTRL_Ribbon_Knee_R_B01'
        CtrlDown2 = 'CTRL_Ribbon_Knee_R_A01'
        DrvJntUp = 'DrvJnt_Leg_R'
        DrvJntMid = 'DrvJnt_Knee_R'
        DrvJntEnd = 'DrvJnt_Ankle_R'
        PreservJnt = 'Bind_Knee_Preserve_R'
        Ctrl = 'CTRL_Leg_R'
        CtrlFKUp = 'CTRL_Thigh_R'
        CtrlFKEnd = 'CTRL_Ankle_R'
        Twist = 'CTRL_Leg_R.Twist_Leg_R'
        IKFK = 'CTRL_Switch_Leg_R.IK_FK_R_Leg'
        
    if radc == 'leg_left' :
        cmds.circle(n='CTRL_Bend_Knee_L')
        Bend = 'CTRL_Bend_Knee_L'
        CtrlGUp= 'CTRL_General_Ribbon_Leg_L_01'
        CtrlUp1 = 'CTRL_Ribbon_Leg_L_B01'
        CtrlUp2 = 'CTRL_Ribbon_Leg_L_A01'
        CtrlGDown= 'CTRL_General_Ribbon_Knee_L_01'
        CtrlDown1 = 'CTRL_Ribbon_Knee_L_B01'
        CtrlDown2 = 'CTRL_Ribbon_Knee_L_A01'
        DrvJntUp = 'DrvJnt_Leg_L'
        DrvJntMid = 'DrvJnt_Knee_L'
        DrvJntEnd = 'DrvJnt_Ankle_L'
        PreservJnt = 'Bind_Knee_Preserve_L'
        Ctrl = 'CTRL_Leg_L'
        CtrlFKUp = 'CTRL_Thigh_L'
        CtrlFKEnd = 'CTRL_Ankle_L'
        Twist = 'CTRL_Leg_L.Twist_Leg_L'
        IKFK = 'CTRL_Switch_Leg_L.IK_FK_L_Leg'
        
    if radc == 'leg_left' or radc == 'leg_right':
#____Connect Ribbon____:        
        cmds.matchTransform(Bend,DrvJntMid)
        cmds.createNode('transform', n=Bend+'Offset')
        cmds.matchTransform(Bend+'Offset',Bend)
        cmds.parent(Bend,Bend+'Offset')

        cmds.parentConstraint(DrvJntUp,Bend, mo=True)
        cmds.parentConstraint(Bend, PreservJnt, sr=["y","z"])
      
        if radc == 'leg_right':
            
            cmds.setAttr('Ribbon_BShp_Surface_Leg_R_01'+'.rotateY', -90)
            cmds.setAttr('Ribbon_Surface_Leg_R_01'+'.rotateY', -90)

            cmds.setAttr('Ribbon_BShp_Surface_Knee_R_01'+'.rotateY', -90)
            cmds.setAttr('Ribbon_Surface_Knee_R_01'+'.rotateY', -90)
            
            
        if radc == 'leg_left':
            
            cmds.setAttr('Ribbon_BShp_Surface_Leg_L_01'+'.rotateY', -90)
            cmds.setAttr('Ribbon_Surface_Leg_L_01'+'.rotateY', -90)
        
            cmds.setAttr('Ribbon_BShp_Surface_Knee_L_01'+'.rotateY', -90)
            cmds.setAttr('Ribbon_Surface_Knee_L_01'+'.rotateY', -90)
        
            
        #____Connect Ribbon Up____:
        cmds.pointConstraint(DrvJntMid, DrvJntUp, CtrlGUp)
        cmds.orientConstraint(DrvJntUp, CtrlGUp)
        cmds.pointConstraint(DrvJntUp,CtrlUp1)
        cmds.parentConstraint(PreservJnt,CtrlUp2, sr=["y","z"])
        #____Connect Ribbon Down____:
        cmds.pointConstraint(DrvJntEnd, DrvJntMid, CtrlGDown)
        cmds.orientConstraint(DrvJntMid, CtrlGDown)
        cmds.pointConstraint(DrvJntEnd,CtrlDown2)
        cmds.parentConstraint(PreservJnt,CtrlDown1, sr=["y","z"])
        

        #____Connect Twist Ribbon____: 
            #____Create Nodes____:
        
        MultFK_Up= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_FK_Mult_'+side_S)
        MultIK_Up= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_IK_Mult_'+side_S)
        Cond_Up= cmds.shadingNode('condition', asUtility=True, n='Cond_Ribbon_'+side_S)
        
        MultFK_Down= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_FK_Mult_'+side_F)
        MultIK_Down= cmds.shadingNode('multiplyDivide',asUtility=True, n='Ribbon_IK_Mult_'+side_F)
        PMA_Down= cmds.shadingNode('plusMinusAverage',asUtility=True, n='PMA_Ribbon_'+side_F)
        Cond_Down= cmds.shadingNode('condition', asUtility=True, n='Cond_Ribbon_'+side_F)
        
        #____Set Nodes____:
         
           
        if radc== 'leg_right' :  
            cmds.setAttr(MultFK_Up+'.input2X', -1)
            cmds.setAttr(MultIK_Up+'.input2X', -1)
            cmds.setAttr (Cond_Up+'.operation', 0)
                
            cmds.setAttr(MultIK_Down+'.input2X', -1)
            cmds.setAttr (Cond_Down+'.operation', 0)
            cmds.setAttr (PMA_Down+'.operation', 2)
                
        if radc== 'leg_left' :
            cmds.setAttr(MultFK_Up+'.input2X', -1)
            cmds.setAttr(MultIK_Up+'.input2X', -1)
            cmds.setAttr (Cond_Up+'.operation', 0)
                
            cmds.setAttr(MultIK_Down+'.input2X', -1)
            cmds.setAttr(MultFK_Down+'.input2X', 1)
            cmds.setAttr (Cond_Down+'.operation', 0)
            cmds.setAttr (PMA_Down+'.operation', 2)
        
        #Connect Nodes Up____:
            
        cmds.connectAttr(CtrlFKUp+'.rotateX', MultFK_Up+'.input1X')
        cmds.connectAttr(MultFK_Up+'.outputX', Cond_Up+'.colorIfFalseR')
        cmds.connectAttr(Twist,MultIK_Up+'.input1X')
        cmds.connectAttr(MultIK_Up+'.outputX',Cond_Up+'.colorIfTrueR')
        cmds.connectAttr(IKFK, Cond_Up+'.firstTerm')

        cmds.connectAttr(Cond_Up+'.outColorR',CtrlUp1+'.rotateX')
        
        #Connect Nodes Down____:
            
        cmds.connectAttr(CtrlFKEnd+'.rotateX', MultFK_Down+'.input1X')
        cmds.connectAttr(MultFK_Down+'.outputX', Cond_Down+'.colorIfFalseR')
        cmds.connectAttr(Twist,MultIK_Down+'.input1X')
        cmds.connectAttr(MultIK_Up+'.outputX',PMA_Down+'.input1D[0]')
        cmds.connectAttr(Ctrl+'.rotateY',PMA_Down+'.input1D[1]')
        cmds.connectAttr(PMA_Down+'.output1D',Cond_Down+'.colorIfTrueR')
        cmds.connectAttr(IKFK, Cond_Down+'.firstTerm')
        
        cmds.connectAttr(Cond_Down+'.outColorR',CtrlDown2+'.rotateX')  
        
        if radc == 'leg_left':
            cmds.connectAttr(Ctrl+'.Bend_Leg_L', Bend+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Leg_L', 'CTRL_Ribbon_Leg_L_Mid'+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Leg_L', 'CTRL_Ribbon_Knee_L_Mid'+'.visibility')
            cmds.setAttr('ExtraNodes_To_Hide_Leg_L.visibility',0)
            cmds.setAttr('ExtraNodes_To_Hide_Knee_L.visibility',0)
            cmds.parent('Ribbon_Knee_L', 'ExtraNodes_To_Show')
            cmds.parent('Ribbon_Leg_L', 'ExtraNodes_To_Show')
            cmds.parent('CTRL_Bend_Knee_LOffset', 'Ctrl_01')
            
        if radc == 'leg_right':
            cmds.connectAttr(Ctrl+'.Bend_Leg_R', Bend+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Leg_R', 'CTRL_Ribbon_Leg_R_Mid'+'.visibility')
            cmds.connectAttr(Ctrl+'.Bend_Leg_R', 'CTRL_Ribbon_Knee_R_Mid'+'.visibility')
            cmds.setAttr('ExtraNodes_To_Hide_Leg_R.visibility',0)
            cmds.setAttr('ExtraNodes_To_Hide_Knee_R.visibility',0)
            cmds.parent('Ribbon_Knee_R', 'ExtraNodes_To_Show')
            cmds.parent('Ribbon_Leg_R', 'ExtraNodes_To_Show')
            cmds.parent('CTRL_Bend_Knee_ROffset', 'Ctrl_01')

     
#___C'EST FINIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII____#


window= cmds.window( t="Auto Ribbon",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 120) )
mainw = cmds.formLayout()

nm = cmds.frameLayout( label='Quel membre?', labelAlign='center')
cmds.rowColumnLayout( p = nm, numberOfColumns=2, columnWidth=[(1, 125), (2, 125)] )

rc = cmds.radioCollection()
al = cmds.radioButton("arm_right", label='Arm Right', align='arm_Left', sl=1 )
ar = cmds.radioButton('arm_left', label='Arm Left', align='arm_right' )
ll = cmds.radioButton('leg_right', label='Leg Right', align='leg_Left' )
lr = cmds.radioButton('leg_left', label='Leg Left', align='leg_right' )


eylup = cmds.frameLayout( p= nm, label="Connections", labelAlign='center' )
cmds.button(l='Create Ribbon', align='center', c=CreateRibbon)



cmds.showWindow(window)