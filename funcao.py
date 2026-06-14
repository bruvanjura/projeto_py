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

    vel = [0.0, 0.0]



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
    



    #State 2

    robo_apontando_destino = True


    distancia_local = (((target[0] - current[0]))**2 + (target[1] - current[1])**2)**(1/2)

    erro_x = (target[0] - current[0])/10
    erro_y = (target[1] - current[1])/10
    
    if robo_apontando_destino and current:
        vel[0] = 0.2
     

     





    return vel