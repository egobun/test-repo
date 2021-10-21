import numpy as np
import matplotlib.pyplot as plt
with open ("settings.txt","r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype=int)
fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(data_array)
ax.minorticks_on()
ax.set_title("График напряжения U(В) на конденсаторе в LC цепи от времени (с)")
ax.set_xlabel("Время(с)")
ax.set_ylabel("напряженеи(В)")
ax.grid(which = 'major', linewidth = 1.2 , color = 'red')
ax.grid(which = "minor", linestyle = '--',  linewidth = 0.6 , color = 'k')
ax.plot(label = "напряжение от времени")
ax.tick_params(which = 'major', length = 15 , width = 3)
ax.tick_params(which = 'minor', length = 8 , width = 2)
plt.legend(['U(В)'])
fig.set_figwidth(12)
fig.savefig("test.png")
plt.show()
