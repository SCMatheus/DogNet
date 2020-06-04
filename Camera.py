import cv2
import numpy as np
from keras.preprocessing import image
from keras.models import load_model


classificador = load_model('DogNet')


video = cv2.VideoCapture(0)
a = 0
dim = (64,64)
while True:
    a = a + 1
    
    check, frame = video.read()
    
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    imagem_teste = image.img_to_array(resized)
    imagem_teste /= 255
    imagem_teste = np.expand_dims(imagem_teste, axis = 0)
    previsao = classificador.predict(imagem_teste)
    #labels = np.argmax(previsao, axis=-1) 
    labels = (previsao > 0.5)
    
    if labels == 0:
        classe = "Fred"
    elif labels == 1:
        classe = "kika"

    videoFinal = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (150,40)
    fontScale              = 1
    fontColor              = (0,0,255)
    lineType               = 2
    
    cv2.putText(videoFinal,classe, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    cv2.imshow("Capturing", videoFinal)
    
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()