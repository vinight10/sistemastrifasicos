import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image



st.header('Calculadora de Sistemas Trifásicos')
st.subheader('Ligação Y-Y com carga **desequilibrada**')
''
''
image = Image.open('images/y-y-des.png')
st.image(image, caption='Sistema Trifásico Desequilibrado - Fonte: Introdução a sistemas elétricos de potência. 1. ed. São Paulo: Blucher, 2000. E-book. Disponível em: https://plataforma.bvirtual.com.br. Acesso em: 13 out. 2023.')
''
st.markdown("Os sistemas trifásicos simétricos e equilibrados com carga desequilibrada são formados por geradores com mesma amplitude e defasagem de 120º, com linhas não possuindo impedâncias mútuas ou com mútuas iguais entre si e que alimentam cargas desequilibradas, onde as impedâncias que compõem a carga têm valores distintos (OLIVEIRA, et al. 2000). Neste modelo, as mútuas são desprezadas e a impedância da rede é igual.")
''
''
st.markdown("Dados do Gerador (caso só possua um ângulo utilize a aba **fasores** para encontrar os demais):")
''
''
Van_modulo = st.number_input('Digite o módulo da tensão de fase(V): ', value = 220.00)
Van_angle = st.number_input('Digite o ângulo da tensão de fase Van (graus): ', value = 0.00)
Vbn_angle = st.number_input('Digite o ângulo da tensão de fase Vbn (graus): ', value = -120.00)
Vcn_angle = st.number_input('Digite o ângulo da tensão de fase Vcn (graus): ', value = 120.00)
Vbn_modulo = Van_modulo
Vcn_modulo = Van_modulo
''
''
'Dados da Matriz de impedâncias da Rede:'
''
''
# IMPEDÂNCIAS PRÓPRIAS
      
Zaa = complex(st.text_input('Digite o valor das impedâncias próprias (formato retangular [r+xj], em Ohms \u03A9):', value=0.5+2.0j ))

Zp = Zaa

""
""
'Dados de Impedância de Carga e de Neutro:'

ZA = complex(st.text_input('Digite a impedância da carga ZA (formato retangular, em Ohms \u03A9): ', value=20+0j))
ZB = complex(st.text_input('Digite a impedância da carga ZB (formato retangular, em Ohms \u03A9): ', value=0+10j))
ZC = complex(st.text_input('Digite a impedância da carga ZC (formato retangular, em Ohms \u03A9): ', value=0-10j))
ZN = complex(st.text_input('Digite a impedância de neutro ZN (formato retangular, em Ohms \u03A9): ', value=0.5+2.0j))


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
    
    # Determinação da Corrente de Neutro

    I_neutro = (((Van/(ZA+Zp))+(Vbn/(ZB+Zp))+(Vcn/(ZC+Zp)))/(1+((ZN/(ZA+Zp))+(ZN/(ZB+Zp))+(ZN/(ZC+Zp)))))

    # Determinação das tensão de Neutro VN'N
    V_neutro = I_neutro * ZN

    # Cálculo das tensões no circuito

    VAN_ = Van - V_neutro
    VBN_ = Vbn - V_neutro
    VCN_ = Vcn - V_neutro
    
    # Cálculo das correntes de Linha

    IA = VAN_/(ZA+Zp)
    IB = VBN_/(ZB+Zp)
    IC = VCN_/(ZC+Zp)

    # Cálculo das tensões de fase na carga

    VAN_carga= IA*ZA
    VBN_carga = IB*ZB
    VCN_carga = IC*ZC

    # Cálculo das tensões de linha na carga

    VAB_carga = VAN_carga - VBN_carga
    VBC_carga = VBN_carga - VCN_carga
    VCA_carga = VCN_carga - VAN_carga

    # Cálculo das tensões sobre a rede

    VAA = Van - VAN_carga
    VBB = Vbn - VBN_carga
    VCC = Vcn - VCN_carga

    # Exiba as variáveis de saída quando os cálculos estiverem prontos

    st.write("Resultados:")
    ''
    'Corrente de Neutro - IN (A): '
    ''
    st.write(f"IN: {fasor(I_neutro)}")
    ''
    'Tensão de Neutro VNN (V):'
    ''
    st.write(f"VNN': {fasor(V_neutro)}")
    ''
    ''
    'Correntes de Fase - IA; IB; IC (A): '
    st.write('------------ MÓDULO (A)    -----------------     ÂNGULO °')
    st.write(f"IA: {fasor(IA)}")
    st.write(f"IB: {fasor(IB)}")
    st.write(f"IC: {fasor(IC)}")
    ''
    ''
    "Tensões de Fase na Carga - VA'N; VB'N; VC'N (V): "
    ''
    st.write('------------ MÓDULO (V)  -----------------     ÂNGULO ° ')
    st.write(f"VA'N: {fasor(VAN_carga)}")
    st.write(f"VB'N: {fasor(VBN_carga)}")
    st.write(f"VC'N {fasor(VCN_carga)}")
    ''
    "Tensões de linha na Carga - VA'B'; VB'C'; VC'A' (V): "
    ''
    st.write('------------ MÓDULO (V)   -----------------     ÂNGULO °')
    st.write(f"VA'B': {fasor(VAB_carga)}")
    st.write(f"VB'C': {fasor(VBC_carga)}")
    st.write(f"VC'A': {fasor(VCA_carga)}")
    ''
    ''    
    
    "Tensões sobre a Rede - VAA'; VBB'; VCC' (V): "
    st.write('------------ MÓDULO (V)   -----------------     ÂNGULO °')
    st.write(f"VAA: {fasor(VAA)}")
    st.write(f"VBB: {fasor(VBB)}")
    st.write(f"VCC: {fasor(VCC)}")

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

    # Plotando as correntes
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