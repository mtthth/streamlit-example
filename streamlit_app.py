import streamlit as st
import pandas as pd
import numpy as np

st.title('Météo BW')


def load_temperature():
    temperature = pd.read_csv(r"X:\bw\environnement\2023_06_températures.txt", sep='\t', names=['MJD','T0', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9'])
    #tilt =  pd.read_csv(r"X:\bw\environnement\2023_06_leica_nivel_20.txt", sep='\t', names=['MJD','X', 'Y', 'T', 'void'])
    return temperature

data_load_state = st.text('Loading data...')
temperature = load_temperature()
data_load_state.text('Loading data...done!')
