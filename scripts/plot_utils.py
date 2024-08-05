import matplotlib.pyplot as plt

def plot_furniture_layout(room_length, room_width, furniture_layout):
    fig, ax = plt.subplots()
    ax.set_xlim(0, room_length)
    ax.set_ylim(0, room_width)
    
    furniture_types = ['Sofa', 'Table', 'Chair', 'Bed', 'Desk']
    for i in range(len(furniture_types)):
        x, y = furniture_layout[2*i], furniture_layout[2*i+1]
        rect = plt.Rectangle((x, y), 1, 1, fill=True, edgecolor='black', linewidth=1.5, label=furniture_types[i])
        ax.add_patch(rect)
        plt.text(x + 0.5, y + 0.5, furniture_types[i], ha='center', va='center', fontsize=10, color='white')
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('AI-Generated Furniture Layout')
    plt.xlabel('Length (m)')
    plt.ylabel('Width (m)')
    plt.grid(True)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.show()
