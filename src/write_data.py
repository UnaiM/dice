import json

from maya import cmds

for xfm in ('d4ah', 'd4bh', 'd6h', 'd8h', 'd10h', 'd12h', 'd20h'):
    data = {'hull': []}
    for i in range(cmds.polyEvaluate(xfm+'Shape', vertex=True)):
        data['hull'].append(cmds.xform('%sShape.vtx[%d]'%(xfm, i), q=True, translation=True))
    data['margin'] = cmds.getAttr(cmds.listConnections(xfm+'Shape', type='bulletRigidBodyShape', source=False)[0] + '.colliderShapeMargin')
    with open(R'C:\Users\Unai\Documents\dice\data\%s.json'%xfm[:-1], 'w') as f:
        json.dump(data, f, indent=2, separators=(',', ': '), sort_keys=True)
