import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image
#import nump as np

#np.detect_plate()

#print(Image("plates/scaned_img_0.jpg"))

reader = easyocr.Reader(['en'])

output = reader.readtext('plates/scaned_img_0.jpg')

print(output)
'''
cord = output[-1][0]

#print(cord)

a = list(zip(*cord))
print(a)

print(min(a[0]))
print(min(a[1]))
print(max(a[0]))
print(max(a[1]))



x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
#print(x_min, y_min)

x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
#print(_max, y_max)

from pylab import rcParams
rcParams['figure.figsize'] = 20, 30

image = cv2.imread('plates/scaned_img_0.jpg')
cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
'''