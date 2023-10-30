import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Título do aplicativo
st.header('Calculadora de Sistemas Trifásicos')
st.subheader("Conversor de Coordenadas")
''
image = Image.open('images/coord.png')
st.image(image, caption='Coordenadas no plano cartesiano - Fonte: Brasil Escola. Disponível em: https://brasilescola.uol.com.br/. Acesso em: 13 out. 2023.')
''
st.markdown("Conhecido como plano complexo ou plano de Argand-Gauss, ele permite a representação na forma geométrica de um número complexo, esse plano é uma adaptação no plano cartesiano para representar números complexos. O eixo horizontal é conhecido como eixo da parte real Re(z), e o eixo vertical é conhecido como eixo da parte imaginária Im(z). Então o número complexo representado por a + bi gera os pontos no plano complexo formado pelo par ordenado (a, b).")

"Lembre-se: As informações devem ser dadas em graus, não radianos."
# Opção para selecionar o tipo de coordenada
''
opcao = st.radio("Selecione o tipo de coordenada:", ("Polar para Retangular", "Retangular para Polar"))

# Inicializa variáveis para armazenar as coordenadas
x, y, modulo, angulo = 0, 0, 0, 0

if opcao == "Polar para Retangular":
    # Entrada para coordenadas polares
    modulo = st.number_input("Módulo (Z):")
    angulo = st.number_input("Ângulo \u03b8 (graus):")

else:
    # Entrada para coordenadas retangulares
    x = st.number_input("Parte Real (a):")
    y = st.number_input("Parte Imaginária (b):")

# Botão para converter e plotar o gráfico
if st.button("Converter"):
    if opcao == "Polar para Retangular":
        # Converter coordenadas polares para retangulares
        x = modulo * np.cos(np.radians(angulo))
        y = modulo * np.sin(np.radians(angulo))
    else:
        # Converter coordenadas retangulares para polares
        modulo = np.sqrt(x ** 2 + y ** 2)
        angulo = np.degrees(np.arctan2(y, x))

    # Exibir coordenadas retangulares
    st.write(f"Coordenadas Retangulares (a, b) : ({x}, {y})")
    st.write(f"Coordenadas Polares (Módulo, Ângulo \u03b8 °) : {modulo}, {angulo}")

    # Plotar gráfico semelhante ao modelo do site
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Parte retangular
    ax.plot([0, x], [0, y], label="Retangular", color='blue', marker='o')
    
    # Parte polar
    ax.plot([0, x], [0, y], linestyle='--', color='gray')
    ax.plot(x, y, 'ro', label="Polar")
    
    ax.annotate(f"{x:.2f} + {y:.2f}j", (x, y), textcoords="offset points", xytext=(10,10), ha='center')
    ax.annotate(f"Módulo: {modulo:.2f}", (x, y), textcoords="offset points", xytext=(10,-20), ha='center')
    ax.annotate(f"Fase (\u03b8): {angulo:.2f}°", (x, y), textcoords="offset points", xytext=(10,-40), ha='center')
    
    ax.set_xlim(min(0, x) - 1, max(0, x) + 1)
    ax.set_ylim(min(0, y) - 1, max(0, y) + 1)
    ax.set_xlabel("Parte Real (eixo X)")
    ax.set_ylabel("Parte Imaginária (eixo Y)")
    ax.grid(True)
    
    st.pyplot(fig)