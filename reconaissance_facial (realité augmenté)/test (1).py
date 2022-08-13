import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode = False,
max_num_hands = 2,
min_detection_confidence = 0.5,
min_tracking_confidence = 0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    hand=[]
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                hand.append([id,cx,cy])
                #if id ==0:
                cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
            #print(hand)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    xball = 20
    yball = 70
    # if len(hand) != 0:
    #     xball = hand[10][1]
    #     yball = hand[10][2]
    #cv2.putText(img, f'FPS:{int(fps)}', (xtext, ytext), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    #cv2.circle(img, (xball,yball), 30, (0,0,255), cv2.FILLED)

    testtext="Not Peace"
    if len(hand) != 0:
        if hand[16][2]>hand[13][2] and hand[20][2]>hand[17][2] and hand[8][2]<hand[6][2] and hand[12][2]<hand[10][2]:
            testtext = "Peace"
    cv2.putText(img, testtext, (250, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    

    # for i in range(len(hand)):
    #     cv2.putText(img, str(i), (hand[i][1],hand[i][2]),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Test", img)
    cv2.waitKey(1)