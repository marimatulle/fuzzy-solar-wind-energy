import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definindo as variáveis de entrada e saída
RS = ctrl.Antecedent(np.arange(0, 11, 1), 'Radiação Solar')
VV = ctrl.Antecedent(np.arange(0, 11, 1), 'Velocidade do Vento')
BA = ctrl.Antecedent(np.arange(0, 11, 1), 'Bateria A')
BB = ctrl.Antecedent(np.arange(0, 11, 1), 'Bateria B')
BC = ctrl.Antecedent(np.arange(0, 11, 1), 'Bateria C')
recarga = ctrl.Consequent(np.arange(0, 11, 1), 'Recarga')

# Fuzzificação
RS['baixo'] = fuzz.trimf(RS.universe, [0, 0, 5])
RS['médio'] = fuzz.trimf(RS.universe, [0, 5, 10])
RS['alto'] = fuzz.trimf(RS.universe, [5, 10, 10])

VV['baixo'] = fuzz.trimf(VV.universe, [0, 0, 5])
VV['médio'] = fuzz.trimf(VV.universe, [0, 5, 10])
VV['alto'] = fuzz.trimf(VV.universe, [5, 10, 10])

BA['baixo'] = fuzz.trimf(BA.universe, [0, 0, 5])
BA['médio'] = fuzz.trimf(BA.universe, [0, 5, 10])
BA['alto'] = fuzz.trimf(BA.universe, [5, 10, 10])

BB['baixo'] = fuzz.trimf(BB.universe, [0, 0, 5])
BB['médio'] = fuzz.trimf(BB.universe, [0, 5, 10])
BB['alto'] = fuzz.trimf(BB.universe, [5, 10, 10])

BC['baixo'] = fuzz.trimf(BC.universe, [0, 0, 5])
BC['médio'] = fuzz.trimf(BC.universe, [0, 5, 10])
BC['alto'] = fuzz.trimf(BC.universe, [5, 10, 10])

recarga['baixo'] = fuzz.trimf(recarga.universe, [0, 0, 5])
recarga['médio'] = fuzz.trimf(recarga.universe, [0, 5, 10])
recarga['alto'] = fuzz.trimf(recarga.universe, [5, 10, 10])

# Regras de inferência
regra1 = ctrl.Rule(RS['alto'] | VV['alto'] | BA['baixo'], recarga['alto'])
regra2 = ctrl.Rule(RS['médio'] | VV['médio'] | BB['baixo'], recarga['médio'])
regra3 = ctrl.Rule(RS['baixo'] | VV['baixo'] | BC['baixo'], recarga['baixo'])

# Adicionando regras para priorizar a bateria com menor carga
regra4 = ctrl.Rule(BA['baixo'] & (BB['médio'] | BB['alto']) & (BC['médio'] | BC['alto']), recarga['alto'])
regra5 = ctrl.Rule(BB['baixo'] & (BA['médio'] | BA['alto']) & (BC['médio'] | BC['alto']), recarga['médio'])
regra6 = ctrl.Rule(BC['baixo'] & (BA['médio'] | BA['alto']) & (BB['médio'] | BB['alto']), recarga['baixo'])

# Controlador
controlador = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6])
sistema = ctrl.ControlSystemSimulation(controlador)

# Defuzzificação
sistema.input['Radiação Solar'] = 6.5
sistema.input['Velocidade do Vento'] = 9.8
sistema.input['Bateria A'] = 2.2
sistema.input['Bateria B'] = 3.4
sistema.input['Bateria C'] = 4.1
sistema.compute()

print(sistema.output['Recarga'])
recarga.view(sim=sistema)
plt.show() 