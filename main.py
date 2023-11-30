import matplotlib.pyplot as plt
import numpy as np
import math as m
import xml.etree.ElementTree as et
import os.path


def func(x):
    return ((6 * x - 2)**2) * m.sin(12 * x - 4)


xmin = 0
xmax = 1
step = 0.01
count = 100

xlist = np.arange(xmin, xmax, step)
# xlist = np.linspace(xmin, xmax, count)
ylist = []

for i in range(len(xlist)):
    y = func(xlist[i])
    ylist.append(y)

if os.path.exists('results') == False:
    os.mkdir('results')

plt.plot(xlist, ylist)
plt.savefig('results\plot_1.png', dpi=50, bbox_inches='tight')
plt.show()

data = et.Element('data')
item_row = et.SubElement(data, 'xdata')
for i in range(len(xlist)):
    item_x = et.SubElement(item_row, 'x')
    item_x.text = str(xlist[i])
item_row = et.SubElement(data, 'ydata')
for i in range(len(ylist)):
    item_y = et.SubElement(item_row, 'y')
    item_y.text = str(ylist[i])

ffile = et.ElementTree(data)
et.indent(ffile, space="\t", level=0)
ffile.write(r"results\results_1.xml", encoding="utf-8", xml_declaration=True)
