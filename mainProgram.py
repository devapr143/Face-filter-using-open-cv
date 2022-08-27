#mouth detection and applying effects using Facemesh
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('Resources/dog.png', cv2.IMREAD_UNCHANGED)
overlay2=cv2.imread('Resources/dogopen.png', cv2.IMREAD_UNCHANGED)


detector = FaceMeshDetector(maxFaces=1)
idList=[0,17,78,292]
while True:
    success, img=cap.read()
    img,faces=detector.findFaceMesh(img,draw=False)
    if faces:
        face=faces[0]
        for id in idList:
            #cv2.circle(img,face[id],5,(0,0,0),cv2.FILLED)
            cv2.circle(img,face[292],5,(0,0,255),cv2.FILLED)
            cv2.circle(img,face[78],5,(0,0,255),cv2.FILLED)
        #cv2.line(img,face[idList[0]],face[idList[1]],(0,255,0),1)
        #cv2.line(img,face[idList[2]],face[idList[3]],(0,255,0),1)
        vertical,_=detector.findDistance(face[idList[0]],face[idList[1]])
        horizontal,_=detector.findDistance(face[idList[2]],face[idList[3]])
        ratio=int((vertical/horizontal)*100)
#when adusting ratio according to your face uncomment the below statement then use that value
#to adjust the if elif statement parameters to ratio that will suit your opening and closing of mouth
#although you won't need adjust it as it works fine most of the time but in case you have smaller mouth the ratio needs to be lowered

        #print(ratio)
        if 75>ratio>55:
                xt, frame = cap.read()
                gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = cascade.detectMultiScale(gray_scale)
                for (x, y, w, h) in faces:
                    # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
                    overlay_resize = cv2.resize(overlay, (int(w * 1.5), int(h * 1.5)))
                    frame = cvzone.overlayPNG(frame, overlay_resize, [x - 60, y - 75])
                cv2.imshow('Display', frame)
                if cv2.waitKey(10) == ord('q'):
                    cv2.destroyWindow('Display')

                    break
        elif ratio>75:
            xt, frame = cap.read()
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray_scale)
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
                overlay_resize = cv2.resize(overlay2, (int(w * 1.8), int(h * 1.8)))
                frame = cvzone.overlayPNG(frame, overlay_resize, [x - 70, y - 50])
            cv2.imshow('Display', frame)
            if cv2.waitKey(10) == ord('q'):
                cv2.destroyWindow('Display')
                break
        else:
            cv2.imshow("Display", img)
            cv2.waitKey(1)


