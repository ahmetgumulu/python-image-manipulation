import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose 
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils

#cap = cv2.VideoCapture("video4.mp4")
# doğrudan kameradan görüntü alma
cap = cv2.VideoCapture(0)

pTime = 0
while True:
    succsess, img = cap.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRGB)
    #print(result.pose_landmarks)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(result.pose_landmarks.landmark):
            h,w,_ = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            if id == 4:
                cv2.circle(img, (cx,cy), 5, (255,0,0),cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, "FPS: "+ str(int(fps)), (10,65), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)
    




    cv2.imshow("img",img)
    cv2.waitKey(25)