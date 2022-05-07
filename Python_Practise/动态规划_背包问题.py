class KnapsackProblem(object):
    def knapsack_problem(self):
        w = [1, 4, 3]  # 物品的重量
        val = [1500, 3000, 2000]  # 物品的价值 这里的val[i] 就是前面讲的v[i]
        m = 4  # 背包的容量
        n = len(val)  # 物品的个数
        # 创建二维数组
        # v[i][j] 表示在前个物品中能够装入的容量为j的背包中的最大值
        v = [[0 for col in range(m + 1)] for row in range(n + 1)]
        # 为了记录放入商品的情况,定义一个二维数组
        path = [[0 for col in range(m + 1)] for row in range(n + 1)]
        # 初始化第一行和第一列,这里本程中,可以不用去处理,因为默认就是0
        for i in range(len(v)):
            v[i][0] = 0  # 循环将第一列全部设置为0

        for j in range(len(v[0])):
            v[0][j] = 0  # 将第一行全部设置为0

        # 根据前面得到的公式来动态处理
        for i in range(1, len(v)):  # 不处理第一行,i是从1开始的
            for j in range(1, len(v[0])):  # 不处理第一列,j是从1开始的
                if w[i - 1] > j:  # 因为程序i 是从1开始的,因此公式中的w[i] 修改成w[i-1]
                    v[i][j] = v[i - 1][j]
                else:
                    # 因为 i 从1 开始,因此公式需要调整成:
                    # v[i][j] = max(v[i - 1][j], val[i - 1] + v[i - 1][j - w[i - 1]])
                    # 为了记录商品的存放到背包的情况,需要加判断
                    if v[i - 1][j] < val[i - 1] + v[i - 1][j - w[i - 1]]:
                        v[i][j] = val[i - 1] + v[i - 1][j - w[i - 1]]
                        # 把当前最优情况记录到path
                        path[i][j] = 1
                    else:
                        v[i][j] = v[i - 1][j]
        # 输出一下v 看下目前的情况
        for row in range(len(v)):
            for item in range(len(v[0])):
                print(v[row][item], end=" ")
            print()

        # 输出最后我们放入的那些商品
        path_row = len(path) - 1  # 行的最大下标
        path_col = len(path[0]) - 1  # 列的最大下标
        while path_row > 0 and path_col > 0:  # 从path的最后开始找
            if path[path_row][path_col] == 1:
                print('第%d个商品放入到背包' % path_row)
                path_col -= w[path_row - 1]
            path_row -= 1


if __name__ == '__main__':
    k = KnapsackProblem()
    k.knapsack_problem()

'''输出结果
0 0 0 0 0 
0 1500 1500 1500 1500 
0 1500 1500 1500 3000 
0 1500 1500 2000 3500 
第3个商品放入到背包
第1个商品放入到背包
'''
# ————————————————
# 版权声明：本文为CSDN博主「storyfull」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/storyfull/java/article/details/103876851
