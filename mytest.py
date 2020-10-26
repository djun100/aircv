import aircv as ac

imsrc = ac.imread('tests/testdata/g18/screen_big.png')  # 原始图像
imsch = ac.imread('tests/testdata/g18/task.png')  # 带查找的部分
print((ac.find_sift(imsrc, imsch)))
