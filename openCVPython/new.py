import cv2

cap = cv2.VideoCapture("Resources/BarrelVideo.mp4")
image = cv2.imread("Resources/ezgif-frame-001.jpg")
frameWidth= 640
frameHeight = 480
path = 'Resources/cascade_3.xml'
objectName = 'survivor'
color = (255,0,255)
#while True:
    #success, img = cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(60) & 0xFF == ord('x'):
        #break
def empty():
    pass

cascade = cv2.CascadeClassifier(path)
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",15,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",0,50,empty)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    scaleVal = 1+ (cv2.getTrackbarPos("Scale", "Result")/1000)
    neig = cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray, scaleVal, neig)

    for (x, y, w, h) in objects:
        area = w * h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            cv2.putText(img, objectName, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            roi_color = img[y:y + h, x:x + w]

    cv2.imshow("Result", img)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
        cap.release()