import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\saras\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('Resources/Screenshot 2021-03-04 225707.png')
#To convert BGR to RGB as tesseract works with RGB only
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))   #To get the string from image
#print(pytesseract.image_to_boxes(img))  # we get x,y,h,w for each letter

hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
print(boxes)

for b in boxes.splitlines():
    print(b)
    b=b.split(' ')   # split values based on ' ' as delimiter
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    # we here use a different arguments here for rectangle coz the ourput they gave is not in our  expected order
    # just try it yourself
    cv2.putText(img, b[0],(x,hImg-y),cv2.FONT_HERSHEY_COMPLEX,0.25, (50,50,255),2)


img = cv2.resize(img, (600,450) )
cv2.imshow("result",img)
cv2.waitKey(0)









