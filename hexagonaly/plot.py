import math
import numpy as np
import matplotlib.collections as mcoll
import matplotlib.transforms as mtransforms
import matplotlib.pyplot as plt

C1 = 1.0 / math.sqrt(3.0)
C2 = C1 / 2.0
verts = [[0,C1], [0.5, C2], [0.5, -C2], [0, -C1], [-0.5, -C2], [-0.5, C2]]

u = np.array([1,0])
v = np.array([0.5, math.sqrt(3.0) / 2.0])

nx = 10
ny = 10
off = np.empty((nx*ny, 2))
# Optimize me
m = 0
for i in range(nx):
    for j in range(ny):
        off[m] = i * u + j *v 
        m += 1

fig = plt.figure()
axes = fig.add_subplot(111)
axes.set_xlim([-1, 10])
axes.set_ylim([-1, 10])

collection = mcoll.PolyCollection(
    verts=[verts],
    offsets=off,
    transOffset=mtransforms.IdentityTransform(),
    offset_position="data"
)

axes.add_collection(collection)
axes.autoscale_view()
plt.show()
