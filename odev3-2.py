import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("./dataset_soru2.csv")
print(dataset.head())

s = dataset['s_n(kPa)']
t_p = dataset['t_p(kPa)']
t_r = dataset['t_r(kPa)']

plt.scatter(s, t_p, color='steelblue')
plt.scatter(s, t_r, color='darkgreen')

#sigma-tau grafikleri
def peakgraph():
    m, b = np.polyfit(s, t_p, 1)
    c_p = b
    phi_peak = math.degrees(math.atan(m))
    print("phi_p =", phi_peak)
    plt.axline((0, b), slope= m, color='steelblue')
    plt.text(0, b, f'c_p={c_p:.2f}', color='steelblue' ,verticalalignment='bottom', horizontalalignment='right')
    plt.text(0.05, 0.95, f'c_p = {c_p:.2f}', transform=plt.gca().transAxes, fontsize=14, color='steelblue', verticalalignment='top', horizontalalignment='left')
    plt.text(0.05, 0.90, f'$\phi$_p = {phi_peak:.2f}', transform=plt.gca().transAxes, fontsize=14, color='steelblue' ,verticalalignment='top', horizontalalignment='left')

    x_text = max(s) * 0.9  # Adjust the position of the text along the x-axis
    y_text = m * x_text + 1
    plt.text(x_text, y_text, fr'$\tau$ = c_p + $\sigma$tan($\phi$_p)', fontsize=14, rotation=phi_peak, color='steelblue', verticalalignment='bottom', horizontalalignment='right')

    return m, b, c_p, phi_peak

peakgraphvals = peakgraph()
print(peakgraphvals)

def residualgraph():
    m, b = np.polyfit(s, t_r, 1)
    c_r = b
    phi_residual = math.degrees(math.atan(m))
    print("phi_res =", phi_residual)
    plt.axline((0, b), slope= m, color='darkgreen')
    plt.text(0, b, f'c_r={c_r:.2f}', color='darkgreen' ,verticalalignment='bottom', horizontalalignment='right')
    plt.text(0.95, 0.1, f'c_r = {c_r:.2f}', transform=plt.gca().transAxes, fontsize=14, color='darkgreen', verticalalignment='bottom', horizontalalignment='right')
    plt.text(0.95, 0.05, f'$\phi$_r = {phi_residual:.2f}', transform=plt.gca().transAxes, fontsize=14, color='darkgreen' ,verticalalignment='bottom', horizontalalignment='right')

    x_text = max(s) * 0.9  # Adjust the position of the text along the x-axis
    y_text = m * x_text - 1
    plt.text(x_text, y_text, fr'$\tau$ = c_r + $\sigma$tan($\phi$_r)', fontsize=14, rotation=phi_residual, color='darkgreen', verticalalignment='bottom', horizontalalignment='right')

    return m, b, c_r, phi_residual

resgraphvals = residualgraph()
print(resgraphvals)

plt.ylim(bottom=0)
plt.xlim(left=0)
plt.xlabel(r'$\sigma$ (kPa)', fontsize=16)
plt.ylabel(r'$\tau$ (kPa)', fontsize=16)
plt.show()