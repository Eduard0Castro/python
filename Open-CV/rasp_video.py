import cv2

# Endereço IP da Raspberry Pi
ip_address = '192.168.1.122'  # Substitua pelo endereço IP da sua Raspberry Pi

# URL do streaming da câmera
stream_url = f'rtsp://{ip_address}:8554/stream'

# Inicialize o objeto VideoCapture com a URL do streaming
stream = cv2.VideoCapture(stream_url)

while True:
    # Capture um quadro do streaming
    _, frame = stream.read()

    # Exiba o quadro em uma janela
    cv2.imshow('Streaming', frame)

    # Se pressionar 'q', saia do loop
    if cv2.waitKey(1) == ord('q'):
        break

# Libere os recursos
stream.release()
cv2.destroyAllWindows()