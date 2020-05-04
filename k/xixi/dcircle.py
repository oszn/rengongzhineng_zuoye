from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# # ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
# cir1 = Circle(xy = (0.0, 0.0), radius=2, fill=False)
# cir2 = Circle(xy = (0.0, 0.0), radius=3, fill=False)

def draw_circle(cow1,cow2,row1,row2,r):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    di = []
    for i in range(cow1,cow2,r):
        for j in range(row1,row2):
            di.append([i*r*2,j*r*2])
            cir=Circle(xy=(i*r*2,j*r*2),radius=r,fill=False)
            ax.add_patch(cir)

    x, y = 0, 0
    ax.plot(x, y, 'ro')

    plt.axis('scaled')
    # ax.set_xlim(-4, 4)
    # ax.set_ylim(-4, 4)
    plt.axis('equal')  # changes limits of x or y axis so that equal increments of x and y have the same length

    plt.show()
draw_circle(-10,10,-10,10,1);
# for i in range(0,9,1):
#     for j in range(0,9,1):
#         di.append([i+1,])
# ax.add_patch(cir1)
# ax.add_patch(cir2)
