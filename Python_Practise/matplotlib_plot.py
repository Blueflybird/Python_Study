import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

#-------------------------------------------
# x_data = [1,1,2,3,4,5,6,7,8,9,10,11]
# y_data = [1,2,3,1,4,5,6,4,7,10,15,9]
#
# plt.figure()
# plt.plot(x_data,y_data, 'ro')
# plt.title('Height vs Weight')
# plt.xlabel('Weight')
# plt.ylabel('Height')
# # plt.savefig('plot.jpg')
# plt.show()

#-------------------sin curve-----------

#设置x,y轴的数值（y=sinx）
x = np.linspace(0,10,1000)
y = np.sin(x)

#创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
plt.figure(figsize=(8,4))

#在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
plt.plot(x,y,"b--",label="$sin(x)$",color="red",linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Pyplot First Example")

#显示图示
plt.legend()

#显示图
plt.show()

#保存图
plt.savefig("sinx.jpg")










