import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

x_data = [1,1,2,3,4,5,6,7,8,9,10,11]
y_data = [1,2,3,1,4,5,6,4,7,10,15,9]

plt.figure()
plt.plot(x_data,y_data, 'ro')
plt.title('Height vs Weight')
plt.xlabel('Weight')
plt.ylabel('Height')
# plt.savefig('plot.jpg')
plt.show()
