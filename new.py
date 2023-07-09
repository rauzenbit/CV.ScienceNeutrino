from itertools import chain
from astropy.time import Time
import numpy as np
import matplotlib.pyplot as plt

read_file = '/home/sonya/Nauchka/Science work/fileofdata.txt'
write_file = '/home/sonya/Nauchka/Science work/Data1.txt'
with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
    for line in fr:
        linei = line.split()[:3]
        lineii = ' '.join(linei)
        fw.write(lineii + "\n")

f = open('/home/sonya/Nauchka/Science work/Data1.txt', 'r')
lineii = f.readlines()

galactic_center_RA = (266.404996-360) * np.pi / 180
galactic_center_DEC = -28.936172 * np.pi / 180
Ra=77.358185 * np.pi / 180
Dec = 5.693148 * np.pi / 180

def arrays(split_beggining, split_end):
    value_name = []
    for line in lineii:
        value_name.append(line.split()[split_beggining:split_end])
    value_name = list(chain(*value_name))
    value_name = [float(a) for a in value_name]
    return(value_name)
    
t = arrays(0, 1)
x = arrays(1, 2)
y = arrays(2, 3)

ind2011 = []
x2011 = []
y2011 = []
for i in range(0, len(x)): 
    tau = Time(t[i], format='mjd')
    tau.format = 'byear'
    t[i] = tau.value
    if t[i] < 2019 and t[i] >= 2018:
        ind2011.append(i)
print(ind2011)
for i in ind2011:
    x2011.append((x[i]-180)*np.pi/180)
    y2011.append(y[i]*np.pi/180)
print(x2011, y2011)

# def picture_of_year(time, indicies, year, x, y):
#     indicies=[]
#     for i in range(0, len(x)):
#         tau = Time(t[i], format='mjd')
#         tau.format = 'byear'
#         t[i] = tau.value
#         print(t[i])

# t2012 = []
# ind2012 = []
# for i in range(0, len(x)): 
#     tau = Time(t[i], format='mjd')
#     tau.format = 'byear'
#     t[i] = tau.value
#     if t[i] < 2013:
#         ind2012.append(i)
# x2012 = []
# y2012 = []
# for i in ind2012:
#     x2012.append(x[i])
#     y2012.append(y[i])
# plt.figure(figsize=(10,5))
# plt.subplot(111, projection="aitoff")
# plt.grid(True)
# plt.scatter(galactic_center_RA, galactic_center_DEC, marker='*', s=10, c='red')
# plt.scatter(Ra, Dec, s=10, c='black', marker="*")
# plt.plot(x2012, y2012, 'o', markersize=2, alpha=0.3)
# plt.subplots_adjust(top=0.95,bottom=0.0)
# plt.show()

plt.figure(figsize=(10,5))
plt.subplot(111, projection="aitoff")
plt.grid(True)
plt.title("Events 2018")
plt.scatter(galactic_center_RA, galactic_center_DEC, marker='*', s=10, c='red')
plt.scatter(Ra, Dec, s=10, c='black', marker="*")
plt.scatter(x2011, y2011, marker='o', s=5, alpha=0.3)
plt.subplots_adjust(top=0.95,bottom=0.0)
plt.show()
f.close()