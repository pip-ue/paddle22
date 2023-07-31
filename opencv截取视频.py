import cv2 as cv
import os.path

# 1.存储图片文件夹
path = 'F:/VideoToImage'  # 存放视频图片的主目录
if not os.path.exists(path):  # 如果不存在就创建文件夹
    os.mkdir(path)

# 2.读取视频文件夹
filepath = 'F:/video'  # 需要读取的视频的路径
pathDir = os.listdir(filepath)  # 获取文件夹中文件名称

# 3.截视频帧数
for allDir in pathDir:  # 逐个读取视频文件
    a = 1  # 图片计数-不改
    c = 1  # 帧数计数-不改
    videopath = r'F:/video/' + allDir  # 视频文件路径
    vc = cv.VideoCapture(videopath)  # 读入视频文件
    # 存储视频的子目录
    path = 'F:/VideoToImage/' + allDir.split('.')[0]
    if not os.path.exists(path):  # 如果不存在就创建文件夹
        os.mkdir(path)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    timeF = 4  # 帧数间隔
    while rval:
        rval, frame = vc.read()  # 分帧读取视频
        if rval == False:
            break
        if (c % timeF == 0):
            cv.imwrite(path + '/' + str(a) + '.jpg', frame)  # 保存路径
            a = a + 1
        c = c + 1
        cv.waitKey(1)
    vc.release()
