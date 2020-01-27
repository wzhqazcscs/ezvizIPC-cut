import cv2
from matplotlib import pyplot as plt

# 通过cv2中的类获取视频流操作对象cap
cap = cv2.VideoCapture('http://hls01open.ys7.com/openlive/xxxx.hd.m3u8')
# 调用cv2方法获取cap的视频帧
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# 获取cap视频流的每帧像素大小
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)

# 定义编码格式mpge-4
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
# 定义视频文件输入对象
outVideo = cv2.VideoWriter('saveDir.avi', fourcc, fps, size) #size必须和视频流的帧大小一致，否则无法执行

# 获取视频流打开状态
if cap.isOpened():
    rval, frame = cap.read()
    print('ture')
else:
    rval = False
    print('False')

tot = 1
c = 1
# 循环使用cv2的read()方法读取视频帧
while rval:
    rval, frame = cap.read()   #ret，frame=cap.read 这一行的“”ret，”是什么意思,cap.read()返回两个参数赋给两个值。第一个参数ret的值为True或False，代表有没有读到图片。第二个参数是frame，是当前截取一帧的图片。
    #cv2.imshow('test', frame)
    # 不注释则每间隔tot %  xx帧保存一张图像帧   保存照片到本地！！！
    if tot % 15 ==0 :
       cv2.imwrite('cut/'+'cut_'+str(c)+'.jpg',frame)
       c+=1
       print('c=', c)
    tot += 1
    print('tot=', tot)

    # 使用VideoWriter类中的write(frame)方法，将图像帧写入视频文件
    #outVideo.write(frame)
    # cv2.waitKey(25)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #   break
cap.release()
outVideo.release()
cv2.destroyAllWindows()