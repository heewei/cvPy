import cv2
from primesense import openni2
from matplotlib import pyplot as plt
import numpy as np

openni2.initialize('C:\\Program Files\\OpenNI2\\Samples\\Bin\\')

dev = openni2.Device.open_any()
print('Hello')
print(dev.get_sensor_info(openni2.SENSOR_DEPTH))

depth_stream = dev.create_depth_stream()
#depth_stream.set_video_mode (openni2.c_api.OniVideoMode( pixelFormat = openni2.c_api.OniPixelFormat. ONI_PIXEL_FORMAT_DEPTH_1_MM , resolutionX = 640 , resolutionY = 480 , fps = 30 ))
depth_stream.start()

ir_stream = dev.create_ir_stream()
ir_stream.start()

shot_idx = 0
while True :
    frame = depth_stream.read_frame()
    frame_data = frame.get_buffer_as_uint16()
    depth_array = np.ndarray ((frame.height, frame.width), dtype = np.uint16, buffer = frame_data) / 10000. # 0 - 10000 mm to 0. - 1.
    cv2.imshow ( ' Depth ' , depth_array)
    ir_frame = ir_stream.read_frame()
    ir_frame_data = ir_frame.get_buffer_as_uint16()
    ir_array = np.ndarray ((ir_frame.height, ir_frame.width), dtype = np.uint16, buffer = ir_frame_data).astype(np.float32)
    cv2.imshow ( ' IR ' , ir_array / ir_array.max())


    ch = 0xFF & cv2.waitKey ( 1 )
    if ch == 27 :
        break
    if ch == ord ( ' ' ):
        fn = ' shot _ % 03 d . png ) ' % shot_idx
        cv2.imwrite (fn, (depth_array * 255 ).astype(np.uint8))
        print(fn, ' saved ')
        fn = ' ir_shot_ % 03 d . png ) ' % shot_idx
        cv2.imwrite (fn, (ir_array / ir_array.max() * 255 ).astype(np.uint8))
        print(fn, ' saved ')
        shot_idx += 1        
depth_stream.stop()
ir_stream.stop()
openni2.unload()
cv2.destroyAllWindows() 

'''
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()
depth_stream.stop()

depth_array = np.ndarray((frame.height,frame.width),dtype=np.uint16,buffer=frame_data) 
plt.imshow(depth_array)
plt.show()
'''
'''
color_stream = dev.create_color_stream()

video_mode = openni2.VideoMode()
video_mode.fps = 30
video_mode.resolutionX = 640
video_mode.resolutionY = 480
video_mode.pixelFormat = openni2.PIXEL_FORMAT_RGB888

color_stream.set_video_mode(video_mode)
color_stream.set_mirroring_enabled(False)

color_stream.start()
'''
openni2.unload()

'''
img = cv2.imread('B1Lancer.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('look', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''