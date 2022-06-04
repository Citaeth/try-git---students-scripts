import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import sys
import math
import pymel.core as pm

"""
________________________________________________________________________________________________________________________________________
-------------
Script by Clement Wallez and Juliette Gueydan

Pour Babouche

But: Aller plus vite
  
________________________________________________________________________________________________________________________________________
"""

#Aide si t'es un debile!

def help_def (*args):
	cmds.window(title="Aled!", w = 350, h = 160, minimizeButton=False, maximizeButton=False)
	cmds.frameLayout(l="O scour!", marginHeight=10, marginWidth=10)
	cmds.setParent()
	cmds.text(("""Komment ke sa marche?
	    - Selectionner le mesh de l'oeil, appuies sur le bouton "Center Eye"!
	    - Creer des curves de tes paupieres en 1 Linear pour avoir 1 point pour chaques vertex de ta paupiere.
	    Une curve pour la paupiere du haut et une autre pour celle du bas!
	    - Selection ta curve de paupiere du haut puis celle du bas et appuies sur le bouton "Rigg Eyelid"."""), align="left", ww=True)
	cmds.showWindow()

def getUParam( pnt = [], crv = None):
    
    #prendre le paramettre de position de chaques locatoc sur la curve
    
    point = OpenMaya.MPoint(pnt[0],pnt[1],pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
    paramUtill=OpenMaya.MScriptUtil()
    paramPtr=paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point)
    if isOnCurve == True:
        
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    else :
        point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    
    param = paramUtill.getDouble(paramPtr)  
    return param

def getDagPath( objectName):
    
    if isinstance(objectName, list)==True:
        oNodeList=[]
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MDagPath()
        selectionList.getDagPath(0, oNode)
        return oNode
 
def setUp(*args):

    sys.path.append( "C:\Users\3D3\Documents\maya\2020\prefs\scripts\Toutafet\Karatys" )
    import atys_Set_Up_Scene
    
def createLocators(*args):

    radc = cmds.radioCollection(rc, q = True, sl= True)
    
    if radc == 'Arm' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Create_Locator_Arms

    if radc == 'Leg' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Create_Locator_Legs

    if radc == 'Head' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Create_Locator_Head

    if radc == 'FootMovement' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Create_Locator_FootMovement

    if radc == 'Hand' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Create_Locator_Hand

def riggSpine(*args):

    sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
    from Toutafet import atys_Auto_Spine_Window

def arm(*args):

    sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
    from Toutafet import atys_JntCTRL_Bras

def leg(*args):

    sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
    from Toutafet import atys_JntCTRL_Legs

def hand(*args):

    sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
    from Toutafet import atys_JntCTRL_Mains

def face(*args):

    sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
    from Toutafet import atys_JntCTRL_Face

def rigg(*args):

    radc = cmds.radioCollection(ab, q = True, sl= True)
    
    if radc == 'Arm' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Connect_Arms

    if radc == 'Hand' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Connect_Mains

    if radc == 'Leg' :
        sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
        from Toutafet import atys_Connect_Legs

def ribbon(*args):

    sys.path.append(r'C:\Users\user\Documents\maya\2018\prefs\scripts')
    from Toutafet import atys_Ribbon_Body



#window___________________________________________________________________________________________________________
    
	
window= cmds.window( t="AutoRigg_v01",mnb=False,mxb= False,s=False, menuBar=True ,widthHeight=(250, 750) )
mainw = cmds.formLayout()
nm = cmds.frameLayout( label='Set up scene', labelAlign='center')
cmds.columnLayout()

cmds.menu( label='Help', tearOff=True )
cmds.menuItem( l='Toutéxpliker?', c=help_def )
cmds.menuItem( divider=True )
cmds.menuItem( label='Quit' )

cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )
cmds.button(l='Set up', align='center', c=setUp)

cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )

nm = cmds.frameLayout( label='Create Locators', labelAlign='center')
cmds.columnLayout()
cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )

rc = cmds.radioCollection()
f = cmds.radioButton("Head", label='Head', align='center')

cmds.rowColumnLayout( p = nm, numberOfColumns=2, columnWidth=[(1, 125),(2,125)] )

a = cmds.radioButton("Arm", label='Arm', align='left' )
h = cmds.radioButton('Hand', label='Hand', align='right')

l = cmds.radioButton("Leg", label='Leg', align='left' )
fm = cmds.radioButton('FootMovement', label='Foot Movement', align='right' )


cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )
cmds.button(l='Create Locators', align='center', c=createLocators)

savestate = cmds.frameLayout( p= nm, label="You only have left side so..... ", labelAlign='center' )
savestate = cmds.frameLayout( p= nm, label="Spoiler group, duplicate -z and UNGROUP", labelAlign='center' )

rspine = cmds.frameLayout(p= nm, label="Create a curve from root to shoulder", labelAlign='center' )
cmds.button(l='Rigg Spine', align='center', c=riggSpine)

arms = cmds.frameLayout( p= nm, label="ONLY if you're done with all steps above ", labelAlign='center' )
cmds.button(l='Jnt/CTRL Arms', align='center', c=arm)

legs = cmds.frameLayout( p= nm, label="ONLY if you're done with all steps above ", labelAlign='center' )
cmds.button(l='Jnt/CTRL Legs', align='center', c=leg)

hands = cmds.frameLayout( p= nm, label="Peat and Repeat are in a boat", labelAlign='center' )
cmds.button(l='Jnt/CTRL Hands', align='center', c=hand)

head = cmds.frameLayout( p= nm, label="Peat and Repeat are in a boat", labelAlign='center' )
cmds.button(l='Jnt/CTRL Head', align='center', c=face)


nm = cmds.frameLayout( label='Finally what you really want', labelAlign='center')
cmds.columnLayout()
cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )


ab = cmds.radioCollection()
r = cmds.radioButton("Arm", label='Arm', align='lef' )
l = cmds.radioButton('Hand', label='Hand', align='right' )
r = cmds.radioButton("Leg", label='Leg', align='left' )


cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )
cmds.button(l='Rigg', align='center', c=rigg)

cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )

nm = cmds.frameLayout( label='AND because were that nice', labelAlign='center')
cmds.columnLayout()
cmds.rowColumnLayout( p = nm, numberOfColumns=1, columnWidth=[(1, 250)] )
cmds.button(l='Ribbon', align='center', c=ribbon)


cmds.showWindow(window)