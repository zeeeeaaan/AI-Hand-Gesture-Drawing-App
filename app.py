import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Default settings
draw_color = (255, 0, 255)   # Pink
brush_thickness = 10
eraser_thickness = 40

# Create a canvas for drawing
canvas = np.zeros((480, 640, 3), np.uint8)

def fingers_up(hand):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if hand.landmark[tip_ids[0]].x < hand.landmark[tip_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers
    for i in range(1, 5):
        if hand.landmark[tip_ids[i]].y < hand.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


cap = cv2.VideoCapture(0)
prev_x, prev_y = 0, 0

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        # DRAW LEFT COLOR PALETTE
        cv2.rectangle(frame, (0, 0), (80, 80), (255, 0, 0), -1)     # Blue
        cv2.rectangle(frame, (0, 80), (80, 160), (0, 255, 0), -1)   # Green
        cv2.rectangle(frame, (0, 160), (80, 240), (0, 0, 255), -1)  # Red
        cv2.rectangle(frame, (0, 240), (80, 320), (0, 255, 255), -1) # Yellow

        # RIGHT PANEL – ERASER BUTTON
        cv2.rectangle(frame, (560, 0), (640, 80), (255, 255, 255), -1)
        cv2.putText(frame, "ERASE", (565, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                fingers = fingers_up(hand_landmarks)

                index_tip = hand_landmarks.landmark[8]
                x = int(index_tip.x * w)
                y = int(index_tip.y * h)

                # ------- SELECT MODE (ALL 5 FINGERS UP) -------
                if fingers.count(1) == 5:
                    prev_x, prev_y = 0, 0

                    # Select colors (left)
                    if x < 80:
                        if 0 < y < 80:
                            draw_color = (255, 0, 0)
                        elif 80 < y < 160:
                            draw_color = (0, 255, 0)
                        elif 160 < y < 240:
                            draw_color = (0, 0, 255)
                        elif 240 < y < 320:
                            draw_color = (0, 255, 255)

                    # Select eraser (right)
                    if 560 < x < 640 and 0 < y < 80:
                        draw_color = (0, 0, 0)  # temporary flag → black means erasing

                    cv2.putText(frame, "SELECT MODE", (120, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

                # ------- DRAW MODE (ONLY INDEX FINGER UP) -------
                elif fingers == [0,1,0,0,0]:

                    # Show mode
                    mode_text = "ERASING" if draw_color == (0,0,0) else "DRAWING"
                    cv2.putText(frame, mode_text, (120, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255), 3)

                    # Start drawing
                    if prev_x == 0 and prev_y == 0:
                        prev_x, prev_y = x, y

                    # Eraser = draw white
                    if draw_color == (0, 0, 0):
                        cv2.line(canvas, (prev_x, prev_y), (x, y),
                                 (0, 0, 0), eraser_thickness)
                    else:
                        cv2.line(canvas, (prev_x, prev_y), (x, y),
                                 draw_color, brush_thickness)

                    prev_x, prev_y = x, y

                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Merge canvas with webcam view
        frame = cv2.addWeighted(frame, 0.7, canvas, 0.7, 0)

        cv2.imshow("AI Hand Drawing App", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
