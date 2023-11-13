import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image


st.header('Calculadora de Sistemas Trifásicos')

st.subheader('Sistema trifásico equilibrado em Triângulo')
''
''
image = Image.open('images/delta.png')
st.image(image, caption='Sistema Trifásico em Triângulo - Fonte: Introdução a sistemas elétricos de potência. 1. ed. São Paulo: Blucher, 2000. E-book. Disponível em: https://plataforma.bvirtual.com.br. Acesso em: 13 out. 2023.')

st.markdown('No tocante a geradores conectados em triângulo, Boylestad (2012, p.844) é enfático ao afirmar que “as tensões de fase e de linha são equivalentes e têm mesmo valor que as tensões induzidas nos enrolamentos do gerador. Ao observar o circuito verifica-se a ausência de neutro, sendo assim, para as ligações em triângulo, apenas três condutores são suficientes para alimentar a carga a partir do gerador. Ao observar o circuito verifica-se a ausência de neutro, sendo assim, para as ligações em triângulo, apenas três condutores são suficientes para alimentar a carga a partir do gerador. Também é possível afirmar que as tensões de fase e de linha em um sistema triângulo são iguais, enquanto, as correntes de linha e de fase obedecem a relação de \u221A 3 com ângulo de -30° quando a sequência é direta e de \u221A 3 com ângulo de +30° quando a sequência é inversa. ')
''
''

# Função para converter módulo e ângulo em formato retangular
def polar_to_rect(magnitude, angle):
    angle_rad = math.radians(angle)
    rect = cmath.rect(magnitude, angle_rad)
    return rect

# Função para converter de retangular para polar em graus
def fasor(fas):
    fasorial = [abs(fas), math.degrees(cmath.phase(fas))]
    return fasorial


# Dados de input do usuário
 
    # Pede ao usuário os dados do gerador   

st.markdown('Dados do Gerador:') 
''
''
Vgerador_modulo = st.number_input('Digite o módulo da tensão de linha do gerador conhecida (V): ', value = 220.00)
gerador_angulo = float (st.text_input('Digite o ângulo da tensão de linha do gerador conhecida (°): ', value = 0.00))
angulo_tipo = st.selectbox("Ângulo pertence a:", ("VAB", "VBC", "VCA"))
seq_fase = st.radio("Sequência de Fase:", ("Direta", "Inversa"))

''
''
    # Pede ao usuário os dados das impedâncias

st.markdown('Dados das impedâncias:')
Z_linha = complex(st.text_input("Digite o valor das impedâncias da rede (ZAA', ZBB', ZCC'), desprezando as mútuas (formato retangular [r+xj], em Ohms \u03A9):", value=0.2+0.15j ))
Z_carga = complex(st.text_input("Digite o valor das impedâncias da carga (ZA'B', ZB'C', ZC'A' em formato retangular [r+xj], em Ohms \u03A9):", value=3+4j ))
Z = (Z_carga)/3


if 'VAB' in angulo_tipo and 'Direta' in seq_fase:
    VAB = polar_to_rect(Vgerador_modulo, gerador_angulo)
    VBC = polar_to_rect(Vgerador_modulo, (gerador_angulo-120))
    VCA = polar_to_rect(Vgerador_modulo, (gerador_angulo+120))
    vab = [Vgerador_modulo, gerador_angulo]
    vbc = [Vgerador_modulo, (gerador_angulo - 120)]
    vca = [Vgerador_modulo, (gerador_angulo + 120)]
elif 'VAB' in angulo_tipo and 'Inversa' in seq_fase:
    VAB = polar_to_rect(Vgerador_modulo, (gerador_angulo))
    VBC = polar_to_rect(Vgerador_modulo, (gerador_angulo+120))
    VCA = polar_to_rect(Vgerador_modulo, (gerador_angulo-120))
    vab = (Vgerador_modulo, gerador_angulo)
    vbc = (Vgerador_modulo, (gerador_angulo + 120))
    vca = (Vgerador_modulo, (gerador_angulo - 120))

if 'VBC' in angulo_tipo and 'Direta' in seq_fase:
    VBC=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VCA=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    VAB=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    vbc = (Vgerador_modulo, gerador_angulo)
    vca = (Vgerador_modulo, (gerador_angulo - 120))
    vab = (Vgerador_modulo, (gerador_angulo + 120))
    
elif 'VBC' in angulo_tipo and 'Inversa' in seq_fase:
    VBC=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VCA=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    VAB=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    vbc = (Vgerador_modulo, gerador_angulo)
    vca = (Vgerador_modulo, (gerador_angulo + 120))
    vab = (Vgerador_modulo, (gerador_angulo - 120))


if 'VCA' in angulo_tipo and 'Direta' in seq_fase:
    VCA=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VAB=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    VBC=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    vca = (Vgerador_modulo, gerador_angulo)
    vab = (Vgerador_modulo, (gerador_angulo - 120))
    vbc = (Vgerador_modulo, (gerador_angulo + 120))

elif 'VCA' in angulo_tipo and 'Inversa' in seq_fase:
    VCA=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VAB=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    VBC=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    vca = (Vgerador_modulo, gerador_angulo)
    vab = (Vgerador_modulo, (gerador_angulo + 120))
    vbc = (Vgerador_modulo, (gerador_angulo - 120))

t_raiz_direta = polar_to_rect(math.sqrt(3),30)
t_raiz_inversa = polar_to_rect(math.sqrt(3),-30)
c_raiz_direta = polar_to_rect(math.sqrt(3),-30)
c_raiz_inversa = polar_to_rect(math.sqrt(3),+30)

if st.button('Calcular'):

    st.markdown('Resultados: ')
    
    if 'Direta' in seq_fase:    
        IAA = (VAB/t_raiz_direta)/(Z_linha+Z)
        IBB = (VBC/t_raiz_direta)/(Z_linha+Z)
        ICC = (VCA/t_raiz_direta)/(Z_linha+Z)
        IAB = (IAA/c_raiz_direta)
        IBC = (IBB/c_raiz_direta)
        ICA = (ICC/c_raiz_direta)
        VAN = (IAA*Z)
        VBN = (IBB*Z)
        VCN = (ICC*Z)
        V_A_B = (VAN*t_raiz_direta)
        V_B_C = (VBN*t_raiz_direta)
        V_C_A = (VCN*t_raiz_direta)

    elif 'Inversa' in seq_fase:
        IAA = (VAB/t_raiz_inversa)/(Z_linha+Z)
        IBB = (VBC/t_raiz_inversa)/(Z_linha+Z)
        ICC = (VCA/t_raiz_inversa)/(Z_linha+Z)
        IAB = (IAA/c_raiz_inversa)
        IBC = (IBB/c_raiz_inversa)
        ICA = (ICC/c_raiz_inversa)
        VAN = (IAA*Z)
        VBN = (IBB*Z)
        VCN = (ICC*Z)
        V_A_B = (VAN*t_raiz_inversa)
        V_B_C = (VBN*t_raiz_inversa)
        V_C_A = (VCN*t_raiz_inversa)

    ''
    'Tensões no Gerador: '
    st.write('---- MÓDULO (V) -----------------   ÂNGULO °')
    st.write(f"VAB: {(vab)}")
    st.write(f"VBC: {(vbc)}")
    st.write(f"VCA: {(vca)}")
    ''
    ''
    'Correntes de Linha: '
    st.write('------------ MÓDULO (A)    -----------------     ÂNGULO °')
    st.write(f"IAA': {fasor(IAA)}")
    st.write(f"IBB': {fasor(IBB)}")
    st.write(f"ICC': {fasor(ICC)}")  
    ''
    ''
    'Correntes de fase na carga: '
    st.write('------------ MÓDULO (A)   -----------------     ÂNGULO °')
    st.write(f"IA'B': {fasor(IAB)}")
    st.write(f"IB'C': {fasor(IBC)}")
    st.write(f"IC'A': {fasor(ICA)}")
    ''
    ''
    'Tensões sobre a carga: '
    st.write('------------ MÓDULO (V)   -----------------     ÂNGULO °')
    st.write(f"VA'B': {fasor(V_A_B)}")
    st.write(f"VB'C': {fasor(V_B_C)}")
    st.write(f"VC'A': {fasor(V_C_A)}")

    ''
    ''

    # Plotagem dos Gráficos

    # Criar a figura para tensão
    fig, ax = plt.subplots(subplot_kw={'projection':'polar'})
    plt.figure(figsize=(8, 8))

    # Função para plotar as tensões
    def plot_tensao(vetor, cor, label):
        angulo = cmath.phase(vetor)
        magnitude = abs(vetor)
        ax.plot([0, angulo], [0, magnitude], color=cor, linewidth=2, label=label)

    # Plotando as tensões
    plot_tensao(VAB, [0.8, 0.4, 0], 'VAB')
    plot_tensao(VBC, [0.4, 0.8, 0], 'VBC')
    plot_tensao(VCA, [0, 0.6, 0.8], 'VCA')
    plot_tensao(V_A_B, [0.6, 0.7, 0], "V A'B'")
    plot_tensao(V_B_C, 'm', "V B'C'")
    plot_tensao(V_C_A, 'k', "V C'A'")
    


    # Definindo o título
    ax.set_title('Gráfico das Tensões: ')

    # Remover os rótulos do raio
    ax.set_yticklabels([])

    # Adicionando legenda
    legend = ax.legend(loc='upper right')
    legend.set_bbox_to_anchor((1.3, 1))

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

    
    # Criar a figura para corrente
    fig, ax = plt.subplots(subplot_kw={'projection':'polar'})
    plt.figure(figsize=(8, 8))

    # Função para plotar as correntes
    def plot_corrente(vetor, cor, label):
        angulo = cmath.phase(vetor)
        magnitude = abs(vetor)
        ax.plot([0, angulo], [0, magnitude], color=cor, linewidth=2, label=label)

    # Plotando as correntes
    plot_corrente(IAA, [0.8, 0.4, 0], 'IAA')
    plot_corrente(IBB, [0.4, 0.8, 0], 'IBB')
    plot_corrente(ICC, [0, 0.6, 0.8], 'ICC')
    plot_corrente(IAB, [0.6, 0.7, 0], "I A'B'")
    plot_corrente(IBC, 'm', "I B'C'")
    plot_corrente(ICA, 'k', "I C'A'")
    
    
    # Definindo o título
    ax.set_title('Gráfico das Correntes do Circuito')

    # Remover os rótulos do raio
    ax.set_yticklabels([])

    # Adicionando legenda
    legend = ax.legend(loc='upper right')
    legend.set_bbox_to_anchor((1.3, 1))

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)