import math
from maya import cmds

SCL = 125
ratio = float(cmds.getAttr('.notes').strip())
hei = math.sqrt(cmds.polyEvaluate(area=True) / cmds.polyEvaluate(uvArea=True) / ratio)
print '%d x %d' % (round(SCL*hei*ratio), round(SCL*hei)),
