# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:53:35 2022

@author: funes
"""

from matplotlib import pyplot as plt
# %matplotlib qt
import numpy as np
#%%
"Frecuencias inferiores y superiores de c/banda de octava"

b_oct = np.array ([60,125,250,500,1000,2000,4000,8000,16000])
f_inf = b_oct / np.sqrt (2)
f_sup = b_oct * np.sqrt (2)
#%%
# =============================================================================
    "A continuación hago los promedios de los 3 micrófonos"
# =============================================================================
#%%
"Hago los promedios para NT2000 Figura 8; ---> Directorio debe estar en TP1\Mediciones\txt\NT2000\Figura 8"
#%%
dif_grados = 10
patron_polar = 8
NT2000_Fig8_txt_list = []
for i in range (19):
    txt = np.loadtxt (str("NT2000-"+str(i*dif_grados)+"-"+str(patron_polar)+".txt"),skiprows=2)
    NT2000_Fig8_txt_list.append (txt)

matrix_NT2000_Fig8 = b_oct.reshape (9,1)    
for angulo, txt in enumerate (NT2000_Fig8_txt_list): #Recorro cada txt (va a haber 19)
    angulo = angulo*10
    for i, banda in enumerate (b_oct): #Recorro las bandas de octava desde 60 hasta 16k
        suma_banda_i = [] #Reinicio esta lista cada vez que entro en una nueva banda de octava
        for freq_index, freq in enumerate (txt[:,0]): #Recorro las frecuencias de cada txt
            if f_inf[i] <= freq <= f_sup[i]: #Veo que esa frecuencia esta en cierta banda de octava
                if txt[freq_index,1] < 500: #Hay algunos valores del txt que tiran como 1000 dB (y claramente es un error), por lo cual hago que no compute esos valores.
                    suma_banda_i.append(10**(txt[freq_index,1]/10)) #Hago una lista que va teniendo la amplitud de dicha frecuencia
            elif freq > f_sup [i]: #Sería como decir "Si la frecuencia que estoy viendo en el txt ya esta fuera de la banda de octava que estoy considerando:
                promedio_banda_i = 10*np.log10 (np.sum(np.array (suma_banda_i)/len(suma_banda_i))) #Calculo el promedio energético de la banda que acaba de terminar
                if i == 0: #Si es la primera banda de octava (la de 60 Hz), inicio la matriz
                    promedio_bandas = promedio_banda_i # promedio_bandas va a ser un vector que tenga los promedios por banda de octava de cada txt
                else: #Si no es la primer banda de octava, completo de forma vertical (filas) el array que ya esta empezado
                    promedio_bandas = np.vstack([promedio_bandas, promedio_banda_i]) 
                break 
    matrix_NT2000_Fig8 = np.hstack ([matrix_NT2000_Fig8, promedio_bandas])
#%%
"Hago los promedios para NT2000 Cardioide; ---> Directorio debe estar en TP1\Mediciones\txt\NT2000\Cardioide"
#%%
dif_grados = 10
patron_polar = "C"
NT2000_Cardioid_txt_list = []
for i in range (19):
    txt = np.loadtxt (str("NT2000-"+str(i*dif_grados)+"-"+str(patron_polar)+".txt"),skiprows=2)
    NT2000_Cardioid_txt_list.append (txt)

matrix_NT2000_Cardioid = b_oct.reshape (9,1)    
for angulo, txt in enumerate (NT2000_Cardioid_txt_list): #Recorro cada txt (va a haber 19)
    angulo = angulo*10
    for i, banda in enumerate (b_oct): #Recorro las bandas de octava desde 60 hasta 16k
        suma_banda_i = [] #Reinicio esta lista cada vez que entro en una nueva banda de octava
        for freq_index, freq in enumerate (txt[:,0]): #Recorro las frecuencias de cada txt
            if f_inf[i] <= freq <= f_sup[i]: #Veo que esa frecuencia esta en cierta banda de octava
                if txt[freq_index,1] < 500: #Hay algunos valores del txt que tiran como 1000 dB (y claramente es un error), por lo cual hago que no compute esos valores.
                    suma_banda_i.append(10**(txt[freq_index,1]/10)) #Hago una lista que va teniendo la amplitud de dicha frecuencia
            elif freq > f_sup [i]: #Sería como decir "Si la frecuencia que estoy viendo en el txt ya esta fuera de la banda de octava que estoy considerando:
                promedio_banda_i = 10*np.log10 (np.sum(np.array (suma_banda_i)/len(suma_banda_i))) #Calculo el promedio energético de la banda que acaba de terminar
                if i == 0: #Si es la primera banda de octava (la de 60 Hz), inicio la matriz
                    promedio_bandas = promedio_banda_i # promedio_bandas va a ser un vector que tenga los promedios por banda de octava de cada txt
                else: #Si no es la primer banda de octava, completo de forma vertical (filas) el array que ya esta empezado
                    promedio_bandas = np.vstack([promedio_bandas, promedio_banda_i]) 
                break 
    matrix_NT2000_Cardioid = np.hstack ([matrix_NT2000_Cardioid, promedio_bandas])
#%%
"Hago los promedios para Shure SM57 Cardioide; ---> Directorio debe estar en TP1\Mediciones\txt\SM57"
#%%
dif_grados = 5
SM57_txt_list = []
for i in range (37):
    txt = np.loadtxt (str("SM57-"+str(i*dif_grados)+".txt"),skiprows=2)
    SM57_txt_list.append (txt)

matrix_SM57 = b_oct.reshape (9,1)    
for angulo, txt in enumerate (SM57_txt_list): #Recorro cada txt (va a haber 19)
    angulo = angulo*5 #Esto pensé que lo iba a usar pero al final no era necesario.
    for i, banda in enumerate (b_oct): #Recorro las bandas de octava desde 60 hasta 16k
        suma_banda_i = [] #Reinicio esta lista cada vez que entro en una nueva banda de octava
        for freq_index, freq in enumerate (txt[:,0]): #Recorro las frecuencias de cada txt
            if f_inf[i] <= freq <= f_sup[i]: #Veo que esa frecuencia esta en cierta banda de octava
                if txt[freq_index,1] < 500: #Hay algunos valores del txt que tiran como 1000 dB (y claramente es un error), por lo cual hago que no compute esos valores.
                    suma_banda_i.append(10**(txt[freq_index,1]/10)) #Hago una lista que va teniendo la amplitud de dicha frecuencia
            elif freq > f_sup [i]: #Sería como decir "Si la frecuencia que estoy viendo en el txt ya esta fuera de la banda de octava que estoy considerando:
                promedio_banda_i = 10*np.log10 (np.sum(np.array (suma_banda_i)/len(suma_banda_i))) #Calculo el promedio energético de la banda que acaba de terminar
                if i == 0: #Si es la primera banda de octava (la de 60 Hz), inicio la matriz
                    promedio_bandas = promedio_banda_i # promedio_bandas va a ser un vector que tenga los promedios por banda de octava de cada txt
                else: #Si no es la primer banda de octava, completo de forma vertical (filas) el array que ya esta empezado
                    promedio_bandas = np.vstack([promedio_bandas, promedio_banda_i]) 
                break 
    matrix_SM57 = np.hstack ([matrix_SM57, promedio_bandas])
#%%
# =============================================================================
    "A continuación genero los gráficos de patrón polar para los 3 micrófonos"
# =============================================================================
#%%
"Genero los gráficos de patrón polar para NT2000 Figura 8"
rad = np.pi/180 #Factor de corrección de grados a radianes
degree_NT2000_posit = np.arange (0,rad*190,rad*10)
degree_NT2000_negat = np.arange (0,-rad*190,-rad*10)
plt.figure()
for row in range (9):
    amplitudes = matrix_NT2000_Fig8 [row,1:] #Las amplitudes a plotear
    amplitudes -= amplitudes [0] #Hago coincidir la incidencia a 0º con 0 dB
    # if row == 0:
        # plt.polar (degree_NT2000_posit, amplitudes, color="green", linestyle="solid", label= str(matrix_NT2000_Fig8[row,0])+"Hz",linewidth=5)
    if row == 1:
        plt.polar (degree_NT2000_negat, amplitudes, color="green", linestyle=(0,(3,1,1,1)), label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    if row == 2:
        plt.polar (degree_NT2000_posit, amplitudes, color="black", linestyle="dotted", label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    if row == 3:
        plt.polar (degree_NT2000_negat, amplitudes, color="black", linestyle=(0,(5,10)), label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    if row == 4:
        plt.polar (degree_NT2000_posit, amplitudes, color="orange", linestyle="dashed", label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    if row == 5:
        plt.polar (degree_NT2000_negat, amplitudes, color="orange", linestyle=(0,(3,10,1,10)), label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    if row == 6:
        plt.polar (degree_NT2000_posit, amplitudes, color="red", linestyle="dashdot", label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)        
    if row == 7:
        plt.polar (degree_NT2000_negat, amplitudes, color="red", linestyle=(0,(3,5,1,5,1,5)), label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    if row == 8:
        plt.polar (degree_NT2000_posit, amplitudes, color="blue", linestyle=(5,(10,3)), label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)
    plt.title ("Patrón polar para RODE NT2000 bidireccional",fontsize=38, pad=10)
    plt.grid (linewidth=3)
    plt.xticks (fontsize=34)
    plt.yticks ([0,-3,-6,-9,-12,-15,-18],["0dB","-3dB","-6dB","-9dB","-12dB","-15dB","-18dB"], ha="center", va="center", x= 35*rad, fontsize=34)
    plt.legend (bbox_to_anchor=(1.1, 0.75),fontsize=28)
#%%
"Genero los gráficos de patrón polar para NT2000 Cardioide"
rad = np.pi/180 #Factor de corrección de grados a radianes
degree_NT2000_posit = np.arange (0,rad*190,rad*10)
degree_NT2000_negat = np.arange (0,-rad*190,-rad*10)
plt.figure ()
for row in range (9):
    amplitudes = matrix_NT2000_Cardioid [row,1:] #Las amplitudes a plotear
    amplitudes -= amplitudes [0] #Hago coincidir la incidencia a 0º con 0 dB
    # if row == 0:
        # plt.polar (degree_NT2000_posit, amplitudes, color="green", linestyle="solid", label= str(matrix_NT2000_Cardioid[row,0])+" Hz",linewidth=5)        
    if row == 1:
        plt.polar (degree_NT2000_negat, amplitudes, color="green", linestyle=(0,(3,1,1,1)), label= str(int(matrix_NT2000_Fig8[row,0]))+" Hz",linewidth=5)        
    if row == 2:
        plt.polar (degree_NT2000_posit, amplitudes, color="black", linestyle="dotted", label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)        
    if row == 3:
        plt.polar (degree_NT2000_negat, amplitudes, color="black", linestyle=(0,(5,10)), label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)        
    if row == 4:
        plt.polar (degree_NT2000_posit, amplitudes, color="orange", linestyle="dashed", label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)        
    if row == 5:
        plt.polar (degree_NT2000_negat, amplitudes, color="orange", linestyle=(0,(3,10,1,10)), label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)        
    if row == 6:
        plt.polar (degree_NT2000_posit, amplitudes, color="red", linestyle="dashdot", label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)
    if row == 7:
        plt.polar (degree_NT2000_negat, amplitudes, color="red", linestyle=(0,(3,5,1,5,1,5)), label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)        
    if row == 8:
        plt.polar (degree_NT2000_posit, amplitudes, color="blue", linestyle=(5,(10,3)), label= str(int(matrix_NT2000_Cardioid[row,0]))+" Hz",linewidth=5)
    plt.title ("Patrón polar para RODE NT2000 cardioide",fontsize=38, pad=10)
    plt.grid (linewidth=3)
    plt.xticks (fontsize=34)
    plt.yticks ([0,-3,-6,-9,-12,-15],["0dB","-3dB","-6dB","-9dB","-12dB","-15dB"], ha="center", va="center", x= -55*rad, fontsize=34)
    plt.legend (bbox_to_anchor=(1.1, 0.75),fontsize=28)
#%%
"Genero los gráficos de patrón polar para Shure SM57 Cardioide"
rad = np.pi/180 #Factor de corrección de grados a radianes
degree_SM57_posit =  np.arange (0,rad*185,rad*5)
degree_SM57_negat =  np.arange (0,-rad*185,-rad*5)
plt.figure ()
for row in range (9):
    amplitudes = matrix_SM57 [row,1:] #Las amplitudes a plotear
    amplitudes -= amplitudes [0] #Hago coincidir la incidencia a 0º con 0 dB
    # if row == 0:
        # plt.polar (degree_SM57_posit, amplitudes, color="green", linestyle="solid", label= str(matrix_SM57[row,0])+" Hz",linewidth=5)        
    if row == 1:
        plt.polar (degree_SM57_negat, amplitudes, color="green", linestyle=(0,(3,1,1,1)), label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 2:
        plt.polar (degree_SM57_posit, amplitudes, color="black", linestyle="dotted", label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 3:
        plt.polar (degree_SM57_negat, amplitudes, color="black", linestyle=(0,(5,10)), label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 4:
        plt.polar (degree_SM57_posit, amplitudes, color="orange", linestyle="dashed", label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 5:
        plt.polar (degree_SM57_negat, amplitudes, color="orange", linestyle=(0,(3,10,1,10)), label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 6:
        plt.polar (degree_SM57_posit, amplitudes, color="red", linestyle="dashdot", label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 7:
        plt.polar (degree_SM57_negat, amplitudes, color="red", linestyle=(0,(3,5,1,5,1,5)), label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)        
    if row == 8:
        plt.polar (degree_SM57_posit, amplitudes, color="blue", linestyle=(5,(10,3)), label= str(int(matrix_SM57[row,0]))+" Hz",linewidth=5)
    plt.title ("Patrón polar para Shure SM57 cardioide",fontsize=38, pad=10)
    plt.grid (linewidth=3)
    plt.xticks (fontsize=34)
    plt.yticks ([0,-3,-6,-9,-12,-15],["0dB","-3dB","-6dB","-9dB","-12dB","-15dB"], ha="center", va="center", x= -55*rad, fontsize=34)
    plt.legend (bbox_to_anchor=(1.1, 0.75),fontsize=28)  






