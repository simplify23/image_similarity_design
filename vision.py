# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
from image_similarity_function import *
from img_aug import *
from main2 import *

str_img1 = "001"
str_img2 = "001-1"
folder = 'D:/Data/all_process'
img1_path1 =""
img1_path2 =""
img2_path2 =""
img2_path1 =""

# init
window = tk.Tk()
window.title('相似度算法')
window.geometry('620x420')
window.resizable(width=True, height=True)


# 按键布局
str1 = tk.Entry(window)
str2 = tk.Entry(window)
str1.grid(row=0,column=1)
str2.grid(row=1,column=1)
tk.Label(window, text='图片1名称').grid(row=0,column=0)
tk.Label(window, text='图片2名称').grid(row=1,column=0)


def read_img():
    global img1_path1
    global img2_path1
    str_img2 = str2.get()
    str_img1 = str1.get()
    img1_path1 = 'D:/Data/all_test/' + str_img1+ '.bmp'
    img2_path1 = 'D:/Data/all_test/' + str_img2 + '.bmp'

    #打开图片1
    img1 = Image.open(img1_path1)
    img1 = img1.resize((300, 300))
    photo1 = ImageTk.PhotoImage(img1)

    #打开图片2
    img2 = Image.open(img2_path1)
    img2 = img2.resize((300, 300))
    photo2 = ImageTk.PhotoImage(img2)

    #print(str_img1,str_img2)
    imglabel1['image']=photo1
    imglabel1.image=photo1
    imglabel2['image']=photo2
    imglabel2.image=photo2

def cal_img():
    img1_path2 = folder + '/' + str_img1 + 'p5.bmp'
    img2_path2 = folder + '/' + str_img2 + 'p5.bmp'
    #print(img1_path1)
    # 图像1处理
    img1 = cv2.imread(img1_path1, 0)
    img1 = img_process(img1)
    # img1 = thre(img1, 'BI', adap_thre - 20)
    # img1 = gamma(img1, 0.005, 5.0)
    # img1 = img_mor(img1, 4)
    # img1 = thre(img1, 'BI', 180)
    img_showandwrite(img1, folder, name='/' + str_img1)

    # 图像2处理
    img2 = cv2.imread(img2_path1, 0)
    img2 = img_process(img2)
    # img2 = gamma(img2, 0.005, 5.0)
    # img2 = img_mor(img2, 4)
    # img2 = thre(img2, 'BI', 150)
    img_showandwrite(img2, folder, name='/' + str_img2)

    kk = calc_image_similarity(img1_path2, img2_path2)
    if kk > 0:
        result.text = '两张图为同一骨骼，相似度为'+str(kk*100)+"%"
        result['text']='两张图为同一骨骼，相似度为'+str(kk*100)+"%"
    else:
        result.text = '两张为不同骨骼图'
        result['text'] = '两张为不同骨骼图'

def pro_img():
    pass

imglabel1 = tk.Label(window)
imglabel2 = tk.Label(window)
imglabel1.grid(row=3, column=0, columnspan=3)
imglabel2.grid(row=3, column=3, columnspan=3)
result = tk.Label(window)
result.grid(row=1,column=3)

read = tk.Button(window, text='读取', width=5, height=2, command=read_img)
cal = tk.Button(window, text='相似度计算', width=10, height=2, command=cal_img)
#pro = tk.Button(window, text='过程', width=5, height=2, command=pro_img)
read.grid(row=2,column=0)
cal.grid(row=2,column=1)
#pro.grid(row=2,column=2)




window.mainloop()

