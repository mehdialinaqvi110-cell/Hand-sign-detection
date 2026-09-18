'''import cv2
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def draw_text(frame, text):

    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    return frame


def draw_landmarks(frame, hand_landmarks):

    for hand in hand_landmarks:

        hand_proto = landmark_pb2.NormalizedLandmarkList()

        hand_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(
                x=lm.x,
                y=lm.y,
                z=lm.z
            )
            for lm in hand
        ])

        mp_draw.draw_landmarks(
            frame,
            hand_proto,
            mp_hands.HAND_CONNECTIONS
        )

    return frame'''

# backend/drawing_utils.py

'''import cv2
import mediapipe as mp

# Hand connections for drawing the skeleton
mp_hands = mp.solutions.hands


def draw_text(frame, text):
    """
    Draw recognized sign text on the frame.
    """

    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    return frame


def draw_landmarks(frame, hand_landmarks):
    """
    Draw hand landmarks and connections on the frame.

    Args:
        frame: OpenCV image (BGR).
        hand_landmarks: results.hand_landmarks from MediaPipe Tasks API.
    """

    h, w, _ = frame.shape

    for hand in hand_landmarks:

        points = []

        # Draw landmark points
        for lm in hand:

            x = int(lm.x * w)
            y = int(lm.y * h)

            points.append((x, y))

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )

        # Draw hand skeleton connections
        for start_idx, end_idx in mp_hands.HAND_CONNECTIONS:

            cv2.line(
                frame,
                points[start_idx],
                points[end_idx],
                (255, 0, 0),
                2
            )

    return frame'''

# backend/drawing_utils.py

import cv2


# Hand connections (21 landmarks)
HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]


def draw_text(frame, text):

    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    return frame


def draw_landmarks(frame, hand_landmarks):

    h, w, _ = frame.shape

    for hand in hand_landmarks:

        points = []

        # Draw landmark points
        for lm in hand:

            x = int(lm.x * w)
            y = int(lm.y * h)

            points.append((x, y))

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )

        # Draw connections
        for start, end in HAND_CONNECTIONS:

            cv2.line(
                frame,
                points[start],
                points[end],
                (255, 0, 0),
                2
            )

    return frame