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
regra1 = ctrl.Rule(RS['ótima'] & VV['ótima'] & BA['alta'], recarga['baixa'])
regra2 = ctrl.Rule(RS['ótima'] & VV['ótima'] & BA['média'], recarga['média'])
regra3 = ctrl.Rule(RS['ótima'] & VV['ótima'] & BA['baixa'], recarga['alta'])

regra4 = ctrl.Rule(RS['boa'] & VV['boa'] & BA['alta'], recarga['baixa'])
regra5 = ctrl.Rule(RS['boa'] & VV['boa'] & BA['média'], recarga['média'])
regra6 = ctrl.Rule(RS['boa'] & VV['boa'] & BA['baixa'], recarga['média'])

regra7 = ctrl.Rule(RS['baixa'] & VV['baixa'] & BA['alta'], recarga['baixa'])
regra8 = ctrl.Rule(RS['baixa'] & VV['baixa'] & BA['média'], recarga['baixa'])
regra9 = ctrl.Rule(RS['baixa'] & VV['baixa'] & BA['baixa'], recarga['baixa'])

regra10 = ctrl.Rule(RS['ótima'] & VV['boa'] & BA['alta'], recarga['baixa'])
regra11 = ctrl.Rule(RS['ótima'] & VV['boa'] & BA['média'], recarga['média'])
regra12 = ctrl.Rule(RS['ótima'] & VV['boa'] & BA['baixa'], recarga['alta'])
regra13 = ctrl.Rule(RS['boa'] & VV['ótima'] & BA['alta'], recarga['baixa'])
regra14 = ctrl.Rule(RS['boa'] & VV['ótima'] & BA['média'], recarga['média'])
regra15 = ctrl.Rule(RS['boa'] & VV['ótima'] & BA['baixa'], recarga['alta'])

regra16 = ctrl.Rule(RS['ótima'] & VV['baixa'] & BA['alta'], recarga['baixa'])
regra17 = ctrl.Rule(RS['ótima'] & VV['baixa'] & BA['média'], recarga['baixa'])
regra18 = ctrl.Rule(RS['ótima'] & VV['baixa'] & BA['baixa'], recarga['baixa'])
regra19 = ctrl.Rule(RS['baixa'] & VV['ótima'] & BA['alta'], recarga['baixa'])
regra20 = ctrl.Rule(RS['baixa'] & VV['ótima'] & BA['média'], recarga['baixa'])
regra21 = ctrl.Rule(RS['baixa'] & VV['ótima'] & BA['baixa'], recarga['baixa'])

regra22 = ctrl.Rule(RS['boa'] & VV['baixa'] & BA['alta'], recarga['baixa'])
regra23 = ctrl.Rule(RS['boa'] & VV['baixa'] & BA['média'], recarga['baixa'])
regra24 = ctrl.Rule(RS['boa'] & VV['baixa'] & BA['baixa'], recarga['baixa'])
regra25 = ctrl.Rule(RS['baixa'] & VV['boa'] & BA['alta'], recarga['baixa'])
regra26 = ctrl.Rule(RS['baixa'] & VV['boa'] & BA['média'], recarga['baixa'])
regra27 = ctrl.Rule(RS['baixa'] & VV['boa'] & BA['baixa'], recarga['baixa'])

# Controlador
controlador = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10,
                                  regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18, regra19, regra20,
                                  regra21, regra22, regra23, regra24, regra25, regra26, regra27])
sistema = ctrl.ControlSystemSimulation(controlador)

# Defuzzificação
sistema.input['Radiação Solar'] = 10
sistema.input['Velocidade do Vento'] = 5.5
sistema.input['Bateria A'] = 3.0
sistema.compute()

print(sistema.output['Recarga'])
recarga.view(sim=sistema)
plt.show()