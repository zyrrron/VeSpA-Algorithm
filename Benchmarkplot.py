import matplotlib.pyplot as plt
import numpy as np
benchmarks = ['x<=40', '40<x<=100', '100<x<=500', 'x>500', 'lrb1', 'lrb2', 'lrb3', 'lrb4', 'lrb5']
parameters = ['Number of Benchmarks', 'Avg. Node Number', 'Avg. Edge Number', 'Avg. Complexity', 'Avg. Constraint per Benchmark',
              'Avg. User Requirement per Benchmark']

# set width of bar
barWidth = 0.1
fig = plt.subplots(figsize=(20, 15))

# set height of bar
b1 = [200, 200, 200, 200, 5, 5, 5, 5, 10]
b2 = [11.24, 21.64, 75.16, 209.24, 47, 32, 62, 154, 162]
b3 = [12.07, 25.54, 62.97, 232.04, 42, 23, 48, 197, 213]
b4 = [34.55, 68.82, 213.29, 650.52, 136, 87, 172, 505, 537]
b5 = [2.12, 4.39, 12.24, 13.96, 13.20, 3.80, 10.80, 14.80, 12.90]
b6 = [1, 1, 1, 1, 1, 1, 1, 1, 1.1]
b = [b1, b2, b3, b4, b5, b6]
# Set position of bar on X axis
c = np.arange(len(b1))
color = ['#f1d77e', '#b1ce46', '#63e398', '#9394e7', '#f27970', '#beb8dc']
for i in range(len(color)):
        # Make the plot
        plt.subplot(3, 2, i+1)
        plt.bar(c, b[i], color=color[i], width=barWidth,
                edgecolor='grey', label=parameters[i])
        plt.xlabel(f"{parameters[i]}, x = 'Complexity'", fontweight='bold', fontsize=15)
        plt.ylabel('Value', fontweight='bold', fontsize=20)
        plt.xticks([r + barWidth for r in range(len(b1))], benchmarks)
        # plt.xticks(range(len(b1)), benchmarks)
        plt.legend()
        # outputpath = f"TestCaseFiles/BenchmarkDescriptionP{i+1}.png"
outputpath = f"TestCaseFiles/BenchmarkDescription.png"
plt.savefig(outputpath)
plt.clf()

