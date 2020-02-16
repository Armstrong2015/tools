import numpy as np
import time
import cv2

def EM_EM2(temp):
    array = temp.reshape(1,-1)
    EM_sum = np.double(np.sum(array[0]))

    square_arr = np.square(array[0])
    EM2_sum = np.double(np.sum(square_arr))
    return EM_sum,EM2_sum


def EI_EI2(img, u, v,temp):
    height, width = temp.shape[:2]
    roi = img[v:v+height, u:u+width]
    array_roi = roi.reshape(1,-1)

    EI_sum = np.double(np.sum(array_roi[0]))

    square_arr = np.square(array_roi[0])
    EI2_sum = np.double(np.sum(square_arr))
    return EI_sum,EI2_sum


def EIM(img, u, v, temp):
    height, width = temp.shape[:2]
    roi = img[v:v+height, u:u+width]
    product = temp*roi*1.0
    product_array = product.reshape(1, -1)
    sum = np.double(np.sum(product_array[0]))
    return sum

def Match(img, temp):
    imgHt, imgWd = img.shape[:2]
    height, width = temp.shape[:2]

    uMax = imgWd-width
    vMax = imgHt-height
    temp_N = width*height
    match_len = (uMax+1)*(vMax+1)
    MatchRec = [0.0 for _ in range(0, match_len)]
    k = 0

    EM_sum, EM2_sum = EM_EM2(temp)
    for u in range(0, uMax+1):
        for v in range(0, vMax+1):
            EI_sum, EI2_sum = EI_EI2(img, u, v, temp)
            IM = EIM(img,u,v,temp)

            numerator=(  temp_N * IM - EI_sum*EM_sum)*(temp_N * IM - EI_sum * EM_sum)
            denominator=(temp_N * EI2_sum - EI_sum**2)*(temp_N * EM2_sum - EM_sum**2)

            ret = numerator/denominator
            MatchRec[k]=ret
            k+=1
        print('进度==》[{}]'.format(u/(vMax+1)))

    val = 0
    k = 0
    x = y = 0
    for p in range(0, uMax+1):
        for q in range(0, vMax+1):
            if MatchRec[k] > val:
                val = MatchRec[k]
                x = p
                y = q
            k+=1
    print ("val: %f"%val)
    return (x, y)

def main():
    temp= cv2.imread('C:/Users/hichens/Desktop/CV_code/images/mario_coin.png', cv2.IMREAD_GRAYSCALE)
    img= cv2.imread('C:/Users/hichens/Desktop/CV_code/images/mario.png', cv2.IMREAD_GRAYSCALE)

    tempHt, tempWd = temp.shape
    (x, y) = Match(img, temp)
    cv2.rectangle(img, (x, y), (x+tempWd, y+tempHt), (255,0,0), 2)
    print(x, y, tempWd, tempHt)
    cv2.imshow("temp", temp)
    cv2.imshow("result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Total Spend time：", str((end - start) / 60)[0:6] + "分钟")

'''
val: 1.000025
Total Spend time： 0.0866分钟
'''
