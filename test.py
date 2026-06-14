import matplotlib.pyplot as plt
import math
import numpy as np
import funcao

initial_pose = (1,1,0)
target = (-5,-5,np.pi/2)
vel = [0.0, 0.0]
pos_rel = [target[0] - initial_pose[0], target[1] - initial_pose[1]]

#desenha o movimento considerando um passo de 0.1s
time = 0
current = initial_pose



plt.figure(1)
plt.title('Posição no espaço (x,y) x Tempo')
plt.xlabel('eixo X (m)')
plt.ylabel('eixo Y (m)')
plt.grid(True)
plt.plot(current[0],current[1],'ro')
plt.plot(target[0],target[1],'go')

plt.figure(2)
plt.title('Orientação (Theta) x Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (°)')
plt.grid(True)
plt.plot(time, current[2], 'b.')

plt.figure(3)
plt.title('Erro do controle')
plt.xlabel('Tempo')
plt.ylabel('Erro')
plt.grid(True)
plt.axhline(y=0, color='r', linestyle='-')



while time < 600 and plt.fignum_exists(1) and (pos_rel[0]**2 + pos_rel[1]**2)**(1/2) > 0.1:
   
    angle_real = math.atan2(pos_rel[1], pos_rel[0])


    # Salva os estados anteriores para traçar uma linha até o próximo
    prev_current = current
    prev_time = time
    prev_error = angle_real-current[2]

    #Calcula Velocidade
    vel = funcao.calculate_velocity(target,current)

    #Calcula os Deltas
    dtheta = vel[1]*0.1
    dx = vel[0]*np.cos(current[2]+dtheta/2)*0.1
    dy = vel[0]*np.sin(current[2]+dtheta/2)*0.1

    #Atualiza
    current = (current[0]+dx, current[1]+dy, current[2]+dtheta)
    pos_rel = [target[0] - current[0], target[1] - current[1]]
    time += 0.1

    #Plota
    erro = angle_real-current[2]
    
    plt.figure(1)
    plt.plot([prev_current[0], current[0]], [prev_current[1], current[1]], 'k-')
    
    plt.figure(2)
    plt.plot([prev_time, time], [math.degrees(prev_current[2]), math.degrees(current[2])], 'b-')
    
    plt.figure(3)
    plt.plot([prev_time,time],[math.degrees(prev_error),math.degrees(erro)],'k-')
    plt.pause(0.1)
    print(f"Velocidae:{vel}\nTime: {time}")

plt.show()
