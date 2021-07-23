###### Contoh Image processing untuk UAS #######
import cv2
gambar_input = cv2.imread('selfhealing.jpg') #untuk load gambarnya

cv2.imshow('selfhealing menurutku',gambar_input) #untuk menampilkan gambar

cv2.waitKey(0) #tekan ESC untuk keluar
cv2.destroyAllWindows()