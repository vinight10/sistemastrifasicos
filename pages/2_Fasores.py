import streamlit as st
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np


st.title('Fasores:')

'O fasor é um número complexo, na forma polar, que representa a amplitude e a fase de uma senóide.'
'Os fasores são uma maneira mais simples de se analisar circuitos alimentados por fontes senoidais (circuitos CA).'
'O que diferencia as fases de um sistema trifásico é seu ângulo de nascimento.'
'Em um sistema trifásico simétrico, o gerador possui mesmo módulo de tensão, variando em 120° suas fases.'
'Desta forma, é possível identificar todas as fases a partir de um ângulo conhecido e de sua sequência de fase.'
st.markdown('Existem duas sequências de fases possíveis. Uma é a sequência **DIRETA**, designada como sequência ABC. Também pode ser designada como BCA ou CAB. Apenas desloca-se a letra inicial para o final. Depois repete-se a sequência. A outra é a sequência **INVERSA**, conhecida como sequência ACB. Também pode ser CBA ou BAC. Para obter a sequência **INVERSA**, troca-se a fase B pela fase C e vice-versa. O sentido de giro continua sendo anti-horário.')

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
    

    # Plotando os fasores
    if 'Van' in  angulo_tipo and 'Direta' in seq_fase:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Van')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vbn')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vcn')
    elif 'Van' in  angulo_tipo and 'Inversa' in seq_fase:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Van')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vbn')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vcn')

    if 'Vbn' in  angulo_tipo and 'Direta' in seq_fase:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vbn')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vcn')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Van')
    elif 'Vbn' in  angulo_tipo and 'Inversa' in seq_fase:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vbn')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Vcn')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Van')

    if 'Vcn' in  angulo_tipo and 'Direta' in seq_fase:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vcn')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Van')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vbn')
    elif 'Vcn' in  angulo_tipo and 'Inversa' in seq_fase:
        plot_fasor(fasor1, [0.8, 0.4, 0], 'Vcn')
        plot_fasor(fasor2, [0.4, 0.8, 0], 'Van')
        plot_fasor(fasor3, [0, 0.6, 0.8], 'Vbn')


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

# Opção para escolher sequência de fase
seq_fase = st.radio("Sequência de Fase:", ("Direta", "Inversa"))

# Entrada para o módulo do fasor
modulo = st.number_input("Módulo do Fasor:")

# Entrada para o ângulo inicial em graus
angulo_inicial = st.number_input("Ângulo Inicial (graus):")

# Selectbox para selecionar o tipo de tensão
angulo_tipo = st.selectbox("Ângulo pertence a:", ("Van", "Vbn", "Vcn"))

# Botão para plotar os fasores
if st.button("Plotar Fasores"):

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

    fasores = [Van, Vbn, Vcn]

    
    if 'Van' in  angulo_tipo:
        fasores_dict = {
            'Van': fasor1,
            'Vbn': fasor2,
            'Vcn': fasor3
        }
    elif 'Vbn' in  angulo_tipo:
        fasores_dict = {
            'Vbn': fasor1,
            'Vcn': fasor2,
            'Van': fasor3
        }
    elif 'Vcn' in angulo_tipo:
        fasores_dict = {
            'Vcn': fasor1,
            'Van': fasor2,
            'Vbn': fasor3
        }
    

    plotar_fasores_com_modulo_e_angulo(fasores)

    for nome, fasor in fasores_dict.items():
        modulo, angulo = fasor
        st.write(f"{nome}: Módulo = {modulo}, Ângulo = {angulo} graus")