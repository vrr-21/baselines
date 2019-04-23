import cv2

def store_video(frame_list, vid_name):
    writer = cv2.VideoWriter("videos/"+vid_name, cv2.VideoWriter_fourcc(*"MJPG"), 10, (320,240), True)
    for frame in frame_list:
        bgr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        writer.write(bgr_frame)
    writer.release()