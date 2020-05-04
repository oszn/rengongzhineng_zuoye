import cv2
import os
def cd():
    filelist=os.listdir("img/")
    # filelist=sorted(filelist)
    fps=8
    path="1.avi"
    fourcc=cv2.VideoWriter_fourcc('M','J','P','G')
    videa=cv2.VideoWriter(path,fourcc,fps,(500,900))
    for item in range(479):
            item='img/'+str(item)+".jpg"
            img=cv2.imread(item)
            videa.write(img)
    videa.release()
cd()
