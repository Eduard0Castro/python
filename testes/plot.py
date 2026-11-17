import matplotlib.pyplot as plt
import numpy as np


freq_sinal = 60
periodo_sinal = 1/freq_sinal
t_final = 2*periodo_sinal
pontos = 500

t = np.linspace(0, t_final, pontos)
sen = np.sin(2*np.pi*freq_sinal*t)
coss = np.cos(2*np.pi*freq_sinal*t)

print("Tempo do Step (período de amostragem): ", step := t_final/pontos)
print("Numero de amostras (resolução): ", np.round(t_final/step, 1))
print("Frequencia de amostragem: ", 1/step)
print("Frequência do sinal: ", freq_sinal)
print("Período do sinal: ", periodo_sinal)

plt.figure()
plt.plot(t, sen, label='Senoide', color = "Red")
plt.plot(t, coss, label = "Cosseno", color = "Blue")
plt.grid(True)
plt.legend()
plt.show()
