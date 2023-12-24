import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("./stress_dataset.csv")
print(dataset.head())

sigma_3 = dataset['s3(MPa)']
sigma_1 = dataset['s1(MPa)']

p = (sigma_1 + sigma_3) / 2
q = (sigma_1 - sigma_3) / 2

dataframe = pd.DataFrame({'sigma_3': dataset['s3(MPa)'], 'sigma_1': dataset['s1(MPa)'], 'q': q, 'p': p})
print(dataframe)

m, b = np.polyfit(p, q, 1)
print("a=", b)
print("m=", m)
phi = math.degrees(math.asin(m))
print("phi=", phi)
c = b / math.cos(math.radians(phi))
print("c=", c)
tanphi = math.tan(math.radians(phi))
print("tan(phi) =", tanphi)

plt.scatter(p, q, marker='+', color='black')
#plt.plot(p, m*p+b, color='darkgreen')
plt.axline((0, b), slope= m, color='darkgreen')
plt.text(0.05, 0.95, f'a = {b:.2f}', transform=plt.gca().transAxes, fontsize=15, verticalalignment='top', horizontalalignment='left')
plt.text(0.05, 0.90, fr'tan($\alpha$) = {m:.2f}', transform=plt.gca().transAxes, fontsize=15, verticalalignment='top', horizontalalignment='left')
plt.text(0.05, 0.85, f'$\phi$ = {phi:.2f}', transform=plt.gca().transAxes, fontsize=15, verticalalignment='top', horizontalalignment='left')
plt.text(0.05, 0.80, f'c = {c:.2f}', transform=plt.gca().transAxes, fontsize=15, verticalalignment='top', horizontalalignment='left')
plt.ylim(bottom=0)
plt.xlim(left=0)
plt.xlabel('p', fontsize=16)
plt.ylabel('q', fontsize=16)
plt.title('p-q grafiği', fontsize=18)
plt.show()

#mohr

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
for index, row in dataframe.iterrows():
    mohr_circle = plt.Circle((row['p'], 0), row['q'], fill=False, color='black')
    ax.add_patch(mohr_circle)
ax.axis('equal')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.text(0, c, f'c={c:.2f}', color='steelblue', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(0.15, 0.95, f'$\phi$ = {phi:.2f}', transform=plt.gca().transAxes, fontsize=14, color='steelblue', verticalalignment='top', horizontalalignment='left')

#setting ylim to 0 for making only the upper half visible
ax.set_ylim(bottom=0)

plt.axline((0, c), slope= tanphi)
plt.xlabel(r'$\sigma$', fontsize=16)
plt.ylabel(r'$\tau$', fontsize=16)
plt.show()
