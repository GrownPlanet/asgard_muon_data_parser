import matplotlib.pyplot as plt
import numpy as np

# formatting
file = open("raw_data.txt", "r")
content = file.read().splitlines()

line = content.pop()
dat = [float(d) for d in line.split(" ")]
base_height = dat[7]
cur_height = 0

muon_count = [1]
height_interval = [0]

for line in content:
    dat = [float(d) for d in line.split(" ")]
    height = int(dat[7] / 100)
    if height != cur_height:
        muon_count.append(0)
        height_interval.append(int(height))
        cur_height = height
    muon_count[len(muon_count) - 1] += 1

height_interval = [f"{i*100}-{(i+1)*100}" for i in height_interval]
with open("out_100m.txt", "w") as file:
    for (i, v) in enumerate(muon_count):
        file.write(f"{height_interval[i]} {v}\n")

# matplotlib
muon_count.pop(0)
muon_count.pop(len(muon_count) - 1)

height_interval.pop(0)
height_interval.pop(len(height_interval) - 1)

x = np.arange(len(muon_count))
fig, ax = plt.subplots(layout="tight", figsize=(16,9))
ax.bar(x, muon_count, width=1)
ax.set_ylabel("muons counted")
ax.set_xlabel("height interval (m)")

nth = 50
ax.set_xticks(x[::nth])
ax.set_xticklabels([height_interval[i] for i in range(0, len(height_interval), nth)])

plt.savefig('muons.png', dpi=100)

plt.show()
