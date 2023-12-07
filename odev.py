import math
import numpy as np

#dataset containing 20 Schmidt values
dataset = np.array([21, 22, 25, 19, 25, 24, 22, 21, 19, 23, 23, 23, 24, 23, 20, 20, 22, 24, 23, 21])

#indices of the smallest 10 values
indices_of_smallest_10 = np.argpartition(dataset, 10)[:10]

#excluding the smallest 10 value
remaining_values = np.delete(dataset, indices_of_smallest_10)

# mean of the remainings
mean_of_remaining_values = np.mean(remaining_values)

print("Schmidt ort: ", mean_of_remaining_values)

#sırasıyla sigma_n değerlerinin tek tek girilmesi gerekiyor
#ilerleyen zamanlarda bunu tek bir aralık için belirlenen adım değeri (ödevde en az 10) için tek seferde yapan bir hale getireceğim ama şu anda vize amelesi olmakla meşgulüm.
sigma_n = 0.01  
jcs = 34
jrc = 14
phi = 20

#doğru sonuçlar elde edilebilmesi için sigma_n ve jcs değerleri aynı birim ve çarpan ile yazılmalı. 
# ör. ikisi de MPa veya kPa olmalı.

tau = sigma_n * math.tan(math.radians((jrc * math.log10(jcs / sigma_n)) + phi))

print("tau = ", tau)
