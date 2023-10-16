import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title='Sistemas Trifásicos',
    page_icon='🏠',
    layout='wide'
)

st.title('Calculadora de Sistemas Trifásicos')
''
st.subheader('Faça cálculos de sistemas trifásicos de forma fácil e interativa')
''
''
'Este site tem como intuito auxiliar os estudantes de engenharia elétrica nas disciplinas de circuitos elétricos, a fim de facilitar o processo de aprendizagem trazendo os gráficos de fasores de tensão e de corrente sem complicações.'
''
'Projeto desenvolvido como trabalho de conclusão de curso de engenharia na Uniftec - Caxias do Sul'
''
'Desenvolvido por: Vinicius Martins Fioreze - Email: vinicius.fioreze@acad.ftec.com.br'
'Professor orientador: Esp. Jocemar Muller Boeira '