import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definindo as variáveis de entrada e saída
RS = ctrl.Antecedent(np.arange(0, 11, 1), 'Radiação Solar')
VV = ctrl.Antecedent(np.arange(0, 11, 1), 'Velocidade do Vento')
BA = ctrl.Antecedent(np.arange(0, 11, 1), 'Bateria A')
recarga = ctrl.Consequent(np.arange(0, 11, 1), 'Recarga')

# Fuzzificação
RS['baixa'] = fuzz.trimf(RS.universe, [0, 0, 5])
RS['boa'] = fuzz.trimf(RS.universe, [0, 5, 10])
RS['ótima'] = fuzz.trimf(RS.universe, [5, 10, 10])

VV['baixa'] = fuzz.trimf(VV.universe, [0, 0, 5])
VV['boa'] = fuzz.trimf(VV.universe, [0, 5, 10])
VV['ótima'] = fuzz.trimf(VV.universe, [5, 10, 10])

BA['baixa'] = fuzz.trimf(BA.universe, [0, 0, 5])
BA['média'] = fuzz.trimf(BA.universe, [0, 5, 10])
BA['alta'] = fuzz.trimf(BA.universe, [5, 10, 10])

recarga['baixa'] = fuzz.trimf(recarga.universe, [0, 0, 5])
recarga['média'] = fuzz.trimf(recarga.universe, [0, 5, 10])
recarga['alta'] = fuzz.trimf(recarga.universe, [5, 10, 10])

# Regras de inferência
regra1 = ctrl.Rule(RS['ótima'] | VV['ótima'] | BA['baixa'], recarga['alta'])
regra2 = ctrl.Rule(RS['boa'] | VV['boa'] | BA['baixa'], recarga['média'])
regra3 = ctrl.Rule(RS['baixa'] | VV['baixa'] | BA['baixa'], recarga['baixa'])

# Controlador
controlador = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(controlador)

# Defuzzificação
sistema.input['Radiação Solar'] = 2.0
sistema.input['Velocidade do Vento'] = 2.0
sistema.input['Bateria A'] = 8.8
sistema.compute()

print(sistema.output['Recarga'])
recarga.view(sim=sistema)
plt.show() 