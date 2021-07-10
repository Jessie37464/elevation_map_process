# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import pylab as pl
import math


def as_num(x):
    y = '{:.10f}'.format(float(x))  # .10f 保留10位小数
    return round(float(y), 2)


def list_as_num(list_num):
    output = []
    for i in range(len(list_num)):
        output.append(as_num(list_num[i]))

    return output


# print(list_as_num(['-2.411965727806091309e-01', '-4.947362840175628662e-01']))
def trans_elevation():
    with open('elevation_data.txt') as f:
        elevation_matrix = []
        lines = f.readlines()
        for i in range(len(lines)):
            data = lines[i].strip().split()
            elevation_matrix.append(list_as_num(data))
    return elevation_matrix



trans_ele = trans_elevation()



def find_list_max(list_data):  #0.17
    max_num = -float('inf')
    for i in range(len(list_data)):
        max_num = max(max_num, max(list_data[i]))
    return max_num


def find_list_min(list_data):  #-1.41
    min_num = float('inf')
    for i in range(len(list_data)):
        min_num = min(min_num, min(list_data[i]))
    return min_num


#中间值-0.79
# print(trans_ele[29][29])




# np.savetxt('ele_result.txt', trans_ele2, fmt='%.2f')


# print(find_list_max(trans_ele2))


# np.savetxt('ele_result2.txt', trans_ele2, fmt='%.2f')
trans_ele = np.array(trans_ele)

trans_ele3 = np.c_[trans_ele, trans_ele[:, 0:4]]


trans_ele3 =  np.delete(trans_ele3, [0, 1, 2, 3], axis=1)




trans_ele2 = np.zeros((len(trans_ele3), len(trans_ele3[0])))
for i in range(len(trans_ele3)):
    for j in range(len(trans_ele3[0])):
        trans_ele2[i][j] = trans_ele3[i][j] + 0.74

print(trans_ele2[29][29])
# print(len(trans_ele3[0]))

for i in range(12):
    for j in range(15):
        if math.isnan(trans_ele2[i][j]):
            trans_ele2[i][j] = 0.88


for i in range(20):
    for j in range(35, 60):
        if math.isnan(trans_ele2[i][j]):
            trans_ele2[i][j] = 0.3

print(trans_ele2[29][29])
trans_ele2[32][29] = 0
trans_ele2[31][29] = 0
trans_ele2[30][29] = 0
trans_ele2[29][29] = 0
trans_ele2[28][29] = 0
trans_ele2[27][29] = 0

trans_ele2[29][27] = 0
trans_ele2[29][28] = 0
trans_ele2[29][29] = 0
trans_ele2[29][30] = 0
trans_ele2[29][31] = 0
trans_ele2[29][32] = 0


# print(find_list_max(trans_ele2))
# print(find_list_min(trans_ele2))
print(trans_ele2[28][26])
print(trans_ele2[20][22])
np.savetxt('ele_result3.txt', trans_ele2, fmt='%.2f')




