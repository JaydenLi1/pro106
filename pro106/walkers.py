import cv2
vid = cv2.VideoCapture('G:/Coding/python/pro106/walking.avi')
people_classifer = cv2.CascadeClassifier(
    'G:/Coding/python/pro106/haarcascade_fullbody.xml')

while (True):
    ret, frame = vid.read()
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    peoples = people_classifer.detectMultiScale(gray_video)

    for (x, y, w, h) in peoples:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('video', frame)

    if cv2.waitKey(25) == 32:
        break
print(len(peoples))
vid.release()
cv2.destroyAllWindows()
