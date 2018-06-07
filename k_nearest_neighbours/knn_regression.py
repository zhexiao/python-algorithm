"""
回归

使用KNN算法预测示例：
假设你在伯克利开个小小的面包店，现在需要根据如下一组特征预测当天该烤多少条面包：
（1）天气指数1～5（1表示天气很糟，5表示天气非常好）
（2）是不是周末或节假日（周末或节假日为1，否则为0）
（3）有没有活动（1表示有，0表示没有）

# 下面是 a ~ f 天的面包记录
# 前面的3个值分别为上述的特征值，最后一个值代表当天卖出了多少面包
history = {
    'a': (5, 1, 0, 300),
    'b': (3, 1, 1, 225),
    'c': (1, 1, 0, 75),
    'd': (4, 0, 1, 200),
    'e': (4, 0, 0, 150),
    'f': (2, 0, 0, 50)
}

现在我需要预期（今天是周末，天气不错）需要准备多少面包。
"""
from math import sqrt, pow

history = {
    'a': (5, 1, 0, 300),
    'b': (3, 1, 1, 225),
    'c': (1, 1, 0, 75),
    'd': (4, 0, 1, 200),
    'e': (4, 0, 0, 150),
    'f': (2, 0, 0, 50)
}

# 根据上面的描述，我们的特征值应该如下
today = (4, 1, 0, None)

# 首先用KNN算法获得最近的3个邻居
knn_dict = {}
for d, dt in history.items():
    val = sqrt(
        pow(dt[0] - today[0], 2) +
        pow(dt[1] - today[1], 2) +
        pow(dt[2] - today[2], 2)
    )
    knn_dict[d] = val

# 根据值排序
knn_dict = sorted(knn_dict.items(), key=lambda x: x[1])

# 使用回归预测，拿到最近的3个邻居的销售数平均值
predict_val = (
                  history[knn_dict[0][0]][3] +
                  history[knn_dict[1][0]][3] +
                  history[knn_dict[2][0]][3]
              ) / 3

print(knn_dict)
print(predict_val)