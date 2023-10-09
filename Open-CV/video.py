import cv2

#definir o codec (vai fazer de maneira mais eficiente a admnistracao do tamanho do video) e criar um objeto VideoWriter
# fourcc =  especifica o codec que vai ser usado para escrever o arquivo do video
# depende da sua instalacao do opencervejas e da config do sistema: (vou tentar com MJPG - Motion JPEG)
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#variaveis para redimensionar largura e altura do stream
width = 640
height = 480

# Loop de captura de frames e os escreve no arquivo do video
while True:
    ret, frame = cap.read()
    if not ret:
        print("Captura nao funcionou")
        break
    resized = cv2.resize(frame, (width, height))
    espelhada = cv2.flip(resized, 1)
    #convert = cv2.cvtColor(resized, cv2.COLOR_RGB2BGR)
# adicionar o frame ao arquivo do video
    output.write(espelhada)

# mostrar o frame com as convercoes 
    cv2.imshow('Video', espelhada)

# sair do loop quando apertar Q
    if cv2.waitKey(1) == ord('q'):
        break

output.release()
cap.release()
cv2.destroyAllWindows()