# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:41:05 2022

@author: funes
"""
from suavizado import suavizado #---> El directorio tiene que estar en ELECTROACUSTICA 1\TP 1\Python
from matplotlib import pyplot as plt
# %matplotlib qt
import numpy as np
#%%

"Arranco por el NT2000 Figura 8"

#%%
# =============================================================================
    "A continuación importo los txt solicitados"
# =============================================================================
#%%
"NT2000 Figura 8--> se pide rta en frecuencia a 0º, 45º, 90º, 135º y 180º"
patron_polar = 8
NT2000_Fig8_freq_list = []
for angulo in [0,50,90,140,180]: #Uso 50º y 140º porque no se midió a 45º y 135º y es practicamente lo mismo
    txt = np.loadtxt (str("NT2000-"+str(angulo)+"-"+str(patron_polar)+".txt"),skiprows=2)
    NT2000_Fig8_freq_list.append (txt)

NT2000_Fig8_rta_freq_list = []    #En esta lista voy a tener las respuestas en frecuencia ya con coherencia de 60%
for txt_index, txt in enumerate (NT2000_Fig8_freq_list): #Me quedo con las frecuencias que tengan coherencia de al menos 60%
    rta_freq = np.empty ((1,2)) #Inicio un vector asi despus puedo usar vstack. Cuando termine el for tengo que eliminar la primera fila porq esta vacía
    for row in txt:
        # if 999<=row [0]<=1001 and txt_index==0: #Si estoy en el primer txt (el de 0º) y estoy en la frecuencia de 1k
            # NT2000_Fig8_1k = row [1] #Almaceno el valor que tiene la curva en 1k Hz (despues la rta en frecuencia tiene que valer cero en este punto)
        if row[-1]>=0.6 and row [1]<500: #Si la coherencia es por lo menos de 60% y la amplitud en dB no es una reverenda pelotudez (hay valores que daban 1200 dB)
            rta_freq = np.vstack([rta_freq, row [:2]])
    rta_freq = rta_freq [1:,:] #Acá elimino ese np.empty que habia puesto antes.
    # rta_freq [:,1] -= NT2000_Fig8_1k #A c/ rta en frecuencia le resto el valor que tiene la curva a incidencia 0º para 1k Hz 
    NT2000_Fig8_rta_freq_list.append (rta_freq)
#%%
# =============================================================================
    "A continuación hago el suavizado de los datos y grafico la rta en Frecuencia"
# =============================================================================
#%%
"NT2000 Figura 8 ---> Le hago suavizado en 1/3 de Octava"
NT2000_Fig8_rta_freq_smoothed_list = [] #Una lista que va a tener las amplitudes ya suavizadas y con 1kHz valiendo 0dB
for index, rta_freq in enumerate(NT2000_Fig8_rta_freq_list):
    rta_smoothed = suavizado(rta_freq[:,0], rta_freq [:,1], 3) #Suavizo cada rta en frecuencia con el code que hizo Pedro
    if index == 0: #Si estoy viendo incidencia a 0º
        index_1k = np.where (999<rta_freq [:,0])[0][0] #index para el cual la frecuencia es 1kHz
        magnitud_1k = rta_smoothed [index_1k] #Obtengo el valor que la curva (ya suavizada) tiene en 1kHz
    rta_smoothed -= magnitud_1k #A la curva suavizada le resto ese valor.
    NT2000_Fig8_rta_freq_smoothed_list.append (rta_smoothed) 
#%%
#Defino un par de boludeces para despues graficar
incidencia = ["Incidencia a 0º","Incidencia a 45º","Incidencia a 90º","Incidencia a 135º","Incidencia a 180º"]
linestyle = ["dotted","dashed","dashdot",(0,(3,1,1,1)),"solid"]
color = ["black","orange","magenta","red","green"]
freqs_interes = [30,60,100,125,250,500,1000,2000,4000,8000,10000,16000,20000]
freqs_interes_labels = ["30Hz","60Hz","100Hz","125Hz","250Hz","500Hz","1kHz","2kHz","4kHz","8kHz","10kHz","16kHz","20kHz"]
dB_interes = [12,9,6,3,0,-3,-6,-9,-12,-15,-18,-21,-24,-30]
dB_interes_labels = ["12dB","9dB","6dB","3dB","0dB","-3dB","-6dB","-9dB","-12dB","-15dB","-18dB","-21dB","-24dB","-30dB"]

"NT2000 Figura 8 ---> Grafico la rta en frecuencia"

plt.figure()
for index, rta_freq_smoothed in enumerate(NT2000_Fig8_rta_freq_smoothed_list):
    plt.plot (NT2000_Fig8_rta_freq_list [index][:,0], rta_freq_smoothed, label=incidencia[index], linestyle=linestyle[index], color=color[index])
plt.xscale("log", basex=10)
plt.rcParams ["font.size"] = 14
plt.title ("Respuesta en frecuencia según ángulo de incidencia para Rode NT2000 con patrón polar bidireccional",fontsize=20)
plt.xlabel ("Frecuencia",fontsize=18)
plt.ylabel ("Magnitud",fontsize=18)
plt.legend (fontsize=16)
plt.xticks (freqs_interes,freqs_interes_labels)
plt.yticks  (dB_interes,dB_interes_labels)
plt.xlim (95,10500) #Habia arrancado en 58 antes de que estandaricemos todo en 95
plt.ylim (-20,12)
plt.grid (True, which="both")    
#%%

"Sigo con el NT2000 Cardioide"

#%%
# =============================================================================
    "A continuación importo los txt solicitados"
# =============================================================================
#%%
#%%
"NT2000 Cardioide--> se pide rta en frecuencia a 0º, 65º, 90º y 180º"
patron_polar = "C"
NT2000_Cardioid_freq_list = []
for angulo in [0,70,90,180]: #Uso 70º porque no se midió a 65º y es practicamente lo mismo
    txt = np.loadtxt (str("NT2000-"+str(angulo)+"-"+str(patron_polar)+".txt"),skiprows=2)
    NT2000_Cardioid_freq_list.append (txt)
    
NT2000_Cardioid_rta_freq_list = []    #En esta lista voy a tener las respuestas en frecuencia ya con coherencia de 60%
for txt_index, txt in enumerate (NT2000_Cardioid_freq_list): #Me quedo con las frecuencias que tengan coherencia de al menos 60%
    rta_freq = np.empty ((1,2)) #Inicio un vector asi despus puedo usar vstack. Cuando termine el for tengo que eliminar la primera fila porq esta vacía
    for row in txt:
        # if 999<=row [0]<=1001 and txt_index==0: #Si estoy en el primer txt (el de 0º) y estoy en la frecuencia de 1k
            # NT2000_Cardioid_1k = row [1] #Almaceno el valor que tiene la curva en 1k Hz (despues la rta en frecuencia tiene que valer cero en este punto)
        if row[-1]>=0.6 and row [1]<500: #Si la coherencia es por lo menos de 60% y la amplitud en dB no es una reverenda pelotudez (hay valores que daban 1200 dB)
            rta_freq = np.vstack([rta_freq, row [:2]])
    rta_freq = rta_freq [1:,:] #Acá elimino ese np.empty que habia puesto antes.
    # rta_freq [:,1] -= NT2000_Fig8_1k #A c/ rta en frecuencia le resto el valor que tiene la curva a incidencia 0º para 1k Hz
    NT2000_Cardioid_rta_freq_list.append (rta_freq)
#%%
# =============================================================================
    "A continuación hago el suavizado de los datos y grafico la rta en Frecuencia"
# =============================================================================
#%%
"NT2000 Cardioide ---> Le hago suavizado en 1/3 de Octava"
NT2000_Cardioid_rta_freq_smoothed_list = [] #Una lista que va a tener las amplitudes ya suavizadas y con 1kHz valiendo 0dB
for index, rta_freq in enumerate(NT2000_Cardioid_rta_freq_list):
    rta_smoothed = suavizado(rta_freq[:,0], rta_freq [:,1], 3) #Suavizo cada rta en frecuencia con el code que hizo Pedro
    if index == 0: #Si estoy viendo incidencia a 0º
        index_1k = np.where (999<rta_freq [:,0])[0][0] #index para el cual la frecuencia es 1kHz
        magnitud_1k = rta_smoothed [index_1k] #Obtengo el valor que la curva (ya suavizada) tiene en 1kHz
    rta_smoothed -= magnitud_1k #A la curva suavizada le resto ese valor.
    NT2000_Cardioid_rta_freq_smoothed_list.append (rta_smoothed) 
#%%
#Defino un par de boludeces para despues graficar
incidencia = ["Incidencia a 0º","Incidencia a 65º","Incidencia a 90º","Incidencia a 180º"]
linestyle = ["dotted","dashed","dashdot","solid"]
color = ["black","orange","red","green"]
freqs_interes = [30,60,100,125,250,500,1000,2000,4000,8000,10000,16000,20000]
freqs_interes_labels = ["30Hz","60Hz","100Hz","125Hz","250Hz","500Hz","1kHz","2kHz","4kHz","8kHz","10kHz","16kHz","20kHz"]
dB_interes = [12,9,6,3,0,-3,-6,-9,-12,-15,-18,-21,-24,-30]
dB_interes_labels = ["12dB","9dB","6dB","3dB","0dB","-3dB","-6dB","-9dB","-12dB","-15dB","-18dB","-21dB","-24dB","-30dB"]

"NT2000 Cardioide ---> Grafico la rta en frecuencia"

plt.figure()
for index, rta_freq_smoothed in enumerate(NT2000_Cardioid_rta_freq_smoothed_list):
    plt.plot (NT2000_Cardioid_rta_freq_list [index][:,0], rta_freq_smoothed, label=incidencia[index], linestyle=linestyle[index], color=color[index])
plt.xscale("log", basex=10)
plt.rcParams ["font.size"] = 14
plt.title ("Respuesta en frecuencia según ángulo de incidencia para Rode NT2000 con patrón polar cardioide",fontsize=20)
plt.xlabel ("Frecuencia",fontsize=18)
plt.ylabel ("Magnitud",fontsize=18)
plt.legend (fontsize=16)
plt.xticks (freqs_interes,freqs_interes_labels)
plt.yticks  (dB_interes,dB_interes_labels)
plt.xlim (95,20000) #Habia arrancado en 30 antes de estandarizar a 95
plt.ylim (-20,6)
plt.grid (True, which="both")
#%%

"Sigo con el Shure SM57"

#%%
# =============================================================================
    "A continuación importo los txt solicitados"
# =============================================================================
#%%
"SM57--> se pide rta en frecuencia a 0º, 65º, 90º y 180º"
SM57_freq_list = []
for angulo in [0,65,90,180]:
    txt = np.loadtxt (str("SM57-"+str(angulo)+".txt"),skiprows=2)
    SM57_freq_list.append (txt)
    
SM57_rta_freq_list = []    #En esta lista voy a tener las respuestas en frecuencia ya con coherencia de 60%
for txt in (SM57_freq_list): #Me quedo con las frecuencias que tengan coherencia de al menos 60%
    rta_freq = np.empty ((1,2)) #Inicio un vector asi despus puedo usar vstack. Cuando termine el for tengo que eliminar la primera fila porq esta vacía
    for row in txt:        
        # if 999<=row [0]<=1001 and txt_index==0: #Si estoy en el primer txt (el de 0º) y estoy en la frecuencia de 1k
            # SM57_1k = row [1] #Almaceno el valor que tiene la curva en 1k Hz (despues la rta en frecuencia tiene que valer cero en este punto)
        if row[-1]>=0.6 and row [1]<500: #Si la coherencia es por lo menos de 60% y la amplitud en dB no es una reverenda pelotudez (hay valores que daban 1200 dB)
            rta_freq = np.vstack([rta_freq, row [:2]])
    rta_freq = rta_freq [1:,:] #Acá elimino ese np.empty que habia puesto antes.
    # rta_freq [:,1] -= SM57_1k #A c/ rta en frecuencia le resto el valor que tiene la curva a incidencia 0º para 1k Hz
    SM57_rta_freq_list.append (rta_freq)
#%%
# =============================================================================
    "A continuación hago el suavizado de los datos y grafico la rta en Frecuencia"
# =============================================================================
#%%
"SM57 ---> Le hago suavizado en 1/3 de Octava"
SM57_rta_freq_smoothed_list = [] #Una lista que va a tener las amplitudes ya suavizadas y con 1kHz valiendo 0dB
for index, rta_freq in enumerate(SM57_rta_freq_list):
    rta_smoothed = suavizado(rta_freq[:,0], rta_freq [:,1], 3) #Suavizo cada rta en frecuencia con el code que hizo Pedro
    if index == 0: #Si estoy viendo incidencia a 0º
        index_1k = np.where (999<rta_freq [:,0])[0][0] #index para el cual la frecuencia es 1kHz
        magnitud_1k = rta_smoothed [index_1k] #Obtengo el valor que la curva (ya suavizada) tiene en 1kHz
    rta_smoothed -= magnitud_1k #A la curva suavizada le resto ese valor.
    SM57_rta_freq_smoothed_list.append (rta_smoothed) 
#%%
#Defino un par de boludeces para despues graficar
incidencia = ["Incidencia a 0º","Incidencia a 65º","Incidencia a 90º","Incidencia a 180º"]
linestyle = ["dotted","dashed","dashdot","solid"]
color = ["black","orange","red","green"]
freqs_interes = [30,60,100,125,250,500,1000,2000,4000,8000,10000,12000,16000,20000]
freqs_interes_labels = ["30Hz","60Hz","100Hz","125Hz","250Hz","500Hz","1kHz","2kHz","4kHz","8kHz","10kHz","12kHz","16kHz","20kHz"]
dB_interes = [12,9,6,3,0,-3,-6,-9,-12,-15,-18,-21,-24,-30]
dB_interes_labels = ["12dB","9dB","6dB","3dB","0dB","-3dB","-6dB","-9dB","-12dB","-15dB","-18dB","-21dB","-24dB","-30dB"]

"SM57 ---> Grafico la rta en frecuencia"

plt.figure()
for index, rta_freq_smoothed in enumerate(SM57_rta_freq_smoothed_list):
    plt.plot (SM57_rta_freq_list [index][:,0], rta_freq_smoothed, label=incidencia[index], linestyle=linestyle[index], color=color[index])
plt.xscale("log", basex=10)
plt.rcParams ["font.size"] = 14
plt.title ("Respuesta en frecuencia según ángulo de incidencia para Shure SM57 con patrón polar cardioide",fontsize=20)
plt.xlabel ("Frecuencia",fontsize=18)
plt.ylabel ("Magnitud",fontsize=18)
plt.legend (fontsize=16)
plt.xticks (freqs_interes,freqs_interes_labels)
plt.yticks  (dB_interes,dB_interes_labels)
plt.xlim (95,20000) #Arrancaba en 95 incluso antes de estandarizar a 95
plt.ylim (-17,9)
plt.grid (True, which="both")