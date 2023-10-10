import cv2

# Inicializando camera
camera = cv2.VideoCapture(0)
width = 320
height = 240

while True:
    # Capturando um quadro
    _, frame = camera.read()
    # Redimensionando o quadro
    resized_frame = cv2.resize(frame, (width, height))
    #Ajeitando as cores
    convert = cv2.cvtColor(resized_frame, cv2.COLOR_RGB2BGR)
    # Exibindo (aparentemente vai direto para o pc)
    cv2.imshow('Camera', convert)

    # 'q' pra sair 
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
