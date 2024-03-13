import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image

Image("/content/scaned_img_0.jpg")

reader = easyocr.Reader(['en'])

output = reader.readtext('/content/scaned_img_0.jpg')
#output

cord = output[-1][0]
#cord

a = list(zip(*cord))
#a
#min(a[0])
#min(a[1])
#max(a[0])
#max(a[1])

x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
#x_min, y_min

x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
#x_max, y_max

from pylab import rcParams
rcParams['figure.figsize'] = 20, 30

image = cv2.imread('/content/bottle.jpg')
cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))