from godot import exposed, export
from godot import *
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

@exposed
class main(Node):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
	cap = cv2.VideoCapture(0)

	def _initialize(self):
		pass

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass

	def _finalize(self):
		self.cap.release()

	def _process(self, delta):
		with mp_pose.Pose(
			min_detection_confidence=0.5,
			min_tracking_confidence=0.5) as pose:
			if self.cap.isOpened():
				success, image = self.cap.read()
				if not success:
					print("Ignoring empty camera frame.")
					# If loading a video, use 'break' instead of 'continue'.
					return False
					#return True

				# To improve performance, optionally mark the image as not writeable to
				# pass by reference.
				image.flags.writeable = False
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#				print("working")
				results = pose.process(image)

				#print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE])
				#print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY])
				print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY])
				#print(results.pose_landmarks.get(14))

				## Draw the pose annotation on the image.
				#image.flags.writeable = True
				#image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
				#mp_drawing.draw_landmarks(
				#	image,
				#	results.pose_landmarks,
				#	mp_pose.POSE_CONNECTIONS,
				#	landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
				## Flip the image horizontally for a selfie-view display.
				#cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
				#if cv2.waitKey(5) & 0xFF == 27:
				#	return
		return False
		 
