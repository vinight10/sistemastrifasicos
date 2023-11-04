import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.header('Calculadora de Sistemas Trifásicos :star:')

st.subheader("Sistema Y-Y Equilibrado")
''
image = Image.open('images/y-y-eq.png')
st.image(image, caption='Sistema Trifásico em estrela equilibrado - Fonte: Introdução a sistemas elétricos de potência. 1. ed. São Paulo: Blucher, 2000. E-book. Disponível em: https://plataforma.bvirtual.com.br. Acesso em: 13 out. 2023.')
''
''
# Função para converter módulo e ângulo em formato retangular

def polar_to_rect(magnitude, angle):
    angle_rad = math.radians(angle)
    rect = cmath.rect(magnitude, angle_rad)
    return rect

# Função para converter de retangular para polar em graus

def fasor(fas):
    fasorial = [round(abs(fas), 5), round(math.degrees(cmath.phase(fas)), 5)]
    return fasorial


# Dados de input do usuário
 
    # Pede ao usuário os dados do gerador   

st.markdown('Dados do Gerador:') 
''
''
Vgerador_modulo = st.number_input('Digite o módulo da tensão de fase do gerador conhecida (V): ', value = 220.00)
gerador_angulo = st.number_input('Digite o ângulo da tensão de fase do gerador conhecida (°): ', value = 0.00)
angulo_tipo = st.selectbox("Ângulo pertence a:", ("VAN", "VBN", "VCN"))
seq_fase = st.radio("Sequência de Fase:", ("Direta", "Inversa"))

''
''
    # Pede ao usuário os dados das impedâncias

st.markdown('Dados das impedâncias:')

Z_linha = complex(st.text_input("Digite o valor das impedâncias da rede (ZAA', ZBB', ZCC'), desprezando as mútuas (formato retangular [r+xj], em Ohms \u03A9):", value=0.2+0.5j ))
Z_carga = complex(st.text_input("Digite o valor das impedâncias da carga (ZA'B', ZB'C', ZC'A' em formato retangular [r+xj], em Ohms \u03A9):", value=3+4j ))
Z = Z_carga + Z_linha

if 'VAN' in angulo_tipo and 'Direta' in seq_fase:
    VAN=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VBN=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    VCN=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    van=(Vgerador_modulo,gerador_angulo)
    vbn=(Vgerador_modulo,(gerador_angulo-120))
    vcn=(Vgerador_modulo,(gerador_angulo+120))

elif 'VAN' in angulo_tipo and 'Inversa' in seq_fase:
    VAN=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VBN=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    VCN=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    van=(Vgerador_modulo,gerador_angulo)
    vbn=(Vgerador_modulo,(gerador_angulo+120))
    vcn=(Vgerador_modulo,(gerador_angulo-120))

if 'VBN' in angulo_tipo and 'Direta' in seq_fase:
    VBN=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VCN=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    VAN=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    vbn=(Vgerador_modulo,gerador_angulo)
    vcn=(Vgerador_modulo,(gerador_angulo-120))
    van=(Vgerador_modulo,(gerador_angulo+120))

elif 'VBN' in angulo_tipo and 'Inversa' in seq_fase:
    VBN=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VCN=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    VAN=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    vbn=(Vgerador_modulo,gerador_angulo)
    vcn=(Vgerador_modulo,(gerador_angulo+120))
    van=(Vgerador_modulo,(gerador_angulo-120))

if 'VCN' in angulo_tipo and 'Direta' in seq_fase:
    VCN=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VAN=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    VBN=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    vcn=(Vgerador_modulo,gerador_angulo)
    van=(Vgerador_modulo,(gerador_angulo-120))
    vbn=(Vgerador_modulo,(gerador_angulo+120))

elif 'VCN' in angulo_tipo and 'Inversa' in seq_fase:
    VCN=polar_to_rect(Vgerador_modulo,gerador_angulo)
    VAN=polar_to_rect(Vgerador_modulo,(gerador_angulo+120))
    VBN=polar_to_rect(Vgerador_modulo,(gerador_angulo-120))
    vcn=(Vgerador_modulo,gerador_angulo)
    van=(Vgerador_modulo,(gerador_angulo+120))
    vbn=(Vgerador_modulo,(gerador_angulo-120))

t_raiz_direta = polar_to_rect(math.sqrt(3),30)
t_raiz_inversa = polar_to_rect(math.sqrt(3),-30)


if st.button('Calcular'):

    st.markdown('Resultados: ')
    
    if 'Direta' in seq_fase:    
        IA = (VAN)/(Z)
        IB = (VBN)/(Z)
        IC = (VCN)/(Z)
        VAN_ = (IA*Z_carga)
        VBN_= (IB*Z_carga)
        VCN_ = (IC*Z_carga)
        V_A_B = (VAN*t_raiz_direta)
        V_B_C = (VBN*t_raiz_direta)
        V_C_A = (VCN*t_raiz_direta)
        VAA = VAN - VAN_
        VBB = VBN - VBN_
        VCC = VCN - VCN_
        VAA_ = VAA*t_raiz_direta
        VBB_ = VBB*t_raiz_direta
        VCC_ = VCC*t_raiz_direta

    elif 'Inversa' in seq_fase:
        IA = (VAN)/(Z)
        IB = (VBN)/(Z)
        IC = (VCN)/(Z)
        VAN_ = (IA*Z_carga)
        VBN_= (IB*Z_carga)
        VCN_ = (IC*Z_carga)
        V_A_B = (VAN*t_raiz_inversa)
        V_B_C = (VBN*t_raiz_inversa)
        V_C_A = (VCN*t_raiz_inversa)
        VAA = VAN - VAN_
        VBB = VBN - VBN_
        VCC = VCN - VCN_
        VAA_ = VAA*t_raiz_inversa
        VBB_ = VBB*t_raiz_inversa
        VCC_ = VCC*t_raiz_inversa

    ''
    'Tensões no Gerador: '
    st.write('---- MÓDULO (V) -----------------   ÂNGULO °')
    st.write(f"VAN: {van}")
    st.write(f"VBN: {vbn}")
    st.write(f"VCN: {vcn}")
    ''
    ''
    'Correntes de Fase e Linha: '
    st.write('------------ MÓDULO (A)    -----------------     ÂNGULO °')
    st.write(f"IA': {fasor(IA)}")
    st.write(f"IB': {fasor(IB)}")
    st.write(f"IC': {fasor(IC)}")  
    ''
    ''
    'Tensões de fase na carga: '
    st.write('------------ MÓDULO (A)   -----------------     ÂNGULO °')
    st.write(f"IA'B': {fasor(VAN_)}")
    st.write(f"IB'C': {fasor(VBN_)}")
    st.write(f"IC'A': {fasor(VCN_)}")
    ''
    ''
    'Tensões de linha na carga: '
    st.write('------------ MÓDULO (V)   -----------------     ÂNGULO °')
    st.write(f"VA'B': {fasor(V_A_B)}")
    st.write(f"VB'C': {fasor(V_B_C)}")
    st.write(f"VC'A': {fasor(V_C_A)}")
    ''
    ''
    'Quedas de tensão na rede: '
    ''
    'Tensão de fase: '
    st.write('------------ MÓDULO (V)   -----------------     ÂNGULO °')
    st.write(f"VAA': {fasor(VAA)}")
    st.write(f"VBB': {fasor(VBB)}")
    st.write(f"VCC': {fasor(VCC)}")
    ''
    'Tensões de linha: '
    st.write('------------ MÓDULO (V)   -----------------     ÂNGULO °')
    st.write(f"VAB - VA'B': {fasor(VAA_)}")
    st.write(f"VBC - VB'C': {fasor(VBB_)}")
    st.write(f"VCA - VC'A': {fasor(VCC_)}")


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
    plot_tensao(VAN_, [0.8, 0.4, 0], "VA'N'")
    plot_tensao(VBN_, [0.4, 0.8, 0], "VB'N'")
    plot_tensao(VCN_, [0, 0.6, 0.8], "VC'N'")
    plot_tensao(V_A_B, [0.6, 0.7, 0], "V A'B'")
    plot_tensao(V_B_C, 'm', "V B'C'")
    plot_tensao(V_C_A, 'k', "V C'A'")
    


    # Definindo o título
    ax.set_title('Gráfico dos fasores de tensão na carga: ')

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
    plot_corrente(IA, [0.8, 0.4, 0], 'IAA')
    plot_corrente(IB, 'm', "I B'C'")
    plot_corrente(IC, 'k', "I C'A'")
    
    
    # Definindo o título
    ax.set_title('Gráfico das Correntes do Circuito')

    # Remover os rótulos do raio
    ax.set_yticklabels([])

    # Adicionando legenda
    legend = ax.legend(loc='upper right')
    legend.set_bbox_to_anchor((1.3, 1))

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)
