import numpy as np


# 以全局变量X定义节点集合，即类似{'A':'A','B':'B','C':'C','D':'D'},如果A、B两点连通，则会更改为{'A':'B','B':'B",...},即任何两点连通之后，两点的值value将相同。
X = dict()
R = dict()   # 各点的初始等级均为0,如果被做为连接的的末端，则增加1


def make_set(point):
    X[point] = point
    R[point] = 0


def find(point):
    if X[point] != point:
        X[point] = find(X[point])
    return X[point]


def merge(point1, point2):
    '''连接两个分量（节点）
    '''
    r1 = find(point1)
    r2 = find(point2)
    if r1 != r2:
        if R[r1] > R[r2]:
            X[r2] = r1
        else:
            X[r1] = r2
            if R[r1] == R[r2]:
                R[r2] += 1


def kruskal(vertices, edges):
    # '''KRUSKAL算法实现
    # '''
    for vertice in vertices:
        make_set(vertice)
    minu_tree = []
    # edges = np.array(edges)
    edges = sorted(edges, key=lambda x: x[0], reverse=False)
    for j in range(len(edges)):
        edges[j] = edges[j].tolist()

    # edges.sort()  # 按照权重从小到大排序
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            merge(vertice1, vertice2)
            minu_tree.append(edge)
    return minu_tree


edges = np.loadtxt('EDGES/sort_weight.txt')
max_weight = np.max(edges[:, 0])
for i in range(edges.shape[0]):
    edges[i, 0] = max_weight - edges[i, 0]
vertices = list(range(1, 37))
min_tree = kruskal(vertices, edges)
nodes = []
for i in range(len(min_tree)):
    nodes.append(min_tree[i][1])
    nodes.append(min_tree[i][2])

total_weight = 0
for i in range(len(min_tree)):
    min_tree[i][0] = max_weight - min_tree[i][0]
    total_weight += min_tree[i][0]

np.savetxt('RESULT/_kruskal_' + str(total_weight) + '.txt', min_tree, fmt='%d')  # 结果中每行是一个三元组，表示[weight, node1, node2]


