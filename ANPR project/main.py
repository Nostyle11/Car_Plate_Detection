import cv2
import matplotlib.pyplot as plt
import easyocr
from IPython.display import Image

def process_image(image_path):
    reader = easyocr.Reader(['en'])
    img = cv2.imread(image_path)
    output = reader.readtext(img)
    print(output)

if __name__ == "__main__":

    harcascade = "model/haarcascade_russian_plate_number.xml"

    cap = cv2.VideoCapture(0)

    cap.set(3, 640) # width
    cap.set(4, 480) #height

    min_area = 500
    count = 0

    while True:
        success, img = cap.read()

        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x,y,w,h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

                img_roi = img[y: y+h, x:x+w]
                cv2.imshow("ROI", img_roi)

        cv2.imshow("Result", img)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            imgout_path = "plates/scaned_img_" + str(count) + ".jpg"
            cv2.imwrite(imgout_path, img_roi)

            process_image(imgout_path)

            cv2.waitKey(500)
            count += 1
