import matplotlib.pyplot as plt 
import math
import numpy as np


import funcao 
initial_pose = (0,0,-np.pi/4)
target = (-1,1,3*np.pi/4)
vel = [0.0, 0.0]
pos_rel = [target[0] - initial_pose[0], target[1] - initial_pose[1]]

# Desenha o movimento considerando um passo de 0.1s
time = 0 
current = initial_pose

# ==========================================
# FIGURA 1 - TRAJETÓRIA 2D
# ==========================================
fig = plt.figure(1, figsize=(6, 6))
ax = fig.gca()

plt.title('Trajetória 2D - Rumo ao Alvo') 

# Câmera Inteligente: Enquadra tanto a origem do robô quanto o alvo
margem = 0.3
plt.xlim(min(initial_pose[0], target[0]) - margem, max(initial_pose[0], target[0]) + margem)
plt.ylim(min(initial_pose[1], target[1]) - margem, max(initial_pose[1], target[1]) + margem)

plt.xlabel('Eixo X (m)')
plt.ylabel('Eixo Y (m)')
plt.grid(True, linestyle='--', alpha=0.6)

# Trava a proporção visual do gráfico em 1:1
ax.set_aspect('equal', adjustable='box') 

# Desenha o Alvo
plt.plot(target[0], target[1], 'go', label='Alvo')

# Desenha o Círculo de Tolerância
raio_tol = 0.1
tolerance_circle = plt.Circle(
    (target[0], target[1]), 
    raio_tol, 
    edgecolor='g',          
    facecolor="#00ff0031",  
    fill=True,
    label='Tolerância'
)
ax.add_patch(tolerance_circle) 


# Cria o Vetor do Robô 
vetor_robo = plt.quiver(
    current[0], current[1], 
    np.cos(current[2]), np.sin(current[2]),
    color='r', scale=10,label='Frente do Robô'
)

# ==========================================
# FIGURA 2 - ORIENTAÇÃO X TEMPO
# ==========================================
plt.figure(2)
plt.title('Orientação (Theta) x Tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (°)')
plt.grid(True)
plt.plot(time, math.degrees(current[2]), 'b.')

# ==========================================
# LOOP DE TESTES
# ==========================================
dist = ((pos_rel[0])**2 + (pos_rel[1])**2)**(1/2)
theta_warped = math.atan2(np.sin(current[2]), np.cos(current[2]))

while plt.fignum_exists(1) and (dist > 0.1 or abs(theta_warped - target[2]) > 0.05):

    angle_real = math.atan2(pos_rel[1], pos_rel[0])
    dist = ((pos_rel[0])**2 + (pos_rel[1])**2)**(1/2)

    # Salva os estados anteriores para traçar uma linha até o próximo
    prev_current = current
    prev_time = time
    prev_error = angle_real - current[2]

    # Calcula Velocidade
    vel = funcao.calculate_velocity(target, current)

    # Calcula os Deltas
    dtheta = vel[1] * 0.1
    dx = vel[0] * np.cos(current[2] + dtheta/2) * 0.1
    dy = vel[0] * np.sin(current[2] + dtheta/2) * 0.1

    # Atualiza a Pose e o Tempo
    theta = current[2] + dtheta
    current = (current[0] + dx, current[1] + dy, theta)
    pos_rel = [target[0] - current[0], target[1] - current[1]]
    theta_warped = math.atan2(np.sin(current[2]), np.cos(current[2]))
    time += 0.1

    # Atualiza Figura 1 (Rastro e Seta)
    plt.figure(1)
    plt.plot([prev_current[0], current[0]], [prev_current[1], current[1]], 'k-') # Rastro preto
    
    vetor_robo.set_offsets([[current[0], current[1]]])
    vetor_robo.set_UVC(np.cos(current[2]), np.sin(current[2]))
    
    # Atualiza Figura 2 (Gráfico de Ângulo)
    plt.figure(2)
    plt.plot([prev_time, time], [math.degrees(prev_current[2]), math.degrees(current[2])], 'b-')
    
   
    
    # Print comentado pra debug
    #plt.pause(0.1) 
    print(f"Velocidade: {vel} \nTempo: {time:.1f} \nPose: {current}")

# ==========================================
# Salva As Figuras
# ==========================================
plt.figure(1)
plt.plot(initial_pose[0], initial_pose[1], 'ro', label='Posição inicial')
plt.legend(loc='upper right')
plt.savefig('Trajeto_caso3.png')

plt.figure(2)
plt.savefig('orientacao_caso3.png')

plt.show()