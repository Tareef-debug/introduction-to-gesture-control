import cv2
import mediapipe as mp
mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils#outline your hand
hands=mp_hands.Hands(max_num_hands=2)
cam=cv2.VideoCapture(0)
while True:
    success,frame=cam.read()
    if not success:
        print("error:colud not access webcam")
        break
    frame=cv2.flip(frame,1)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)
    #check if hand land marks were registered
    if result.multi_hand_landmarks:
        for landmark in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,landmark,mp_hands.HAND_CONNECTIONS)
    cv2.imshow("detected hand",frame)
    if cv2.waitKey(1) & 0XFF==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()