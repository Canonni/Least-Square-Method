import matplotlib.pyplot as plt
from pylab import mpl
#一元线性拟合#
#采用的拟合原始数据为xi=1,2,3,4,5,6,7#
#对应的相应函数值yi=0.5,2.5,2,4,3.5,6,5.5#

x = [1, 2, 3, 4, 5, 6, 7]
y = [5.9,6.8,9.3,10.9,13.7,15.9,16.6]


#拟合曲线参数计算函数#

def liner_fitting(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_xy = 0
    sum_y = 0
    sum_x = 0
    sum_sqare_x = 0
    average_x = 0
    average_y = 0
    while i < size:  # 求出各项∑值
        sum_xy += data_x[i]*data_y[i]
        sum_y += data_y[i]
        sum_x += data_x[i]
        sum_sqare_x += data_x[i]*data_x[i]
        i += 1
    average_x = sum_x / size
    average_y = sum_y / size
    fitting_k = (size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)    #计算出拟合曲线k、b的值
    fitting_b = average_y-average_x*fitting_k
    return [fitting_k, fitting_b]


#计算拟合后的曲线上的数值#

def calculate(data_x, k, b):
    fitting_data_y = []
    for x in data_x:
        fitting_data_y.append(k*x+b)
    return fitting_data_y


#函数绘制#

def draw(data_x, data_y_new, data_y_old):
    plt.plot(data_x, data_y_new, label="拟合曲线", color="black")
    plt.scatter(data_x, data_y_new, label="拟合后的数据",color="blue")
    plt.scatter(data_x, data_y_old, label="离散原始数据", color="red")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("一元线性拟合数据")
    plt.legend(loc="upper left")
    plt.show()


parameter = liner_fitting(x, y)
draw_data = calculate(x, parameter[0], parameter[1])
print('拟合曲线的方程为：y = %.2f * x + %.2f ' %(parameter[0], parameter[1]))
draw(x, draw_data, y)
