import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def plot_graph(data, algorithm):
    frame_sizes = [entry[0] for entry in data]
    page_faults = [entry[1] for entry in data]
    fault_rates = [entry[2] for entry in data]
    hit_rates = [entry[3] for entry in data]

    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Bar graph
    ax[0].bar(frame_sizes, page_faults, color='skyblue', label='Page Faults')
    ax[0].set_xlabel('Frame size')
    ax[0].set_ylabel('Page Faults')
    ax[0].set_title(f'{algorithm} Page Faults vs Frame size')
    ax[0].legend()
    ax[0].set_ylim(0, 50)  # Set y-axis range

    # Line graph
    ax[1].plot(frame_sizes, fault_rates, marker='o', linestyle='-', color='orange', label='Fault Rate %')
    ax[1].plot(frame_sizes, hit_rates, marker='o', linestyle='-', color='green', label='Hit Rate %')
    ax[1].set_xlabel('Frame size')
    ax[1].set_ylabel('Rate %')
    ax[1].set_title(f'{algorithm} Fault Rate and Hit Rate vs Frame size')
    ax[1].legend()

    plt.tight_layout()
    plt.show()

def compare_fault_rates(fifo_data, opt_data, lru_data):
    frame_sizes = [entry[0] for entry in fifo_data]
    fifo_fault_rates = [entry[2] for entry in fifo_data]
    opt_fault_rates = [entry[2] for entry in opt_data]
    lru_fault_rates = [entry[2] for entry in lru_data]

    plt.plot(frame_sizes, fifo_fault_rates, marker='o', linestyle='-', color='blue', label='FIFO')
    plt.plot(frame_sizes, opt_fault_rates, marker='o', linestyle='-', color='green', label='OPT')
    plt.plot(frame_sizes, lru_fault_rates, marker='o', linestyle='-', color='red', label='LRU')

    plt.xlabel('Frame size')
    plt.ylabel('Fault Rate %')
    plt.title('Comparison of Fault Rates among Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

# Sample data
fifo_data1 = [
    (3, 22, 73.33, 26.67),
    (4, 22, 73.33, 26.67),
    (5, 18, 60, 40),
    (6, 16, 53.33, 46.67),
    (7, 11, 36.67, 63.33),
    (8, 11, 36.67, 63.33)
]

opt_data1 = [
    (3, 16, 53, 47.67),
    (4, 14, 46.67, 53.33),
    (5, 12, 40, 60),
    (6, 11, 36.67, 63.33),
    (7, 10, 33.33, 66.67),
    (8, 10, 33.33, 66.67)
]

lru_data1 = [
    (3, 22, 73.33, 26.67),
    (4, 22, 73.33, 26.67),
    (5, 18, 60, 40),
    (6, 15, 50, 50),
    (7, 14, 46.67, 53.33),
    (8, 14, 46.67, 53.33)
]

fifo_data2 = [
    (4, 29, 58, 42),
    (5, 25, 50, 50),
    (6, 22, 44, 56),
    (7, 22, 44, 56),
    (8, 15, 30, 70),
    (9, 10, 20, 80)
]

opt_data2 = [
    (4, 19, 38, 62),
    (5, 16, 32, 68),
    (6, 13, 26, 74),
    (7, 12, 24, 76),
    (8, 11, 22, 78),
    (9, 10, 20, 80)
]

lru_data2 = [
    (4, 28, 56, 44),
    (5, 25, 50, 50),
    (6, 21, 42, 58),
    (7, 17, 34, 66),
    (8, 13, 26, 74),
    (9, 12, 24, 76)
]

fifo_data3 = [
    (5, 53, 53, 47),
    (6, 43, 43, 57),
    (7, 36, 36, 64),
    (8, 32, 32, 68),
    (9, 21, 21, 79),
    (10, 10, 10, 90)
]

opt_data3 = [
    (5, 37, 37, 63),
    (6, 29, 29, 71),
    (7, 22, 22, 78),
    (8, 17, 17, 83),
    (9, 13, 13, 87),
    (10, 10, 10, 90)
]

lru_data3 = [
    (5, 57, 57, 43),
    (6, 47, 47, 53),
    (7, 39, 39, 61),
    (8, 32, 32, 68),
    (9, 24, 24, 76),
    (10, 10, 10, 90)
]


# Plot graphs
plot_graph(fifo_data3, 'FIFO')
plot_graph(opt_data3, 'OPT')
plot_graph(lru_data3, 'LRU')

compare_fault_rates(fifo_data3, opt_data3, lru_data3)
