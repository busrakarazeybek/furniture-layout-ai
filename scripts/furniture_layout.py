import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from scripts.plot_utils import plot_furniture_layout

def generate_furniture_layout_ai(room_length, room_width, num_furniture):
    model = tf.keras.models.load_model('models/furniture_model.h5')
    input_data = np.array([[room_length, room_width, num_furniture]])
    predictions = model.predict(input_data)
    return predictions[0]

if __name__ == "__main__":
    room_length = 10
    room_width = 8
    num_furniture = 5  # Number of furniture items

    layout = generate_furniture_layout_ai(room_length, room_width, num_furniture)
    plot_furniture_layout(room_length, room_width, layout)
