import numpy as np
import pandas as pd

def generate_training_data(num_samples, room_length, room_width):
    data = []
    for _ in range(num_samples):
        sofa_x = np.random.uniform(0, room_length - 2)
        sofa_y = np.random.uniform(0, room_width - 1)
        table_x = np.random.uniform(0, room_length - 1.5)
        table_y = np.random.uniform(0, room_width - 1.5)
        chair_x = np.random.uniform(0, room_length - 1)
        chair_y = np.random.uniform(0, room_width - 1)
        bed_x = np.random.uniform(0, room_length - 3)
        bed_y = np.random.uniform(0, room_width - 2)
        desk_x = np.random.uniform(0, room_length - 2)
        desk_y = np.random.uniform(0, room_width - 1)
        
        data.append([sofa_x, sofa_y, table_x, table_y, chair_x, chair_y, bed_x, bed_y, desk_x, desk_y])
    
    columns = ['sofa_x', 'sofa_y', 'table_x', 'table_y', 'chair_x', 'chair_y', 'bed_x', 'bed_y', 'desk_x', 'desk_y']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('data/raw/training_data.csv', index=False)

if __name__ == "__main__":
    generate_training_data(1000, 10, 8)
