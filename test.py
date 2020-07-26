# -*- encoding=utf-8 -*-
from image_similarity_function import *
from img_aug import *
from main2 import *
import os
import shutil
from scipy.misc import imsave

def test():
    folder = 'D:/Data/all_process'
    lis = ['001','002','003','004','005','006','007','008','009','010']
    for i in lis:

        #给出路径
        img1_path1='D:/Data/all_test/'+i+'.bmp'
        img2_path1 = 'D:/Data/all_test/' + i + '-0.bmp'
        img1_path2= folder+'/'+i + 'p5.bmp'
        img2_path2= folder+'/'+i +'-0p5.bmp'

        #图像1处理
        img1 = cv2.imread(img1_path1, 0)


        # img1 = thre(img1, 'BI', adap_thre - 20)
        #img1 = log(42,img1)
        img1 = gamma(img1, 0.005, 5.0)
        # img1 = img_mor(img1, 4)
        #img1 = thre(img1, 'BI', 150)
        img1 = img_process(img1)

        img_showandwrite(img1, folder, name='/' + i)

        #图像2处理
        img2 = cv2.imread(img2_path1, 0)

        img2 = gamma(img2, 0.005, 5.0)
        img2 = img_process(img2)
        #img2=log(42,img2)
        # img2 = img_mor(img2, 4)
        #img2 = thre(img2, 'BI', 180)
        img_showandwrite(img2, folder, name='/' + i+'-0')

        kk = calc_image_similarity(img1_path2, img2_path2)


if __name__ == '__main__':
    test()