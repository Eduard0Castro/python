import cv2
from pathlib import Path
import numpy as np

path = Path().absolute().parent.parent

class ImagesProcessing:
    def __init__(self, img):
        self.img = img
        self.__rows = img.shape[0]
        self.__cols = img.shape[1]
        self.proportion = self.__cols//self.__rows

    @property
    def rows(self):
        return self.__rows
    @property
    def cols(self):
        return self.__cols
    
    def cut(self, width, height):
        new = self.img[0:width, 0: height]
        return new
    
    def binary(self, thresh, inv = False):
        if inv == False:
            type = cv2.THRESH_BINARY

        elif inv == True:
            type = cv2.THRESH_BINARY_INV

        else:
            type = cv2.THRESH_BINARY
            print("Valor de tipo incorreto, setado como False")

        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, thresh, 255, type)

        return binary
    
    def negative(self, c1x = -1, c1y = -1, c2x = -1, c2y = -1):
        coordenadas = [c1x, c1y, c2x, c2y]
        negative = self.img.copy()

        while coordenadas[0] < 0 or coordenadas[0] > self.__cols:
            coordenadas[0] = int(input("Digite o x para a coordenada de início: "))

        while coordenadas[1] < 0 or coordenadas[1] > self.__rows:
            coordenadas[1] = int(input("Digite o y para a coordenada de início: "))

        while coordenadas[2] < 0 or coordenadas[2] > self.__cols:
            coordenadas[2] = int(input("Digite o x para a coordenada final: "))

        while coordenadas[3] < 0 or coordenadas[3] > self.__rows:
            coordenadas[3] = int(input("Digite o y para a coordenada final: "))

        for i in range(coordenadas[0], coordenadas[2]):
            for j in range(coordenadas[1], coordenadas[3]):
                negative[j, i, 0] = 255 - self.img[j, i, 0] 
                negative[j, i, 1] = 255 - self.img[j, i, 1] 
                negative[j, i, 2] = 255 - self.img[j, i, 2] 

        return negative
    
    def swap(self):

        swapped = self.img.copy()
        sequence = [2, 1, 3, 0]

        metadeX = self.__cols//2
        metadeY = self.__rows//2
        roi = [(0, 0, metadeX, metadeY), 
               (metadeX, 0, self.__cols, metadeY),
               (0, metadeY, metadeX, self.__rows),
               (metadeX, metadeY, self.__cols, self.__rows)]
        
        for i in range(0,4):
            region = self.img[roi[i][1]:roi[i][3], roi[i][0]:roi[i][2]]
            swapped[roi[sequence[i]][1]:roi[sequence[i]][3], 
                    roi[sequence[i]][0]:roi[sequence[i]][2]] = region
            
        return swapped
    
    def warp(self, x1, y1, x2, y2, x3, y3, x4, y4):
        width = 500
        height = width//self.proportion

        src = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        destiny = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        matriz = cv2.getPerspectiveTransform(src, destiny)

        warpped = cv2.warpPerspective(self.img, matriz, (width, height))

        return warpped

eneas = cv2.imread(f"{path}/Open-CV/Images/eneas.jpg")
cube = cv2.imread(f"{path}/Open-CV/Images/cube.jpeg")
teste = ImagesProcessing(eneas)
cube = ImagesProcessing(cube)

negative = teste.negative(0, 0, 354, 472)
swapped = teste.swap()
binary = teste.binary(127, True)
julio = cube.warp(55, 179, 208, 212, 126, 386, 279, 427)

cv2.imshow("Binary", binary)
cv2.imshow("Negative", negative)
cv2.imshow("Swapped", swapped)
cv2.imshow("Julio", julio)

cv2.waitKey()