import matplotlib.pyplot as plt
import math

grade = []
sine = []
cosine = []
tangent = []
x = []
y = []
for i in range(0,540):
    grade.append(i)
    radians = (i*math.pi)/180
    sine.append(math.sin(radians))
    cosine.append(math.cos(radians))
    tangent.append(math.tan(radians))
#     x.append(i)
#     y.append(i)

# plt.ylim(-100,100)
plt.ylim(-2,2)
plt.plot(grade,sine,"r")    # sine
plt.plot(grade,cosine,'y')  # cosine
plt.plot(grade,tangent,'b') # tangent line
# plt.plot(x,y,"p")

# x_val = [1,2,3,4,5,6]
# y_val = [6,5,4,3,2,1]
# 
# plt.plot(x_val,y_val,'y')
plt.show()