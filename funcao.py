import math

def calculate_velocity(target, current):

    """
    
    Retornar uma lista com velx e w

    Args:
        current (tuple): Tupla com valores posicionais x, y e orientação do atuais do robô
        target (tuple): Tupla com valores posicionais x, y e orientação objetiva do robô

    Returns:
        list: Lista com os valores de velocidadex e velocidade angular w do robô
    
        
    """
    # Vel (tupla): (Vx, Omega)
    vel = [0.0, 0.0]
    pos_rel = [target[0] - current[0], target[1] - current[1]]
    robo_apontando_destino = False
    distancia_local = ((pos_rel[0])**2 + (pos_rel[1])**2)**(1/2)

   
    # math.atan2 lida com divisão por zero e corrige o quadrante do ângulo
    angle_real = math.atan2(pos_rel[1], pos_rel[0])
    aiming_angle = {'max': angle_real + math.radians(10),
                    'min': angle_real - math.radians(10),
                    'real': angle_real}


    is_not_looking = (current[2]>aiming_angle['max'] or  current[2]<aiming_angle['min']) #True ou false

    #state 1 => Bota o ponto num campo de visão legal
    if(is_not_looking and distancia_local > 0.1):
        erro = aiming_angle['real']-current[2]
        if erro > math.pi:
            erro -= 2*math.pi
        elif erro < -math.pi:
            erro += 2*math.pi
        vel[1] = erro*0.3
    else:
        robo_apontando_destino = True
    
    #State 2
    if robo_apontando_destino:

        if distancia_local < 0.1:
            #State 3
            vel[0] = 0.0
            erro = target[2]-current[2]
            if erro > math.pi:
                erro -= 2*math.pi
            elif erro < -math.pi:
                erro += 2*math.pi

            if abs(target[2] - current[2]) < 0.05:
                vel[1] = 0.0
            else:
                vel[1] = erro*0.2

        else:
            erro = aiming_angle['real']-current[2] # => manter o ponto no campo de visão
            vel[1] = erro*0.2
            vel[0] = 0.5


    

    return vel