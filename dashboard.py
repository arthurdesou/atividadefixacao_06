from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from scipy import stats

NOME = "Arthur de Souza Câmara"
NUMERO_CHAMADA = "XX"
TURMA = "XX"


st.set_page_config(
    page_title="Dashboard - Atividade 06",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
