# Entradas

#Dados gerais
consumo_total_energia = 23332 #consumir do banco
irradiacao_local = 4.38
temperatura_minima_ambiente = 0.00
constante_gstc = 1.00
taxa_desempenho_sistema = 0.80

# Dados dos módulos
potencia_maxima_modulo = 400 #consumir do banco modulos
tensao_modulo_ca = 85.3 #consumir do banco modulos
corrente_cc = 5.9 #consumir do banco modulos

#Dados do inversor
potencia_maxima_inversor = 10000 #consumir do banco inversores
tensao_maxima_mppt = 480 #consumir do banco inversores
tensao_minima_mppt = 100 #consumir do banco inversores
corrente_maxima_mppt = 28.7897 #consumir do banco inversores
numero_mppt = 3 #consumir do banco inversores
quantidade_inversores = 2 #consumir do banco inversores

# Dados MPPT
capacidade_cc = 19200
capacidade_ca = 20000
numero_maximo_strings = 4
numero_maximo_strings = 5

# Dados dos arranjos | se tiver tudo 0 o mppt não será utilizado
numero_total_modulos = 48 #consumir do banco arranjos

#mppt 1
numero_strings_mppt1 = 2 #consumir do banco arranjos
numero_modulo_mppt1 = 4 #consumir do banco arranjos
azimute_mppt1 = 0 #consumir do banco arranjos
inclinacao_mppt1 = 0 #consumir do banco arranjos

#mppt 2
numero_strings_mppt2 = 2 #consumir do banco arranjos
numero_modulo_mppt2 = 4 #consumir do banco arranjos
azimute_mppt2 = 0 #consumir do banco arranjos
inclinacao_mppt2 = 0 #consumir do banco arranjos

#mppt 3
numero_strings_mppt3 = 2 #consumir do banco arranjos
numero_modulo_mppt3 = 4 #consumir do banco arranjos
azimute_mppt3 = 0 #consumir do banco arranjos
inclinacao_mppt3 = 0 #consumir do banco arranjos

#mppt 4
numero_strings_mppt4 = 0 #consumir do banco arranjos
numero_modulo_mppt4 = 0 #consumir do banco arranjos
azimute_mppt4 = 0 #consumir do banco arranjos
inclinacao_mppt4 = 0 #consumir do banco arranjos


# Critérios

# GERAÇÃO FOTOVOLTAICA
print('GERAÇÃO FOTOVOLTAICA')
if consumo_total_energia/12 > (numero_total_modulos*potencia_maxima_modulo*30*irradiacao_local*taxa_desempenho_sistema/(constante_gstc*1000)):
    notas_geracao = 'ADICIONAR MAIS MÓDULOS'
elif (numero_total_modulos*potencia_maxima_modulo*30*irradiacao_local*taxa_desempenho_sistema/(constante_gstc*1000))>1.2*consumo_total_energia/12:
    notas_geracao = 'REDUZIR MÓDULOS'
else:
    notas_geracao = 'VÁLIDA'

print('notas_geracao', notas_geracao)

min_geracao = consumo_total_energia
presente_geracao = (numero_total_modulos*potencia_maxima_modulo*30*irradiacao_local*taxa_desempenho_sistema/(constante_gstc*1000))*12
max_geracao = min_geracao*1.2
print('min_geracao ',min_geracao )
print('presente_geracao ',presente_geracao )
print('max_geracao ',max_geracao )

#POTÊNCIA DO INVERSOR
print('#POTÊNCIA DO INVERSOR ' )
if potencia_maxima_modulo*numero_total_modulos*0.8 > potencia_maxima_inversor*quantidade_inversores:
    notas_inversor = 'DIMENSIONAR INVERSOR DE MAIOR POTÊNCIA'
elif potencia_maxima_inversor*quantidade_inversores*0.8 > potencia_maxima_modulo*numero_total_modulos:
    notas_inversor = 'DIMENSIONAR INVERSOR DE MENOR POTÊNCIA'
else:
    notas_inversor = 'VÁLIDA'

print('notas_inversor ',notas_inversor )

min_inversor = numero_total_modulos*potencia_maxima_modulo*0.8
presente_inversor = potencia_maxima_inversor*quantidade_inversores
max_inversor = numero_total_modulos*potencia_maxima_modulo*1.2

print('min_inversor ',min_inversor )
print('presente_inversor ',presente_inversor )
print('max_inversor ',max_inversor )

# Validação de quantidade de MPPTs
print('# Validação de quantidade de MPPTs ' )

if numero_total_modulos != quantidade_inversores*(numero_strings_mppt1*numero_modulo_mppt1+numero_strings_mppt2*numero_modulo_mppt2+numero_strings_mppt3*numero_modulo_mppt3+numero_strings_mppt4*numero_modulo_mppt4):
    notas_mppts = 'NÚMERO DE MÓDULOS NOS ARRANJOS DIFERENTE DO NÚMERO DE MÓDULOS DEFINIDO PARA O SISTEMA'
elif numero_mppt == 1:
    if numero_strings_mppt2*numero_modulo_mppt2+numero_strings_mppt3*numero_modulo_mppt3+numero_strings_mppt4*numero_modulo_mppt4 == 0 and numero_strings_mppt1*numero_modulo_mppt1 > 0:
        notas_mppts = 'VÁLIDA'
    else:
        notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
elif numero_mppt == 2:
    if numero_strings_mppt3*numero_modulo_mppt3+numero_strings_mppt4*numero_modulo_mppt4 == 0 and numero_strings_mppt1*numero_modulo_mppt1 > 0 and numero_strings_mppt2*numero_modulo_mppt2 > 0:
        notas_mppts = 'VÁLIDA'
    else:
        notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
elif numero_mppt == 3:
    if numero_strings_mppt4*numero_modulo_mppt4 == 0 and numero_strings_mppt1*numero_modulo_mppt1 > 0 and numero_strings_mppt2*numero_modulo_mppt2 > 0 and numero_strings_mppt3*numero_modulo_mppt3 > 0:
        notas_mppts = 'VÁLIDA'
    else:
        notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
elif numero_strings_mppt1*numero_modulo_mppt1 != 0 and numero_strings_mppt3*numero_modulo_mppt3 != 0 and numero_strings_mppt3*numero_modulo_mppt3 != 0 and numero_strings_mppt4*numero_modulo_mppt4 != 0:
    notas_mppts = 'VÁLIDA'
else:
    notas_mppts = 'MÓDULOS DISPOSTOS INCORRETAMENTE NOS MPPTs'
print('notas_mppts ',notas_mppts )

# MPPT 1

# TENSÃO DE OPERAÇÃO NO MPPTs
print('# TENSÃO DE OPERAÇÃO NO MPPTs ' )
if numero_modulo_mppt1*tensao_modulo_ca > tensao_maxima_mppt:
    notas_tencao_mppt1 = 'REDUZIR MÓDULOS POR STRING'
elif tensao_modulo_ca*numero_modulo_mppt1 < tensao_minima_mppt:
    notas_tensao_mppt1 = 'ADICIONAR MAIS MÓDULOS POR STRING'
else:
    notas_tensao_mppt1 = 'VÁLIDA'
print('notas_tensao_mppt1 ',notas_tensao_mppt1 )

min_mppt1 = tensao_minima_mppt
presente_mppt1 = tensao_modulo_ca*numero_modulo_mppt1
max_mppt1 = tensao_maxima_mppt
print('min_mppt1 ',min_mppt1 )
print('presente_mppt1 ',presente_mppt1 )
print('max_mppt1 ',max_mppt1 )

# CORRENTE DE OPERAÇÃO NO MPPTs
print('# CORRENTE DE OPERAÇÃO NO MPPTs ' )
if corrente_cc*numero_strings_mppt1>corrente_maxima_mppt:
    notas_corrente_mppt1 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
else:
    notas_corrente_mppt1 = 'VÁLIDA'

print('notas_corrente_mppt1 ',notas_corrente_mppt1 )

# MPPT 2

# TENSÃO DE OPERAÇÃO NO MPPTs
print('# TENSÃO DE OPERAÇÃO NO MPPTs ' )
if numero_mppt > 1:
    if numero_mppt > 1:
        if numero_modulo_mppt2*tensao_modulo_ca > tensao_maxima_mppt:
            notas_tensao_mppt2 = 'REDUZIR MÓDULOS POR STRING'
        else:
            if tensao_modulo_ca*numero_modulo_mppt2 < tensao_minima_mppt:
                notas_tensao_mppt2 = 'ADICIONAR MAIS MÓDULOS POR STRING'
            else:
                notas_tensao_mppt2 = 'VÁLIDA'
    else:
        notas_tensao_mppt2 = 'VÁLIDA'
else:
    notas_tensao_mppt2 = 'VÁLIDA'

print('notas_tensao_mppt2 ',notas_tensao_mppt2 )

min_mppt2 = tensao_minima_mppt
presente_mppt2 = tensao_modulo_ca*numero_modulo_mppt2
max_mppt2 = tensao_maxima_mppt
print('min_mppt2 ',min_mppt2 )
print('presente_mppt2 ',presente_mppt2 )
print('max_mppt2 ',max_mppt2 )

# CORRENTE DE OPERAÇÃO NO MPPTs
print('# CORRENTE DE OPERAÇÃO NO MPPTs ' )
if numero_mppt > 1:
    if corrente_cc*numero_strings_mppt2 > corrente_maxima_mppt:
        notas_corrente_mppt2 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
    else:
        notas_corrente_mppt2 = 'VÁLIDA'
else: 
    notas_corrente_mppt2 = 'VÁLIDA'
print('notas_corrente_mppt2 ',notas_corrente_mppt2 )

# MPPT 3

# TENSÃO DE OPERAÇÃO NO MPPTs
print('# TENSÃO DE OPERAÇÃO NO MPPTs ' )
if numero_mppt > 2:
    if numero_modulo_mppt3*tensao_modulo_ca > tensao_maxima_mppt:
        notas_tensao_mppt3 = 'REDUZIR MÓDULOS POR STRING'
    else:
        if tensao_modulo_ca*numero_modulo_mppt3 < tensao_minima_mppt:
            notas_tensao_mppt3 = 'ADICIONAR MAIS MÓDULOS POR STRING'
        else:
            notas_tensao_mppt3 = 'VÁLIDA'
else:
    notas_tensao_mppt3 = 'VÁLIDA'
print('notas_tensao_mppt3 ',notas_tensao_mppt3 )

min_mppt3 = tensao_minima_mppt
presente_mppt3 = tensao_modulo_ca*numero_modulo_mppt3
max_mppt3 = tensao_maxima_mppt
print('min_mppt3 ',min_mppt3 )
print('presente_mppt3 ',presente_mppt3 )
print('max_mppt3 ',max_mppt3 )

# CORRENTE DE OPERAÇÃO NO MPPTs
print('# CORRENTE DE OPERAÇÃO NO MPPTs ' )
if numero_mppt > 2:
    if  corrente_cc*numero_strings_mppt3 > corrente_maxima_mppt:
        notas_corrente_mppt3 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
    else:
        notas_corrente_mppt3 = 'VÁLIDA'
else:
    notas_corrente_mppt3 = 'VÁLIDA'
print('notas_corrente_mppt3 ', notas_corrente_mppt3)

# MPPT 4

# TENSÃO DE OPERAÇÃO NO MPPTs
print('# TENSÃO DE OPERAÇÃO NO MPPTs ' )
if numero_mppt > 3:
    if numero_modulo_mppt4*tensao_modulo_ca > tensao_maxima_mppt:
        notas_tensao_mppt4 = 'REDUZIR MÓDULOS POR STRING'
    else:
        if tensao_modulo_ca*numero_modulo_mppt4 < tensao_minima_mppt:
            notas_tensao_mppt4 = 'ADICIONAR MAIS MÓDULOS POR STRING'
        else:
           notas_tensao_mppt4 = 'VÁLIDA' 
else:
    notas_tensao_mppt4 = 'VÁLIDA'
print('notas_tensao_mppt4 ',notas_tensao_mppt4 )

min_mppt4 = tensao_minima_mppt
presente_mppt4 = tensao_modulo_ca*numero_modulo_mppt4
max_mppt4 = tensao_maxima_mppt
print('min_mppt4 ',min_mppt4 )
print('presente_mppt4 ',presente_mppt4 )
print('max_mppt4 ',max_mppt4 )

# CORRENTE DE OPERAÇÃO NO MPPTs
print('# CORRENTE DE OPERAÇÃO NO MPPTs ' )
if numero_mppt > 3:
    if corrente_cc*numero_strings_mppt4 > corrente_maxima_mppt:
        notas_corrente_mppt4 = 'CORRENTE ELEVADA - REDUZIR QUANTIDADE DE STRINGS'
    else:
        notas_corrente_mppt4 = 'VÁLIDA'
else: 
    notas_corrente_mppt4 = 'VÁLIDA'

print('notas_corrente_mppt4 ',notas_corrente_mppt4 )