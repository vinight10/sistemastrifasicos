import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.title('Calculadora de Sistemas Trifásicos')
''
st.subheader('Ligação Y-Y - Com carga qualquer e com impedâncias mútuas de rede')
''
''
image = Image.open('y-y.png')
st.image(image, caption='Sistema Trifásico - Fonte: Introdução a sistemas elétricos de potência. 1. ed. São Paulo: Blucher, 2000. E-book. Disponível em: https://plataforma.bvirtual.com.br. Acesso em: 13 out. 2023.')

'Dados do Gerador'
''
''
tipo_ligacao_gerador = st.radio(
    
    "O gerador possui mesmo módulo de tensão?",
    ['SIM','NÃO'] ,
    )

''
''
if 'SIM' in tipo_ligacao_gerador:
    Van_modulo = st.number_input('Digite o módulo da tensão de fase(V): ', value = None, placeholder='Digite aqui')
    Van_angle = st.number_input('Digite o ângulo da tensão de fase Van (graus): ', value = None, placeholder='Digite aqui')
    Vbn_angle = st.number_input('Digite o ângulo da tensão de fase Vbn (graus): ', value = None, placeholder='Digite aqui')
    Vcn_angle = st.number_input('Digite o ângulo da tensão de fase Vcn (graus): ', value = None, placeholder='Digite aqui')
    Vbn_modulo = Van_modulo
    Vcn_modulo = Van_modulo
elif 'NÃO' in tipo_ligacao_gerador:
    Van_modulo = st.number_input('Digite o módulo da tensão de fase Van (V): ', value=220)
    Van_angle = st.number_input('Digite o ângulo da tensão de fase Van (graus): ', value=0)
    Vbn_modulo = st.number_input('Digite o módulo da tensão de fase Vbn (V): ', value=250)
    Vbn_angle = st.number_input('Digite o ângulo da tensão de fase Vbn (graus): ', value=-120)
    Vcn_modulo = st.number_input('Digite o módulo da tensão de fase Vcn (V): ', value=230)
    Vcn_angle = st.number_input('Digite o ângulo da tensão de fase Vcn (graus): ', value=120)
''
''
''
'Dados da Matriz de impedâncias da Rede:'
''
''
# IMPEDÂNCIAS PRÓPRIAS
zp = st.radio(
    
    'Serão consideradas as impedâncias próprias?',
    ['Sim','Não'] ,
    
    )
if 'Sim' in zp:
   
    zp_igual = st.radio(
    'As impedâncias próprias possuem mesmo valor?',
    ['sim','não'] ,
    
    )
    if 'sim' in zp_igual:
      
        Zaa = complex(st.text_input('Digite o valor das impedâncias próprias (formato retangular [r+xj], em Ohms \u03A9):', value=0+0j ))
        Zbb = Zaa
        Zcc = Zaa


    elif 'não' in zp_igual:
       
        Zaa = complex(st.text_input('Digite a impedância própria Zaa (formato retangular, em Ohms \u03A9): ', value=0+0j))
        Zbb = complex(st.text_input('Digite a impedância própria Zbb (formato retangular, em Ohms \u03A9): ', value=0+0j))
        Zcc = complex(st.text_input('Digite a impedância própria Zcc (formato retangular, em Ohms \u03A9): ', value=0+0j))

elif 'Não' in zp:

    Zaa = 0
    Zbb = 0
    Zcc = 0

# IMPEDÂNCIAS MÚTUAS

zm = st.radio(
    
    'Serão consideradas as impedâncias próprias?',
    ['Sim ','Não '] ,
    
    )
if 'Sim ' in zm:
   
    zm_igual = st.radio(
    'As impedâncias próprias possuem mesmo valor?',
    ['sim ','não '] ,
    
    )
    if 'sim ' in zm_igual:
      
        Zab = complex(st.text_input('Digite o valor das impedâncias mútuas (formato retangular [r+xj], em Ohms \u03A9):', value=0+0j ))
        Zac = Zab
        Zba = Zab
        Zbc = Zab
        Zca = Zab
        Zcb = Zab


    elif 'não ' in zm_igual:
       
        Zab = complex(st.text_input('Digite a impedância mútua Zab (formato retangular [r+xj], em Ohms \u03A9): ', value=0+0j))
        Zac = complex(st.text_input('Digite a impedância mútua Zac (formato retangular [r+xj], em Ohms \u03A9): ', value=0+0j))
        Zba = complex(st.text_input('Digite a impedância mútua Zba (formato retangular [r+xj], em Ohms \u03A9): ', value=0+0j))
        Zbc = complex(st.text_input('Digite a impedância mútua Zbc (formato retangular [r+xj], em Ohms \u03A9): ', value=0+0j))
        Zca = complex(st.text_input('Digite a impedância mútua Zca (formato retangular [r+xj], em Ohms \u03A9): ', value=0+0j))
        Zcb = complex(st.text_input('Digite a impedância mútua Zcb (formato retangular [r+xj], em Ohms \u03A9): ', value=0+0j))

elif 'Não ' in zm:

    Zab = 0
    Zac = 0
    Zba = 0
    Zbc = 0
    Zca = 0
    Zcb = 0

""
""
'Dados de Impedância de Carga e de Neutro:'

ZA = complex(st.text_input('Digite a impedância da carga ZA (formato retangular, em Ohms \u03A9): ', value=0+0j))
ZB = complex(st.text_input('Digite a impedância da carga ZB (formato retangular, em Ohms \u03A9): ', value=0+0j))
ZC = complex(st.text_input('Digite a impedância da carga ZC (formato retangular, em Ohms \u03A9): ', value=0+0j))
ZN = complex(st.text_input('Digite a impedância de neutro ZN (formato retangular, em Ohms \u03A9): ', value=0+0j))


# Criação das matrizes de impedância
Z_matrix = np.array([[Zaa, Zab, Zac], [Zba, Zbb, Zbc], [Zca, Zcb, Zcc]])
Z_carga = np.diag([ZA, ZB, ZC]) + np.array([[ZN] * 3])
Z_total = Z_matrix + Z_carga


#Cálculos - Só executados quando usuario pressionar o botão 'calcular'

# Função para converter módulo e ângulo em formato retangular
def polar_to_rect(magnitude, angle):
    angle_rad = math.radians(angle)
    rect = cmath.rect(magnitude, angle_rad)
    return rect

# Função para converter de retangular para polar em graus
def fasor(fas):
    fasorial = [abs(fas), math.degrees(cmath.phase(fas))]
    return fasorial

if st.button('Calcular'):

    # Cálculo das tensões de fase do gerador
    Van = polar_to_rect(Van_modulo, Van_angle)
    Vbn = polar_to_rect(Vbn_modulo, Vbn_angle)
    Vcn = polar_to_rect(Vcn_modulo, Vcn_angle)
    Vfasegerador = np.array([Van, Vbn, Vcn])
    VAN = Van
    VBN = Vbn
    VCN = Vcn

    # Cálculo das correntes de fase e de linha na carga
    I_carga = np.linalg.inv(Z_total).dot(Vfasegerador)
    I_neutro = I_carga[0] + I_carga[1] + I_carga[2]

    # Determinação das Correntes
    IA = I_carga[0]
    IB = I_carga[1]
    IC = I_carga[2]

    # Cálculo das tensões de fase na carga e sobre a rede
    V_carga = np.dot(Z_carga, I_carga)
    V_neutro = I_neutro * ZN
    V_rede = Vfasegerador - V_carga - V_neutro

    # Cálculo das tensões de linha na carga
    VAB_carga = V_carga[0] - V_carga[1]
    VBC_carga = V_carga[1] - V_carga[2]
    VCA_carga = V_carga[2] - V_carga[0]

    # Anotação de Variáveis de Tensão de fase na carga
    VAN_carga = V_carga[0]
    VBN_carga = V_carga[1]
    VCN_carga = V_carga[2]


    # Exiba as variáveis de saída quando os cálculos estiverem prontos

    st.write("Resultados:")

    'Correntes de Fase - IA; IB; IC (A): '

    st.write('------------ MÓDULO    -----------------     ÂNGULO ')
    st.write(f"IA: {fasor(IA)}")
    st.write(f"IB: {fasor(IB)}")
    st.write(f"IC: {fasor(IC)}")
    ''
    if I_neutro > 1e-8:
        'Corrente de Neutro - IN (A): '
        ''
        st.write(f"IN: {fasor(I_neutro)}")
    ''
    "Tensões de Fase na Carga - VA'N; VB'N; VC'N (V): "
    ''
    st.write(f"VA'N: {fasor(VAN_carga)}")
    st.write(f"VB'N: {fasor(VBN_carga)}")
    st.write(f"VC'N {fasor(VCN_carga)}")
    ''
    "Tensões de linha na Carga - VA'B'; VB'C'; VC'A' (V): "
    ''
    st.write(f"VA'B': {fasor(VAB_carga)}")
    st.write(f"VB'C': {fasor(VBC_carga)}")
    st.write(f"VC'A': {fasor(VCA_carga)}")
    ''

    if V_neutro > 1e-8:
        'Tensão de Neutro VNN (V):'
        st.write(f"VNN': {fasor(V_neutro)}")
    
    if V_rede [0]> 1e-8:
        "Tensões sobre a Rede - VAA'; VBB'; VCC' (V): "
        st.write(f"Vbc: {fasor(V_rede[0])}")
        st.write(f"Vbc: {fasor(V_rede[1])}")
        st.write(f"Vbc: {fasor(V_rede[2])}")

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
    plot_tensao(VAB_carga, [0.8, 0.4, 0], 'VAB')
    plot_tensao(VBC_carga, [0.4, 0.8, 0], 'VBC')
    plot_tensao(VCA_carga, [0, 0.6, 0.8], 'VCA')
    plot_tensao(VAN_carga, [0.6, 0.7, 0], 'VAN')
    plot_tensao(VBN_carga, 'm', 'VBN')
    plot_tensao(VCN_carga, 'k', 'VCN')
    if V_neutro > 1e-8:
        plot_tensao(V_neutro,'g','VNN')
    
    # Definindo o título
    ax.set_title('Gráfico das Tensões sobre a Carga')

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

    # Plotando as tensões
    plot_corrente(IA, [0.8, 0.4, 0], 'IA')
    plot_corrente(IB, [0.4, 0.8, 0], 'IB')
    plot_corrente(IC, [0, 0.6, 0.8], 'IC')
    plot_corrente(I_neutro, [0.6, 0.7, 0], 'IN')
    
    # Definindo o título
    ax.set_title('Gráfico das Correntes do Circuito')

    # Remover os rótulos do raio
    ax.set_yticklabels([])

    # Adicionando legenda
    legend = ax.legend(loc='upper right')
    legend.set_bbox_to_anchor((1.3, 1))

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)
