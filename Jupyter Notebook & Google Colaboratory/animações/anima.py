
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np


# Angle of Rotation
ang = 180
ang_rad = (ang/180)*np.pi

# Rotation increment
inc = 10
ang_rad = ang_rad/inc

# Rotation matrix
R = np.eye(3)
R[0,0] = np.cos(ang_rad)
R[0,1] = -np.sin(ang_rad)
R[1,0] = np.sin(ang_rad)
R[1,1] = np.cos(ang_rad)

print('Rotation Matrix: \n',R)


pts0 = np.array([[3,1],[5,1],[5,3],[3,3],[3,1]])
#print('Points:\n ',pts0)


# Preparing the points to be in homogeneous coordinates

pts0 = pts0.T
pts0 = np.vstack([pts0,np.ones(pts0.shape[1])])
print('Points:\n ',pts0)

pts1 = pts0


# Ploting the original points as a red line 
plt.figure(figsize=[10,10])
ax0 = plt.axes()
ax0.plot(pts0[0,:],pts0[1,:],'r')
ax0.grid()
ax0.set_xlim(-10, 10)
ax0.set_ylim(-10, 10)
ax0.set_aspect('equal')
plt.pause(0.5)
  
  
# Rotating the points in an animation
for x in range(inc):
  plt.cla() 
  ax0.set_xlim(-10, 10)
  ax0.set_ylim(-10, 10)
  ax0.grid()
  pts1 = np.dot(R,pts1)
  ax0.plot(pts0[0,:],pts0[1,:],'r')
  # Ploting the new points as a blue line 
  ax0.plot(pts1[0,:],pts1[1,:],'--b')
  plt.pause(0.5)
  
  
 


ax0.plot(pts1[0,:],pts1[1,:],'--c')
plt.show()
