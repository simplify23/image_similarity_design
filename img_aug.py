# -*- encoding=utf-8 -*-

# 导入包
import cv2
from functools import reduce
from PIL import Image
import numpy as np
import os
from skimage import morphology,color,data
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from scipy.misc import imsave
adap_thre = 0
total = 0

def double_img_process(img1,img2):
    pass

def img_process(src):
#展示，保存，强特征去除
    global adap_thre
    global total
    adap_thre = 0
    total = 0
    #src=thre(img1_path,False)
    # retval, src = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY)
    # #res2 = cv2.bitwise_not(res1)
    # result = cv2.bitwise_or(res1,src)
    #src = cv2.imread(img1_path, 0)
    rows,cols=src.shape
    for i in range(rows):
        for j in range(cols):
            if (src[i,j]<=80):
                src[i,j]=255
            else:
                adap_thre=adap_thre+src[i,j]
                total=total+1
    adap_thre=adap_thre//total

    # #打印阈值
    # print("阈值为",adap_thre)

    #这里给一手超参调整
    if adap_thre > 220 :
        adap_thre=adap_thre+20
    elif adap_thre <140 :
        adap_thre = adap_thre -10
    #src = thre(src True)

    #临时代码，二值化求个结果
    src = thre(src, 'BI', adap_thre-20 )

    return src


def thre(src, adap, thre_value=70):
    '''
    对图像进行二值化
    :param:图像
    :param is_adapteive: 是否自适应
    :param thre_value: 非自适应模式下的阈值
    :return: 二值化后的图像
    '''
    #中值滤波去除噪点
    src = cv2.medianBlur(src, 5)

    if adap=='OT':
        # result = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 195, 50)
        # 输入图 超小阈值赋的值 值域的操作方法 二值化操作类型 分块大小 常数项
        ret, result = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 输入图 阈值 超过或小于阈值赋的值 选择类型 otsu可自动寻找合适阈值
    elif adap=='TO':
        retval, result = cv2.threshold(src, thre_value, 255, cv2.THRESH_TOZERO)
    elif adap=='BI':
        retval, result = cv2.threshold(src, thre_value, 255, cv2.THRESH_BINARY)
    elif adap=='ADG':
        result = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 5)
    elif adap=='ADM':
        result = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 5)

    return result

def img_showandwrite(img,img_path,name):
    # cv2.imshow('not', img)
    # cv2.waitKey(2000)
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    #imsave(img_path + name + 'p5.bmp', img)
    cv2.imwrite(img_path + name + 'p5.bmp', img)
    return 0

def img_mor(src,c):
    '''
    开，闭，黑帽，顶帽运算
    :param img: 
    :return: 
    '''
    # 设置卷积核
    kernel = np.ones((10, 10), np.uint8)
    if c==1:
    # 图像顶帽运算
        result = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)
    elif c==2:
    #黑帽算法
        result = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)
    elif c==3:
    #开运算
        result = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel)
    else:
    #闭运算
        result = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)

    # 显示图像
    #cv2.imshow("src", src)
    #cv2.imshow("result"+str(c), result)

    # 等待显示
    #cv2.waitKey(5000)
    return result

def img_watershed(img):
    '''
    分水岭算法
    :param img: 
    :return: 
    '''
    # 现在我们用分水岭算法分离两个圆
    distance = ndi.distance_transform_edt(img)  # 距离变换
    local_maxi = feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
                                        labels=img)  # 寻找峰值
    markers = ndi.label(local_maxi)[0]  # 初始标记点
    labels = morphology.watershed(-distance, markers, mask=img)  # 基于距离变换的分水岭算法

    return labels

def img_skeleton(img):
    '''
    骨架提取算法
    个人感觉效果并不好，噪点无法很好的处理掉
    :param img:
    :return:
    '''
    retval, result = cv2.threshold(img, 100, 1, cv2.THRESH_BINARY)
    result = morphology.skeletonize(result)
    #retval, result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY)
    # 显示结果
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.axis('off')
    ax1.set_title('original', fontsize=20)

    ax2.imshow(result, cmap=plt.cm.gray)
    ax2.axis('off')
    ax2.set_title('skeleton', fontsize=20)

    fig.tight_layout()
    #plt.show()
    return result

def img_hist(img):
    '''
    增强对比度
    :param img: 
    :return: 
    '''
    # #2D卷积增强对比度
    # Mat kernel = (Mat_ < char > (3, 3) << 0, -1, 0,
    #           -1, 5, -1,
    #           0, -1, 0);
    # Mat dst;
    # img=filter2D(img, dst, img.depth(), kernel)
    return img

# 对数变换
def log(c, img):
    output = c * np.log(1.0 + img)
    output = np.uint8(output + 0.5)
    return output
#伽玛变换
def gamma(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output_img = cv2.LUT(img, lut) #像素灰度值的映射
    output_img = np.uint8(output_img+0.5)
    return output_img



if __name__ == '__main__':
    img1_path = 'D:/Data/all_test/007.bmp'
    #读取图片
    src = cv2.imread(img1_path, 0)

    # 去除背景处理
    src = img_process(src)

    #自适应二值化操作
    # res1=thre(src,'ADG')
    # img_showandwrite(src, img1_path, '001-1gass')
    # res2 = thre(src, 'ADM')
    # img_showandwrite(src, img1_path, '001-1mean')

    # # #3.4是可以作为选择的
    # # #开闭运算去除噪声
    # res1=img_mor(src, 4)
    # res1=thre(res1,'BI',adap_thre-20)
    ##打印自适应出来的阈值
    #print(adap_thre)

    # #增强对比度
    # res1 = img_hist(src)

    # #对数变换
    # res1 = log(42,src)
    #gamma变换
    res1 = gamma(src,0.005, 5.0)

    # #骨骼提取
    # res2 = img_skeleton(res1)
    # res2=imag_process(img1_path,res1)

    #分水岭算法
    #res1 = img_watershed(src)

    # #绘制直方图
    # plt.hist(src.ravel(), 256)
    # plt.show()

    #图片可视化
    cv2.imshow('water', res1)
    cv2.waitKey(5000)