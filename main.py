import cv2
import audiofile as af
drum_sounds = {
    'hihat': 'hi hat.wav',
    'kick': 'kick.wav',
    'crash': 'crash.wav',
    'tom': 'tom.wav',
    'clap': 'clap.wav',
    'snare': 'snare.wav'
}
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if 300 < x < 500 and 100 < y < 300:
                if w > 200:
                    cv2.putText(frame, 'Crash', (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    af.play(drum_sounds['crash'])
                elif w > 150:
                    cv2.putText(frame, 'Tom 3', (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    af.play(drum_sounds['snare'])
                else:
                    cv2.putText(frame, 'Tom 2', (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    af.play(drum_sounds['clap'])
            elif 100 < x < 300 and 100 < y < 300:
                if w > 200:
                    cv2.putText(frame, 'Hihat', (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    af.play(drum_sounds['hihat'])
                elif w > 150:
                    cv2.putText(frame, 'Tom 1', (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    af.play(drum_sounds['tom'])
                else:
                    cv2.putText(frame, 'Kick', (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    af.play(drum_sounds['kick'])
    cv2.imshow('Drum Trigger', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
