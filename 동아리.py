import cv2
import tensorflow as tf
import numpy as np
from tensorflow.python.keras.models import load_model

# Custom Layer 정의
class MyBatchNormalization(tf.keras.layers.Layer):
    def __init__(self, units, **kwargs):
        super(MyBatchNormalization, self).__init__(**kwargs)
        self.units = units
        self.batch_norm = tf.keras.layers.BatchNormalization()

    def call(self, inputs, training=None, **kwargs):
        normalized_output = self.batch_norm(inputs, training=training)
        return normalized_output

# 모델 로드
model_path = "C:/Users/cmt06/OneDrive/converted_keras/keras_model.h5"
custom_objects = {'MyBatchNormalization': MyBatchNormalization}
image_classification_model = load_model(model_path, compile=False, custom_objects=custom_objects)

# 클래스 레이블 정의
class_labels = ["car crush", "normal"]  # 실제 모델이 예측하는 클래스에 맞게 수정

# 동영상 파일 경로 설정
video_path = "C:/Users/cmt06/OneDrive/converted_keras/강화 교통사고 동영상.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임 크기 조절 (선택적)
    frame = cv2.resize(frame, (640, 480))

    # 이미지 전처리
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # 이미지 분류
    predictions = image_classification_model.predict(img)
    predicted_class_index = np.argmax(predictions)
    predicted_class_label = class_labels[predicted_class_index]

    # 프레임에 클래스 정보 표시
    cv2.putText(frame, f"Class: {predicted_class_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 동영상에 이미지 그리기
    cv2.imshow("Real-time Video Classification", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
