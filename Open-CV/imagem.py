import cv2

#inicialização da webcam
cap = cv2.VideoCapture(0)

#Verificação de funcionamento da webcam
if not cap.isOpened():
    print("Webcam não iniciou.")
    exit()

#captura de um frame como imagem
ret, frame = cap.read()
if not ret:
    print("Captura de imagem falhou.")    
    exit()
vuaida  = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#Salvamento da imagem
cv2.imwrite("mestre.jpg", vuaida)    

cap.release()
