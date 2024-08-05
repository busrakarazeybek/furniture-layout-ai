import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def load_data(file_path):
    df = pd.read_csv(file_path)
    X = df.drop(columns=['sofa_x', 'sofa_y', 'table_x', 'table_y', 'chair_x', 'chair_y', 'bed_x', 'bed_y', 'desk_x', 'desk_y'])
    y = df[['sofa_x', 'sofa_y', 'table_x', 'table_y', 'chair_x', 'chair_y', 'bed_x', 'bed_y', 'desk_x', 'desk_y']]
    return X.values, y.values

def build_model(input_dim, output_dim):
    model = Sequential()
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(output_dim))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model(X, y):
    model = build_model(X.shape[1], y.shape[1])
    model.fit(X, y, epochs=100, batch_size=32, validation_split=0.2)
    model.save('models/furniture_model.h5')

if __name__ == "__main__":
    X, y = load_data('data/raw/training_data.csv')
    train_model(X, y)
