from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) У нас есть пять семей по 4 человека.', fontsize=15)
plt.text(0.01, 0.8, '6 человек заболели, но в 2-х семьях.', fontsize=15)
plt.text(0.01, 0.7, 'Решение:', fontsize=15)
form = r"$C_{20}^6*C_5^2*((C_4^3)^2 + C_2^1*C_4^2*C_4^4)$"
plt.text(0.01, 0.6, form, fontsize=15)
plt.text(0.01, 0.5, 'Если заболели в 3-х семях:', fontsize=15)
form = r"$C_{20}^6C_5^3((C_4^2)^3 + C_3^1C_4^1C_2^1C_4^2C_4^3 + C_3^2C_4^1C_4^1C_4^4)$"
plt.text(0.01, 0.4, form, fontsize=15)
plt.text(0.01, 0.3, 'Если заболели во всех семях:', fontsize=15)
form = r"$C_{20}^6*C_5^5*((C_5^1*C_4^2*(C_4^1)^4)$"
plt.text(0.01, 0.2, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '2) У нас есть семейные пары. Нам нужно', fontsize=15)
plt.text(0.01, 0.8, 'рассадить их вокруг круглого стола', fontsize=15)
plt.text(0.01, 0.7, 'чередуя мужчин и женщин. Решение:', fontsize=15)
form = r"$f(m, k) = C_{m-k}^k + C_{m-k-1}^{k-1} = \frac{m}{m-k}*C_{m-k}^k$"
plt.text(0.01, 0.5, form, fontsize=15)
plt.text(0.01, 0.3, 'Если посчитать, то выходит 2 способами', fontsize=15)
plt.text(0.01, 0.2, 'мы сможем рассадить людей и не важно', fontsize=15)
plt.text(0.01, 0.1, 'количество людей если все по парам.', fontsize=15)
plt.text(0.01, 0.01, 'Либо муж, жен, либо жен, муж.', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()