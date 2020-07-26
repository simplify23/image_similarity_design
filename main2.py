# -*- encoding=utf-8 -*-

from image_similarity_function import *
from img_aug import *
import os
import shutil

# 融合相似度阈值
threshold1 = 0.74
# 最终相似度较高判断阈值
threshold2 = 0.74


# 融合函数计算图片相似度
def calc_image_similarity(img1_path2, img2_path2):
    """
    :param img1_path: filepath+filename
    :param img2_path: filepath+filename
    :return: 图片最终相似度
    """

    #similary_ORB = float(ORB_img_similarity(img1_path2, img2_path2))
    similary_phash = float(phash_img_similarity(img1_path2, img2_path2))
    #similary_hist = float(calc_similar_by_path(img1_path2, img2_path2))
    # 如果三种算法的相似度最大的那个大于0.85，则相似度取最大，否则，取最小。
    # max_three_similarity = max(similary_ORB, similary_phash, similary_hist)
    # min_three_similarity = min(similary_ORB, similary_phash, similary_hist)
    if similary_phash > threshold1:
        result = similary_phash
    else:
        result = 0

    return round(result, 3)


if __name__ == '__main__':

    # 搜索图片路径和文件名
    folder = 'D:/Data/process'
    str1 = '004'
    str2 = '005'
    img1_path = 'D:/Data/test/'+str1+'.bmp'
    img2_path = 'D:/Data/test/'+str2+'.bmp'
    img1_path2 = 'D:/Data/process/'+str1+'p2.bmp'
    img2_path2 = 'D:/Data/process/'+str2+'p2.bmp'

    #图像1的处理过程
    img1 = cv2.imread(img1_path, 0)
    img1=img_process(img1)
    # img1 = img_mor(img1, 4)
    # img1 = thre(img1, 'BI', adap_thre - 20)
    img_showandwrite(img1,folder,name='/'+str1)

    #图象2的处理过程
    img2 = cv2.imread(img2_path, 0)
    img2 = img_process(img2)
    # res2 = img_mor(img2, 4)
    # res2 = thre(res1, 'BI', adap_thre - 20)
    img_showandwrite(img2, folder, name='/' + str2)
    #
    # # 搜索文件夹
    # filepath = 'D:/img_spam/data/train/unqrcode/'
    #
    # # 相似图片存放路径
    # newfilepath = 'F:/img_spam/4/第九组/'
    #
    # for parent, dirnames, filenames in os.walk(filepath):
    #     for filename in filenames:
    #         # print(filepath+filename)
    #         img2_path = filepath + filename

    kk = calc_image_similarity(img1_path2, img2_path2)

    # try:
    #     if kk >= threshold2:
    #         print(img2_path, kk)
    #         shutil.copy(img2_path, newfilepath)
    # except Exception as e:
    #             # print(e)
    #   pass
