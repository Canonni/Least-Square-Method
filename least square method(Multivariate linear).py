import matplotlib.pyplot as plt
from pylab import mpl
from numpy import *  # 导入numpy的库函数
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math

#多元线性拟合#
def calculate_parameter(data_x1,data_x2,data_x3,data_y):

    a1 = mat(data_x1).T
    a2 = mat(data_x2).T
    a3 = mat(data_x3).T
    b = mat(data_y).T

    A = mat(hstack((a1, a2, a3 )))
    B = mat(b)

    A_T = A.T
    parameter = (A_T*A).I*A_T*B
    return parameter

def calculate(data_x1, data_x2, data_x3, parameters):
    fitting_data_y = []
    i = 0
    while i < len(data_x1):
        result = parameters[2]+parameters[1]*data_x2[i]+parameters[0]*data_x1[i]
        i += 1
        fitting_data_y.append(result)
    return fitting_data_y

def draw( x1, x2, old_y, new_y):
    # 创建绘图函数对象
    fig = plt.figure()
    # 创建Axes3D对象，让其包含图像3D坐标
    ax = Axes3D(fig)
    ax.scatter( x1, x2, old_y, color='red')
    ax.plot( x1, x2, new_y, color='black')
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("多元线性拟合数据")
    plt.show()


x1 = [2, 4, 5, 8, 9]
x2 = [3, 5, 7, 9, 12]
x3 = [1, 1, 1, 1, 1]
y = [48, 50, 51, 55, 56]
fit_y = []
parameters=calculate_parameter( x1, x2, x3, y)
newY = calculate(x1, x2, x3, parameters)
for m in newY:
    fit_y.append(int(m))
print (fit_y)
draw( x1, x2, y, fit_y)
