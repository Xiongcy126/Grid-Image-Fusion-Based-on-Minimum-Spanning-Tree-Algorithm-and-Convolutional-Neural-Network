# Subgragh-Fusion-Based-on-Minimum-Spanning-Tree-Algorithm-and-Convolutional-Neural-Network
本研究提出了一种基于最小生成树算法和卷积神经网络的栅格图像融合方法。该方法首先对子图图像数据进行尺度不变特征变换(Scale-invariant feature transform，SIFT)，
对特征点进行提取，基于克鲁斯卡尔(Kruskal)算法进行最小生成树构建，每次找到特征重合度最大的两张图像，
然后利用卷积神经网络将这些特征融合，得到最终的融合图像，并使用消融实验验证了最小生成树算法规划子图融合顺序对图像融合结果效果的提升。

使用vgg19获取图像的特征点，代码在Stitch_Net中。
规划子图融合顺序的最小生成树算法在min_tree_kruskal.py中，
EDGES中存储了report中图2.1中的子图间的特征点数量排序
RESULTS中为上述排序中，特征点对数量前三的子图对前三和对应的子图序号，即得出了子图匹配顺序。
stitcher中为子图拼接函数
main中使用out文件夹中的图像1 2 3 4，分别对应report中2.1（b）-2.1（e），运行时需要根据上一步得出的匹配顺序手动更改输入图像的序号完成图像拼接。
分步拼接结果保存为1+2  3+4 最终融合结果保存为1+2+3+4
链接为：https://github.com/Xiongcy126/Subgragh-Fusion-Based-on-Minimum-Spanning-Tree-Algorithm-and-Convolutional-Neural-Network.git
