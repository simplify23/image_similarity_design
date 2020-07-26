**算起来有段时间没写博客了，最近在整夏令营的事，随着夏令营告一段落，后面也需要给自己多多充电，顺便把浙大软院我做的项目放上来。代码放github上**

## 项目要求
1. 设计一个算法比较2张图片的计算相似度，在文档例子里面都是一对对的相识图片
2. 相识度设计为（0-1）， 给出2张图片是相识的，相识度取向1。否者取向0；
3. 可以开发有界面的，也可以是命令行。

代码一共分为4个文件，和一个主函数
-  img_aug.py: 图像增强（包含二值化，图像的膨胀腐蚀，开闭运算，骨骼提取等）
- image_similarity.py : 相似度算法（包含ORB，phash，直方图对比等）
- test.py : 所有数据的精度测试
- vision.py : 可视化界面
- main.py : 主函数

其中除相似度算法外，基本自己手撸，大部分注掉的代码都是过程中进行的尝试。


## 实验效果
项目演示ppt放在文档类里面，其中测试用例日志为我当时日常测试出来的数据。
#### 这个是当时给出的检测精度。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200726153459598.png)

##### 可视化的界面如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/202007261535595.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MzA3MDA1,size_16,color_FFFFFF,t_70)
可以进行图片的读取，并给出判定结果。

#### 各种目前现有的方法对比
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200726153638405.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM1MzA3MDA1,size_16,color_FFFFFF,t_70)
可以看出我的方法趋于稳定并获得良好的检测精确度。




## 我的方法介绍
1.中值滤波去除噪点
2.膨胀腐蚀

3.自适应二值化
（低值移除，自适应阈值二值化）
求均值

4.phash相似度比较

大体为这4个步骤。
