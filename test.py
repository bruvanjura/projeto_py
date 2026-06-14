import matplotlib.pyplot as plt
import numpy as np
import funcao

initial_pose = (1,1,0)
target_pose = (5,5,np.pi/2)
vel = [0.0, 0.0]

#desenha o movimento considerando um passo de 0.1s
time = 0
current = initial_pose

plt.figure(1)
plt.grid(True)
plt.axis('equal')
plt.plot(current[0],current[1],'ro')
plt.plot(target_pose[0],target_pose[1],'go')

while time < 60 and plt.fignum_exists(1):   
    vel = funcao.calculate_velocity(target_pose,current)
    dtheta = vel[1]*0.1
    dx = vel[0]*np.cos(current[2]+dtheta/2)*0.1
    dy = vel[0]*np.sin(current[2]+dtheta/2)*0.1

    current = (current[0]+dx, current[1]+dy, current[2]+dtheta)

    plt.plot(current[0],current[1],'ro')
    plt.pause(0.1)
    time += 0.1



plt.show()

