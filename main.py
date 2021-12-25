import cv2
import shutil
import os
import dropbox
import time
import random

from code import TransferData

start_time = time.time() 

def takePhotosOften():
    number = random.randint(0,100)
    videoCapture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCapture.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        start_time = time.time()
        result = False
    return imageName
    videoCapture.release()
    cv2.destroyAllWindows()

def uploadToDropbox(imageName):
    access_token = '_MJpD57MwlgAAAAAAAAAAQWPtnpiRAKdMZiLqVHAJqnz0F9yilMgv5Eb0b7t7LJ_'

    fileFrom = imageName
    fileTo = "/test/" + (imageName)
    dbx = dropbox.Dropbox(access_token)

    with open(fileFrom, "rb") as f: 
        dbx.files_upload(f.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = takePhotosOften()
            uploadToDropbox(name)
main()


