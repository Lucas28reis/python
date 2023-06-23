velocidade = 61
local_carro = 102


RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_rada_1 =  velocidade > RADAR_1
range_inicio =  local_carro >= (LOCAL_1 - RADAR_RANGE)
range_fim = local_carro <= (LOCAL_1 + RADAR_RANGE)


if range_inicio and range_fim and vel_carro_pass_rada_1:
    print('Carro multado em radar 1')

else:
    print('Carro dentro da velocidade')