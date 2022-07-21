import cv2

#Video capture Instance
cap =cv2.VideoCapture('sample.mp4')

#Properties of the video#

#Total npo. of frames
frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)

#FPS, HEight, Width of the video
fps =cap.get(cv2.CAP_PROP_FPS)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#Initialising output writer for video
fourcc =cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('reversed.avi',fourcc,fps,(int(width*0.5),int(height*0.5)))
print("No. of frames are : {}".format(frames))
print("FPS is : {}".format(fps))

#Now we get the index of the last frame
frame_index= frames-1

#Checking if the video instance is ready
if(cap.isOpened()):
	#reading till the end of the video
	while(frame_index>=0):

		#we set the current index to last frame
		cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
		ret,frame =cap.read()

		#Resize the frame
		frame=cv2.resize(frame,(int(width*0.5),int(height*0.5)))

		#OPtional: to show the reversing video
		#cv2.imshow('Reverse video',frame)

		#Writing the reverse video
		out.write(frame)

		#decrementing frame index at each step
		frame_index=frame_index-1

		#Printing the progress
		if(frame_index%100==0):
			print(frame_index)
		#if(cv2.waitKey(2)==ord('q')):
			#break

out.release()
cap.release()
cv2.destroyAllWindows()




