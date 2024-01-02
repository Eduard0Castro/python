import cv2
from pathlib import Path

path = Path().absolute().parent
print(path)

img = cv2.imread("{}/Images/fifty.bmp" .format(path))

cut  = img[0:300, 0:500]

cv2.imwrite(f"{path}/Images/fifty_cut.bmp", cut)
cv2.imshow("Cut", cut)

key = cv2.waitKey(0)

if key == 'q':
    cv2.destroyAllWindows()
