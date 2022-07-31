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

				# To improve performance, optionally mark the image as not writeable to
				# pass by reference.
				image.flags.writeable = False
				image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
				results = pose.process(image)
				if results.pose_landmarks is not None:
					skeleton = main.get_node(self, "Player").get_node("Skeleton2D")
					map = (
						(8, mp_pose.PoseLandmark.LEFT_SHOULDER),
						(9, mp_pose.PoseLandmark.LEFT_ELBOW),
						(10, mp_pose.PoseLandmark.LEFT_WRIST),
						(11, mp_pose.PoseLandmark.RIGHT_SHOULDER),
						(12, mp_pose.PoseLandmark.RIGHT_ELBOW),
						(13, mp_pose.PoseLandmark.RIGHT_WRIST)
					)
					for BONE_ID, BODY_PART in map:
						bone = skeleton.get_bone(BONE_ID)
						initial_pos = bone.get_skeleton_rest()
						body_part_pos = results.pose_landmarks.landmark[BODY_PART]
						transformation = initial_pos.translated(Vector2(body_part_pos.x/10000, body_part_pos.y/10000))
						print(BODY_PART, initial_pos, transformation)
						print(body_part_pos)
						bone.set_rest(transformation)
						bone.apply_rest()

		return False
