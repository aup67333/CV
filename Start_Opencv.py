import numpy as np
import cv2



class show(object):
    Showimage_be_called_times = 0

    def showfrompath(self,Image_Path):
        img = cv2.imread(Image_Path)
        cv2.namedWindow(Image_Path,0)
        cv2.moveWindow(Image_Path,
        self.Showimage_be_called_times*320,
        240)
        cv2.resizeWindow(Image_Path,320,240)
        cv2.imshow(Image_Path, img)
        self.Showimage_be_called_times += 1

    def showfromImg(self,Img):
        Title = str(self.Showimage_be_called_times)
        cv2.namedWindow(Title,0)
        cv2.moveWindow(Title,self.Showimage_be_called_times*320,240)
        cv2.resizeWindow(Title,320,240)
        cv2.imshow(Title, Img)
        self.Showimage_be_called_times += 1


Image1_path = 'C:/Users/aup67/Pictures/Lenna.jpg'
Image2_path = 'C:/Users/aup67/Pictures/Test.png'

showwindow = show()
show.showfrompath(showwindow,Image1_path)
show.showfrompath(showwindow,Image2_path)

img = cv2.imread(Image1_path)
(B,G,R) = cv2.split(img)
show.showfromImg(showwindow,B)
show.showfromImg(showwindow,G)
show.showfromImg(showwindow,R)
# cv2.imshow("B",B)
# cv2.imshow("G",G)
# cv2.imshow("R",R)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
msg = "hello world"
print(msg)


