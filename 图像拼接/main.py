import numpy as np
from Stitcher import Stitcher
import cv2
from tqdm import *

# city = ['bellingham', 'bloomington', 'innsbruck', 'sfo', 'tyrol-e']
# # city = ['bloomington', 'innsbruck', 'sfo', 'tyrol-e']
#
# for c in range(len(city)):
#     img = []
#     for i in range(1, 37):
#         img.append(cv2.imread('AerialImageDataset/test/trans_jpg/' + city[c] + str(i) + '.jpg'))
#     edge = []
#     for i in trange(len(img)):
#         for j in range(len(img)):
#             if i != j:
#                 # 图片拼接
#                 stitcher = Stitcher()
#                 if stitcher.stitch([img[i], img[j]], showMatches=True) != None:
#                     # print(i+1, j+1, len(stitcher.stitch([img[i], img[j]], showMatches=True)[0]))
#                     edge.append([len(stitcher.stitch([img[i], img[j]], showMatches=True)[0]), i+1, j+1])
#     np.savetxt('EDGES/' + city[c] + '.txt', np.array(edge, dtype=int), fmt='%d')



img = []
for i in range(1, 5):
    img.append(cv2.imread('out/' + str(i) + '.jpg'))
edge = []
for i in range(len(img)):
    for j in range(len(img)):
        if i != j:
            # 图片拼接
            stitcher = Stitcher()
            if stitcher.stitch([img[i], img[j]], showMatches=True) != None:
                print(i+1, j+1, len(stitcher.stitch([img[i], img[j]], showMatches=True)[0]))
                edge.append([len(stitcher.stitch([img[i], img[j]], showMatches=True)[0]), i + 1, j + 1])
edge = sorted(edge, key=lambda x: x[0], reverse=True)
np.savetxt('EDGES/sort_weight.txt', np.array(edge, dtype=int), fmt='%d')

