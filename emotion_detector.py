def detect_emotion():
    import cv2
    from deepface import DeepFace

    cap = cv2.VideoCapture(0)
    print("Press 'q' to capture a frame and detect mood...")

    frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        cv2.imshow("Mood2Meal - Press 'q'", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=True)
        return result[0]['dominant_emotion']
    except Exception as e:
        print("Error detecting emotion:", e)
        return None
