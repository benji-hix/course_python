# import cv2
# import numpy as np
# from cvzone.HandTrackingModule import HandDetector
# from keras import models
# from cvzone.ClassificationModule import Classifier
# import math
# import time
# import os

# cap = cv2.VideoCapture(1)
# detector = HandDetector(maxHands=1)
# # model = models.load_model('keras_model.h5')
# classifier = Classifier('./keras_model.h5', './labels.txt')

# offset = 20
# imgSize = 300
# counter = 0

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# #
# def activate():
#     message = ''
#     while True:
#         success, img = cap.read()
#         imgOutput = img.copy()
#         hands, img = detector.findHands(img)

#         if not success:
#             break

#         if hands:
#             hand = hands[0]
#             x, y, w, h = hand['bbox']

#             imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
#             imgCrop = img[y-offset:y + h, x-offset:x + w+offset]

#             imgCropShape = imgCrop.shape

#             aspectRatio = h/w

#             if aspectRatio > 1:
#                 k = imgSize/h
#                 wCalc = math.ceil(k * w)
#                 try:
#                     imgResize = cv2.resize(imgCrop, (wCalc, imgSize))
#                     imgResizeShape = imgResize.shape
#                     wGap = math.ceil((imgSize - wCalc) /2)
#                     imgWhite[:, wGap:wCalc+wGap] = imgResize
#                     prediction, index = classifier.getPrediction(imgWhite, draw=False)
#                     # print(prediction, index)
#                 except:
#                     print('no image')


#             elif aspectRatio < 1:
#                 try:
#                     k = imgSize / w
#                     hCalc = math.ceil(k * h)
#                     imgResize = cv2.resize(imgCrop, (imgSize, hCalc))
#                     imgResizeShape = imgResize.shape
#                     hGap = math.ceil((imgSize - hCalc) /2)
#                     imgWhite[hGap:hCalc+hGap, :] = imgResize
#                     prediction, index = classifier.getPrediction(imgWhite)
#                     # print(prediction, index)
#                 except:
#                     print('no image')

#             elif aspectRatio == 1:
#                 imgWhite[0:imgCropShape[0], 0:imgCropShape[1]] = imgCrop
#                 prediction, index = classifier.getPrediction(imgWhite, draw=False)
#                 # print(prediction, index)

#             try:
#                 cv2.putText(imgOutput, labels[index], (x-offset, y-offset-10), cv2.FONT_HERSHEY_PLAIN, 2.5, (255,255,255), 2)
#             except:
#                 print('no index')
#             cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w + offset, y + h + offset), (255, 255, 255), 3)
#             # cv2.imshow("imageCrop", imgCrop)
#             # cv2.imshow("imageWhite", imgWhite)

#         cv2.imshow("image", imgOutput)
#         key = cv2.waitKey(1)
#         if key == 9:
#             message += labels[index]
#         elif key == 32:
#             message += ' '
#         elif key == 13:
#             print(message)
#         elif key == 0:
#             message = ''
#         elif key == 27:
#             break
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__=='__main__':
#     activate()