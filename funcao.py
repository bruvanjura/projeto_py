import math

def calculate_velocity(target, current):
    # Vel (tupla): (Vx, Omega)
    vel = [0.0, 0.0]
    pos_rel = [target[0] - current[0], target[1] - current[1]]


    # math.atan2 lida com divisão por zero e corrige o quadrante do ângulo
    angle_real = math.atan2(pos_rel[1], pos_rel[0])
    aiming_angle = {'max': angle_real + math.radians(10),
                    'min': angle_real - math.radians(10),
                    'real': angle_real}

    #state 1
    if(current[2]>aiming_angle['max'] or  current[2]<aiming_angle['min']):
        erro = aiming_angle['real']-current[2]
        vel[1] = erro*0.1
        return vel
    
    return vel