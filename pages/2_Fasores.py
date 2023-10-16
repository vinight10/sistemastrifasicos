import streamlit as st
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np


st.header('Calculadora de Sistemas Trifásicos')
st.title('Fasores:')

'O fasor é um número complexo, na forma polar, que representa a amplitude e a fase de uma senóide.'
'Os fasores são uma maneira mais simples de se analisar circuitos alimentados por fontes senoidais (circuitos CA).'
'O que diferencia as fases de um sistema trifásico é seu ângulo de nascimento.'
'Em um sistema trifásico simétrico, o gerador possui mesmo módulo de tensão, variando em \u00B1 120° suas fases.'
'Desta forma, é possível identificar todas as fases a partir de um ângulo conhecido e de sua sequência de fase.'
st.markdown('Existem duas sequências de fases possíveis. A sequência **DIRETA**, designada como sequência ABC. Também pode ser designada como BCA ou CAB. Apenas desloca-se a letra inicial para o final. Depois repete-se a sequência, fazendo com que o sentido de giro seja **HORÁRIO**. A outra é a sequência **INVERSA**, conhecida como sequência ACB. Também pode ser CBA ou BAC. Para obter a sequência **INVERSA**, troca-se a fase B pela fase C e vice-versa. O sentido de giro continua sendo **ANTI-HORÁRIO**.')
st.markdown("Vale ressaltar ainda que, existe uma relação conhecida entre as tensões de fase e de linha do gerador (desde que o sistema seja simétrico) e da carga (desde que seja equilibrada), dada por \u221A 3 com ângulo de \u00B1 30°, dependendo da sequência de fase. Vamos nos ater a representação da sequência de fase considerando os fasores de um gerador simétrico. A calculadora abaixo retornará os valores dos fasores de tensão de fase e de linha em um sistema Y -Y. Em um sistema triângulo, as tensões de fase e de linha são as mesmas. De forma visual, no que tange aos fasores de tensão, existe uma regra onde o fasor referente a tensão de linha sempre 'chega primeiro' do que o de fase, independente do sentido de rotaçao, ou seja, ao analisar as tensões Van e Vab, conforme o sentido de fase escolhido, basta percorrer pelo gráfico e verificar que a tensão de linha sempre chega antes do que a de fase.")

# Função para converter módulo e ângulo em formato retangular
def polar_to_rect(magnitude, angle):
    angle_rad = math.radians(angle)
    rect = cmath.rect(magnitude, angle_rad)
    return rect

# Função para converter de retangular para polar em graus
def fasor(fas):
    fasorial = [abs(fas), math.degrees(cmath.phase(fas))]
    return fasorial

# Função para plotar os fasores com módulo e ângulo
def plotar_fasores_com_modulo_e_angulo(fasores):
    fig, ax = plt.subplots(subplot_kw={'projection':'polar'})
    plt.figure(figsize=(8, 8))
    
    # Função para plotar os fasores
    def plot_fasor(fasor, cor, label):
        magnitude, angulo = fasor
        rect = polar_to_rect(magnitude, angulo)
        angulo_rad = math.radians(angulo)
        ax.plot([0, angulo_rad], [0, magnitude], color=cor, linewidth=2, label=label)
    

    # Plotando os fasores para ESTRELA
    if 'Van' in angulo_tipo and 'Estrela' in ligacao:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Van')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vbn')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vcn')
        plot_fasor(fasor4, 'k', 'Vab')
        plot_fasor(fasor5, 'b','Vbc')
        plot_fasor(fasor6,'y','Vca')

    if 'Vbn' in angulo_tipo and 'Estrela' in ligacao:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vbn')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vcn')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Van')
        plot_fasor(fasor4, 'k', 'Vbc')
        plot_fasor(fasor5, 'b','Vca')
        plot_fasor(fasor6,'y','Vab')

    if 'Vcn' in angulo_tipo and 'Estrela' in ligacao:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vcn')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Van')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vbn')
        plot_fasor(fasor4, 'k', 'Vca')
        plot_fasor(fasor5, 'b','Vab')
        plot_fasor(fasor6,'y','Vbc')

    # Plotando os fasores para TRIÂNGULO

    if 'Vab' in angulo_tipo and 'Triângulo' in ligacao:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vab')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vbc')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vca')

    if 'Vbc' in angulo_tipo and 'Triângulo' in ligacao:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vbc')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vca')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vab')

    if 'Vca' in angulo_tipo and 'Triângulo' in ligacao:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vca')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vab')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vbc')



    # Definindo o título
    ax.set_title('Gráfico de Fasores')

    # Remover os rótulos do raio
    ax.set_yticklabels([])

    # Adicionando legenda
    legend = ax.legend(loc='upper right')
    legend.set_bbox_to_anchor((1.4, 1))

    st.pyplot(fig)

# Configuração da página Streamlit
st.title("Representação de Fasores de Tensão")
st.divider()

# Criação de colunas

col1, col2 = st.columns(2)

# Opção para escolher sequência de fase
with col1:
    seq_fase = st.radio("Sequência de Fase:", ("Direta", "Inversa"))

# Opção para escolher tipo de ligação
with col2:
    ligacao = st.radio("Tipo de Ligação: ", ('Estrela','Triângulo'))

# Entrada para o módulo do fasor
modulo = st.number_input("Módulo do Fasor (V):")

# Entrada para o ângulo inicial em graus
angulo_inicial = st.number_input("Ângulo Inicial (graus):")

# Selectbox para selecionar o tipo de tensão
if 'Estrela' in ligacao:
    angulo_tipo = st.selectbox("Ângulo pertence a:", ("Van", "Vbn", "Vcn"))
elif 'Triângulo' in ligacao:
    angulo_tipo = st.selectbox("Ângulo pertence a:", ("Vab", "Vbc", "Vca"))
# Botão para plotar os fasores
if st.button("Plotar Fasores"):

    # Definindo tensões de fase -  Y - Y

    if 'Van' in  angulo_tipo and 'Direta' in seq_fase:
        fasor1 = Van = [modulo,(angulo_inicial)]
        fasor2 = Vbn = [modulo,(angulo_inicial-120)]
        fasor3 = Vcn = [modulo,(angulo_inicial+120)]
    elif 'Van' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor1 = Van = [modulo,(angulo_inicial)]
        fasor2 = Vbn = [modulo,(angulo_inicial+120)]
        fasor3 = Vcn = [modulo,(angulo_inicial-120)]

    if 'Vbn' in  angulo_tipo and 'Direta' in seq_fase:
        fasor1 = Vbn = [modulo,(angulo_inicial)]
        fasor2 = Vcn = [modulo,(angulo_inicial-120)]
        fasor3 = Van = [modulo,(angulo_inicial+120)]
    elif 'Vbn' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor1 = Vbn = [modulo,(angulo_inicial)]
        fasor2 = Vcn = [modulo,(angulo_inicial+120)]
        fasor3 = Van = [modulo,(angulo_inicial-120)]

    if 'Vcn' in  angulo_tipo and 'Direta' in seq_fase:
        fasor1 = Vcn = [modulo,(angulo_inicial)]
        fasor2 = Van = [modulo,(angulo_inicial-120)]
        fasor3 = Vbn = [modulo,(angulo_inicial+120)]
    elif 'Vcn' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor1 = Vcn = [modulo,(angulo_inicial)]
        fasor2 = Van = [modulo,(angulo_inicial+120)]
        fasor3 = Vbn = [modulo,(angulo_inicial-120)]

    # Definindo tensões de linha -Y -Y 

    if 'Van' in  angulo_tipo and 'Direta' in seq_fase:
        fasor4 = Vab = [modulo*math.sqrt(3),(angulo_inicial+30)]
        fasor5 = Vbc = [modulo*math.sqrt(3),(angulo_inicial-90)]
        fasor6 = Vca = [modulo*math.sqrt(3),(angulo_inicial+150)]
    elif 'Van' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor4 = Vab = [modulo*math.sqrt(3),(angulo_inicial-30)]
        fasor5 = Vbc = [modulo*math.sqrt(3),(angulo_inicial+90)]
        fasor6 = Vca = [modulo*math.sqrt(3),(angulo_inicial-150)]

    if 'Vbn' in  angulo_tipo and 'Direta' in seq_fase:
        fasor4 = Vbc = [modulo*math.sqrt(3),(angulo_inicial+30)]
        fasor5 = Vca = [modulo*math.sqrt(3),(angulo_inicial-90)]
        fasor6 = Vab = [modulo*math.sqrt(3),(angulo_inicial+150)]
    elif 'Vbn' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor4 = Vbc = [modulo*math.sqrt(3),(angulo_inicial-30)]
        fasor5 = Vca = [modulo*math.sqrt(3),(angulo_inicial+90)]
        fasor6 = Vab = [modulo*math.sqrt(3),(angulo_inicial-150)]

    if 'Vcn' in  angulo_tipo and 'Direta' in seq_fase:
        fasor4 = Vca = [modulo*math.sqrt(3),(angulo_inicial+30)]
        fasor5 = Vab = [modulo*math.sqrt(3),(angulo_inicial-90)]
        fasor6 = Vbc = [modulo*math.sqrt(3),(angulo_inicial+150)]
    elif 'Vcn' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor4 = Vca = [modulo*math.sqrt(3),(angulo_inicial-30)]
        fasor5 = Vab = [modulo*math.sqrt(3),(angulo_inicial+90)]
        fasor6 = Vbc = [modulo*math.sqrt(3),(angulo_inicial-150)]

    # Definindo tensões de linha -Triângulo

    if 'Vab' in  angulo_tipo and 'Direta' in seq_fase:
        fasor1 = Van = [modulo,(angulo_inicial)]
        fasor2 = Vbn = [modulo,(angulo_inicial-120)]
        fasor3 = Vcn = [modulo,(angulo_inicial+120)]
    elif 'Vab' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor1 = Van = [modulo,(angulo_inicial)]
        fasor2 = Vbn = [modulo,(angulo_inicial+120)]
        fasor3 = Vcn = [modulo,(angulo_inicial-120)]

    if 'Vbc' in  angulo_tipo and 'Direta' in seq_fase:
        fasor1 = Vbn = [modulo,(angulo_inicial)]
        fasor2 = Vcn = [modulo,(angulo_inicial-120)]
        fasor3 = Van = [modulo,(angulo_inicial+120)]
    elif 'Vbc' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor1 = Vbn = [modulo,(angulo_inicial)]
        fasor2 = Vcn = [modulo,(angulo_inicial+120)]
        fasor3 = Van = [modulo,(angulo_inicial-120)]

    if 'Vca' in  angulo_tipo and 'Direta' in seq_fase:
        fasor1 = Vcn = [modulo,(angulo_inicial)]
        fasor2 = Van = [modulo,(angulo_inicial-120)]
        fasor3 = Vbn = [modulo,(angulo_inicial+120)]
    elif 'Vca' in  angulo_tipo and 'Inversa' in seq_fase:
        fasor1 = Vcn = [modulo,(angulo_inicial)]
        fasor2 = Van = [modulo,(angulo_inicial+120)]
        fasor3 = Vbn = [modulo,(angulo_inicial-120)]

    # Definindo dicionario de fasores comforme seleção
    
    if 'Estrela' in ligacao:
        fasores = [fasor1, fasor2, fasor3, fasor4, fasor5, fasor6]
    elif 'Triângulo' in ligacao:
        fasores = [fasor1, fasor2, fasor3]
   

    
    if 'Van' in angulo_tipo and 'Estrela' in ligacao:
        fasores_dict = {
            'Van': fasor1,
            'Vbn': fasor2,
            'Vcn': fasor3,
            'Vab': fasor4,
            'Vbc': fasor5,
            'Vca': fasor6
        }
    elif 'Vbn' in angulo_tipo and 'Estrela' in ligacao:
        fasores_dict = {
            'Vbn': fasor1,
            'Vcn': fasor2,
            'Van': fasor3,
            'Vbc': fasor4,
            'Vca': fasor5,
            'Vab': fasor6
        }
    elif 'Vcn' in angulo_tipo and 'Estrela' in ligacao:
        fasores_dict = {
            'Vcn': fasor1,
            'Van': fasor2,
            'Vbn': fasor3,
            'Vca': fasor4,
            'Vab': fasor5,
            'Vbc': fasor6
        }
    
    if 'Vab' in angulo_tipo and 'Triângulo' in ligacao:
        fasores_dict = {
            'Vab': fasor1,
            'Vbc': fasor2,
            'Vca': fasor3,       
        }
    elif 'Vbc' in angulo_tipo and 'Triângulo' in ligacao:
        fasores_dict = {
            'Vbc': fasor1,
            'Vca': fasor2,
            'Vab': fasor3,        
        }
    elif 'Vca' in angulo_tipo and 'Triângulo' in ligacao:
        fasores_dict = {
            'Vca': fasor1,
            'Vab': fasor2,
            'Vbc': fasor3
        }

    plotar_fasores_com_modulo_e_angulo(fasores)

    for nome, fasor in fasores_dict.items():
        modulo, angulo = fasor
        st.write(f"{nome}: Módulo = {modulo} V, Ângulo = {angulo}°")