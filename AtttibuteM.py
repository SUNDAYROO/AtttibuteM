import maya.cmds as cmds

selected_objects = {}
showing_list_for = None

def ui():
    windowID = 'AttributeM'
    if cmds.window(windowID, ex=True):
        cmds.deleteUI(windowID)

    window = cmds.window(windowID, t='AttributeM', rtf=0, s=1, mnb=0, mxb=0)
    master = cmds.columnLayout()

    cmds.rowColumnLayout(nc=1)
    cmds.text(l='Create Attributes', h=25, bgc=[0.1, 0.1, 0.1])
    
    cmds.rowColumnLayout(nr=1)

    cmds.textField('custom', w=300, tx='please select mesh', ed=0)
#    cmds.symbolButton(i="arrowDown.png", w=30, c=showSelectedObjects)

    cmds.button(l='Select', w=40, c=selectButtonCommand)
    cmds.button(l='Clear', w=40, c=clearButtonCommand)
    cmds.button(l='Delete', w=40, c=delButtonCommand)
    cmds.setParent('..')
    
    cmds.textField('customAtt', w=400, text='AttributeName')
    cmds.setParent('..')
    
    cmds.textScrollList('objectScrollList', width=400, height=150, visible=False)

    cmds.setParent(master)
    cmds.showWindow(windowID)

def delButtonCommand(*args):
    customSetName = cmds.textField('customAtt', text=True, q=True)
    customSetName = customSetName.replace(' ', '_')
    selected = cmds.ls(sl=1, dag=True, leaf=True)
    
    if cmds.objExists(customSetName):
        cmds.delete(customSetName)
    cmds.textField('custom', e=True, tx='please select mesh')
    cmds.textScrollList('objectScrollList', e=True, removeAll=True)
    cmds.textScrollList('objectScrollList', e=True, visible=False)
    
    for obj in selected:
        if cmds.attributeQuery(customSetName, node=obj, exists=True):
            cmds.deleteAttr(obj, attribute=customSetName)

def clearButtonCommand(*args):
    customSetName = cmds.textField('customAtt', text=True, q=True)
    cmds.select(cl=True)
    cmds.textField('custom', e=True, tx='please select mesh')
    cmds.textField('customAtt', e=True, tx='')
    cmds.textScrollList('objectScrollList', e=True, removeAll=True)
    cmds.textScrollList('objectScrollList', e=True, visible=False)


def selectButtonCommand(*args):
    global showing_list_for
    selected = cmds.ls(sl=1, dag=True, leaf=True)
    sels_all = f'{len(selected)} objects selected'
    cmds.textField('custom', e=True, text=sels_all)
    customSetName = cmds.textField('customAtt', text=True, q=True)
    customSetName = customSetName.replace(' ', '_')
    
    if not customSetName:
        cmds.warning('Please type an attribute name.')
        cmds.confirmDialog(title='Warning', message='Please type an attribute name.', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK')        
        cmds.textField('custom', e=True, tx='please select mesh')
        return
    
    cmds.sets(selected, n=customSetName)
    showSelectedObjects()
    cmds.addAttr(selected, longName=customSetName, attributeType='float', defaultValue=1, keyable=True)

def showSelectedObjects(*args):
    global showing_list_for
    customSetName = cmds.textField('customAtt', text=True, q=True)
    customSetName = customSetName.replace(' ', '_')
        
    if showing_list_for == customSetName:
        cmds.textScrollList('objectScrollList', e=True, visible=False)
        showing_list_for = None
    else:
        selected = cmds.sets(customSetName, q=True) or []
        cmds.textScrollList('objectScrollList', e=True, removeAll=True)
        for obj in selected:
            cmds.textScrollList('objectScrollList', e=True, append=obj)
        cmds.textScrollList('objectScrollList', e=True, visible=True)

ui()
