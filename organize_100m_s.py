import matplotlib.pyplot as plt
import numpy as np

# formatting
file = open("raw_data.txt", "r")
content = file.read().splitlines()

line = content.pop()
dat = [float(d) for d in line.split(" ")]
# base_height = dat[7]
cur_height = 0
startime = -1 # erros will be more vissible
endtime = -1

muon_count = [1]
delta_t = []
height_interval = [0]

for line in content:
    dat = [float(d) for d in line.split(" ")]
    height = int(dat[7] / 100)
    if height != cur_height:
        endtime = dat[1]
        if endtime != startime:
            muon_count[len(muon_count) - 1] /= (endtime - startime) / 100
            delta_t.append((endtime - startime) / 100)
        startime = dat[1]
        muon_count.append(0)
        height_interval.append(int(height))
        cur_height = height
    muon_count[len(muon_count) - 1] += 1

height_interval = [f"{i*100}-{(i+1)*100}" for i in height_interval]
with open("out_100m_s.txt", "w") as file:
    for (i, v) in enumerate(muon_count):
        file.write(f"{height_interval[i]} {v}\n")

# matplotlib
muon_count.pop(0)
muon_count.pop(len(muon_count) - 1)

height_interval.pop(0)
height_interval.pop(len(height_interval) - 1)

delta_t.pop(0)
delta_t.pop(len(delta_t) - 1)

x = np.arange(len(muon_count))
fig, ax = plt.subplots(layout="tight", figsize=(16,9))
ax.bar(x, muon_count, width=1)
ax.set_ylabel("muons counted/second")
ax.set_xlabel("height interval (m)")

ax2 = ax.twinx()
ax2.plot(delta_t, 'r')
ax2.set_ylabel("time interval")

nth = 50
ax.set_xticks(x[::nth])
ax.set_xticklabels([height_interval[i] for i in range(0, len(height_interval), nth)])

plt.savefig('muons.png', dpi=100)

plt.show()
