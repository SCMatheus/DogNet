import cv2

cachorro = 'Baby'
numVid = 1
rotacao = False
rotacaoNegativa = False
for y in range(1,numVid+1):
# Opens the Video file
    cap= cv2.VideoCapture(cachorro.lower()+str(y)+'.mp4')
    i=1
    dim = (224,224)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i%15 == 0 or i == 1:
            if rotacao == True:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            elif rotacaoNegativa == True:
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
            resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite('./'+cachorro+'/vd'+str(y)+'_'+str(i)+'.png',resized)
        i+=1
    
    cap.release()
    cv2.destroyAllWindows()