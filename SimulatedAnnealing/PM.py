import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
###########################
import AdaptiveControlSystem

###########################
###########################
xList = np.arange(0, 101, 1)
yList = xList
oldYList = None

def GetTrajectoryValue(x, pv):
    y = 2 * 0.0004 * (pv - 0.5) * x * (100 - x)
    return y

def GetTrajectoryValueList(xList, pv):
    yList = []
    for x in xList:
        y = GetTrajectoryValue(x, pv)
        yList.append(y)
    return yList

######################################################
######################################################
#"main"
print "HELLO! Think of a value between 0.0 and 1.0. Type 'exit' to stop"
cs = AdaptiveControlSystem.AdaptiveControlSystem()
#####################################################
plt.ion()
plt.xlim(0,100)
plt.ylim(-1,1)
si = 0
while True: #for ti in xrange(0, 20):
  print "step" + str(si) + ":"
  action = cs.GenerateNewAction("null")
  pValue = 0.5
  if (isinstance(action, AdaptiveControlSystem.Action) == True):
      pValue = action._paramValues[0]
  print "value = " + str(pValue)
  #print "step length = " + str(cs._kb[0]._stepLength)
  ########################
  #DRAWING
  ########################
  yList = GetTrajectoryValueList(xList, pValue)
  ########
  for ti in xrange (0, 126, 5):
      plt.clf()
      plt.xlim(0, 100)
      plt.ylim(-1, 1)
      plt.plot([0, 100], [0, 0], 'bo')
      #########
      if oldYList is not None:
          plt.plot(xList, oldYList, color='black')
      ########
      lastPi = min(101, ti)
      for pi in xrange (0, lastPi):
          dotSize = 12 - (ti - pi)/2
          if dotSize <= 3:
              dotSize = 3
          plt.plot(xList[pi], yList[pi], color='red', marker='o', linestyle='dashed', linewidth=2, markersize=dotSize)
      ########
      plt.pause(0.05)
  ########
  oldYList = yList
  #######################
  #EndOfDrawing
  #######################
  est = raw_input("User Estimation (+/-): ");
  est2 = 0
  if (est == "exit"):
      break
  if (est == "-"):
      est2 = -1
  else:
      est2 = +1
  cs.ReceiveRelativeEstimation(est2)
  print ""
  #############
  si += 1
#}while
############
plt.close()



      