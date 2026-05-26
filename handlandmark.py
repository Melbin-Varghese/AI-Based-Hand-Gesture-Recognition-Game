def fingers_up(hand_landmarks, img):
    h, w, _ = img.shape
    lm = []

    for id, landmark in enumerate(hand_landmarks.landmark):
        lm.append((int(landmark.x * w), int(landmark.y * h)))

    fingers = []

    # Thumb (works for right hand)
    fingers.append(1 if lm[4][0] > lm[3][0] else 0)

    # Other fingers
    tips = [8, 12, 16, 20]
    for tip in tips:
        fingers.append(1 if lm[tip][1] < lm[tip - 2][1] else 0)

    return fingers
