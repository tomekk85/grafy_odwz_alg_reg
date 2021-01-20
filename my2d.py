import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import collections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
import numpy as np
from mpl_toolkits.mplot3d import proj3d

#klasa do rysowania wektorów ("strzałek")
class myArrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)





#dane wejściowe

#2D

vert4x4 = [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 1], [2, 2], [3, 3], [4, 4]

conn4x4 = [1, 2], [1, 8], [2, 3], [2, 4], [3, 5], [4, 5], [4, 9], [5, 6], [6, 10], [7, 1], [8, 4], [9, 6]

vert5x5 = [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [1, 1], [2, 2], [3, 3], \
         [4, 4], [5, 5]

conn5x5 = [1, 2], [1, 12], [2, 3], [2, 5], [3, 4], [3, 6], [4, 7], [5, 6], [5, 13], [6, 7], [6, 8], [7, 9], [8, 9], \
          [8, 14], [9, 10], [10, 15], [11, 1], [12, 5], [13, 8], [14, 10]

vert6x6 = [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6], [4, 5], \
          [4, 6], [5, 6], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]
conn6x6 = [1, 2], [1, 17], [2, 3], [2, 6], [3, 4], [3, 7], [4, 5], [4, 8], [5, 9], [6, 7], [6, 18], [7, 8], [7, 10], \
          [8, 9], [8, 11], [9, 12], [10, 11], [10, 19], [11, 12], [11, 13], [12, 14], [13, 14], [13, 20], [14, 15], \
          [15, 21], [16, 1], [17, 6], [18, 10], [19, 13], [20, 15]

vert8x8 = [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [4, 5], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8], [6, 7], [6, 8], [7, 8], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]
conn8x8 = [1, 2], [1, 30], [2, 3], [2, 8], [3, 4], [3, 9], [4, 5], [4, 10], [5, 6], [5, 11], [6, 7], [6, 12], [7, 13], [8, 9], [8, 31], [9, 10], [9, 14], [10, 11], [10, 15], [11, 12], [11, 16], [12, 13], [12, 17], [13, 18], [14, 15], [14, 32], [15, 16], [15, 19], [16, 17], [16, 20], [17, 18], [17, 21], [18, 22], [19, 20], [19, 33], [20, 21], [20, 23], [21, 22], [21, 24], [22, 25], [23, 24], [23, 34], [24, 25], [24, 26], [25, 27], [26, 27], [26, 35], [27, 28], [28, 36], [29, 1], [30, 8], [31, 14], [32, 19], [33, 23], [34, 26], [35, 28]

vert10x10 = [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [6, 7], [6, 8], [6, 9], [6, 10], [7, 8], [7, 9], [7, 10], [8, 9], [8, 10], [9, 10], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]
conn10x10 = [1, 2], [1, 47], [2, 3], [2, 10], [3, 4], [3, 11], [4, 5], [4, 12], [5, 6], [5, 13], [6, 7], [6, 14], [7, 8], [7, 15], [8, 9], [8, 16], [9, 17], [10, 11], [10, 48], [11, 12], [11, 18], [12, 13], [12, 19], [13, 14], [13, 20], [14, 15], [14, 21], [15, 16], [15, 22], [16, 17], [16, 23], [17, 24], [18, 19], [18, 49], [19, 20], [19, 25], [20, 21], [20, 26], [21, 22], [21, 27], [22, 23], [22, 28], [23, 24], [23, 29], [24, 30], [25, 26], [25, 50], [26, 27], [26, 31], [27, 28], [27, 32], [28, 29], [28, 33], [29, 30], [29, 34], [30, 35], [31, 32], [31, 51], [32, 33], [32, 36], [33, 34], [33, 37], [34, 35], [34, 38], [35, 39], [36, 37], [36, 52], [37, 38], [37, 40], [38, 39], [38, 41], [39, 42], [40, 41], [40, 53], [41, 42], [41, 43], [42, 44], [43, 44], [43, 54], [44, 45], [45, 55], [46, 1], [47, 10], [48, 18], [49, 25], [50, 31], [51, 36], [52, 40], [53, 43], [54, 45]

vert15x15 = [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [1, 15], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [2, 15], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [4, 15], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [6, 15], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [8, 15], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [9, 15], [10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [11, 12], [11, 13], [11, 14], [11, 15], [12, 13], [12, 14], [12, 15], [13, 14], [13, 15], [14, 15], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15]
conn15x15 = [1, 2], [1, 107], [2, 3], [2, 15], [3, 4], [3, 16], [4, 5], [4, 17], [5, 6], [5, 18], [6, 7], [6, 19], [7, 8], [7, 20], [8, 9], [8, 21], [9, 10], [9, 22], [10, 11], [10, 23], [11, 12], [11, 24], [12, 13], [12, 25], [13, 14], [13, 26], [14, 27], [15, 16], [15, 108], [16, 17], [16, 28], [17, 18], [17, 29], [18, 19], [18, 30], [19, 20], [19, 31], [20, 21], [20, 32], [21, 22], [21, 33], [22, 23], [22, 34], [23, 24], [23, 35], [24, 25], [24, 36], [25, 26], [25, 37], [26, 27], [26, 38], [27, 39], [28, 29], [28, 109], [29, 30], [29, 40], [30, 31], [30, 41], [31, 32], [31, 42], [32, 33], [32, 43], [33, 34], [33, 44], [34, 35], [34, 45], [35, 36], [35, 46], [36, 37], [36, 47], [37, 38], [37, 48], [38, 39], [38, 49], [39, 50], [40, 41], [40, 110], [41, 42], [41, 51], [42, 43], [42, 52], [43, 44], [43, 53], [44, 45], [44, 54], [45, 46], [45, 55], [46, 47], [46, 56], [47, 48], [47, 57], [48, 49], [48, 58], [49, 50], [49, 59], [50, 60], [51, 52], [51, 111], [52, 53], [52, 61], [53, 54], [53, 62], [54, 55], [54, 63], [55, 56], [55, 64], [56, 57], [56, 65], [57, 58], [57, 66], [58, 59], [58, 67], [59, 60], [59, 68], [60, 69], [61, 62], [61, 112], [62, 63], [62, 70], [63, 64], [63, 71], [64, 65], [64, 72], [65, 66], [65, 73], [66, 67], [66, 74], [67, 68], [67, 75], [68, 69], [68, 76], [69, 77], [70, 71], [70, 113], [71, 72], [71, 78], [72, 73], [72, 79], [73, 74], [73, 80], [74, 75], [74, 81], [75, 76], [75, 82], [76, 77], [76, 83], [77, 84], [78, 79], [78, 114], [79, 80], [79, 85], [80, 81], [80, 86], [81, 82], [81, 87], [82, 83], [82, 88], [83, 84], [83, 89], [84, 90], [85, 86], [85, 115], [86, 87], [86, 91], [87, 88], [87, 92], [88, 89], [88, 93], [89, 90], [89, 94], [90, 95], [91, 92], [91, 116], [92, 93], [92, 96], [93, 94], [93, 97], [94, 95], [94, 98], [95, 99], [96, 97], [96, 117], [97, 98], [97, 100], [98, 99], [98, 101], [99, 102], [100, 101], [100, 118], [101, 102], [101, 103], [102, 104], [103, 104], [103, 119], [104, 105], [105, 120], [106, 1], [107, 15], [108, 28], [109, 40], [110, 51], [111, 61], [112, 70], [113, 78], [114, 85], [115, 91], [116, 96], [117, 100], [118, 103], [119, 105]

# lista ep, będzie przekazywana do funkcji jeżeli nie podamy "swojej" jako argument
ep_dict = collections.OrderedDict([(-4, [[5, 6, np.array([1, 5])]]),
                                         (-3, [[4, 5, np.array([1, 4])], [9, 7, np.array([2, 5])]]),
                                         (-2, [[3, 4, np.array([1, 3])], [8, 6, np.array([2, 4])], [12, 8, np.array([3, 5])]]),
                                         (-1, [[2, 3, np.array([1, 2])], [7, 5, np.array([2, 3])], [11, 7, np.array([3, 4])], [14, 9, np.array([4, 5])]]),
                                         (0, [[1, 2, np.array([1, 1])], [6, 4, np.array([2, 2])], [10, 6, np.array([3, 3])], [13, 8, np.array([4, 4])], [15, 10, np.array([5, 5])]])])



class Subplot:

    def draw(self, dim, ep_dictionary=ep_dict, napis=''):



        # lista współrzednych początku i końca linii dla Ep
        eps =[[] for i in range(len(ep_dictionary))]
            #range(len(dict_ep_))


        count = 0
        for key in ep_dictionary:
            arr = ep_dictionary.get(key)
            #print(arr)
            for i in range(0, len(arr)):
                #print(arr[i][2])
                if i == 0:
                    eps[count].append(arr[i][2])
                if i == len(arr) - 1:
                    eps[count].append(arr[i][2])
            count += 1


        #matplotlib inlie
        plt.rcParams['figure.figsize'] =(8, 6)
        plt.rcParams['figure.dpi'] = 120

        #Make Axes3D
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #tytuł wykresu
        ax.set_title('Metoda podstawienia dla macierzy o n=' + str(dim[0]) + '\nElementy przetwarzające ' + napis)
        #ax.set_title('Metoda podstawienia \nGraf zależności dla n = 6')
        #ustawienie "kroku" na układzie współrzędnych
        loc = plticker.MultipleLocator(base=1.0)
        ax.xaxis.set_major_locator(loc)
        ax.yaxis.set_major_locator(loc)
        ax.zaxis.set_major_locator(loc)

        #ustawienie etykiet na osiach
        ax.set_xlabel('$W1$', fontsize=25)
        ax.set_ylabel('$W2$', fontsize=25)
        ax.set_zlabel('', fontsize=25, rotation=60)

        #ax.plot_wireframe(2.1945, 2.8355, 1.2287, rstride=5, cstride=5)

        #pozycja "kamery"
        elev = 62.0
        azim = -90.0
        ax.view_init(elev, azim)

        #lista wierzchołków
        dictionary = {'4x4': [vert4x4, conn4x4],'5x5': [vert5x5, conn5x5] ,'6x6': [vert6x6, conn6x6],
                      '8x8': [vert8x8, conn8x8], '10x10': [vert10x10, conn10x10],
                      '15x15':[vert15x15, conn15x15]}

        Vertices = dictionary[dim][0]
        # lista połączeń
        Connections = dictionary[dim][1]

        #definicje list zawierających współrzędnie wierzchołków dla poszczególnych osi
        X = []
        Y = []
        Z = []
        bX = []
        bY = []
        bZ = []

        for i in range(len(Vertices)):
            for j in range(len([Vertices[i]])):
                x = Vertices[i][0]
                y = Vertices[i][1]
                if x != y:
                    X.append(x)
                    Y.append(y)
                    Z.append(0)
                else:
                    bX.append(x)
                    bY.append(y)
                    bZ.append(0)

        # rysowanie punktów do układu współrzędnych
        ax.scatter(X, Y, Z, c="red")
        # rysowanie punktów do układu na "czarno"
        ax.scatter(bX, bY, bZ, c="green")



        #rysowanie linii połączeń na układzie współrzędnych

        for i in range(len(Connections)):
            startX = Vertices[Connections[i][0] - 1][0]
            endX = Vertices[Connections[i][1] - 1][0]
            startY = Vertices[Connections[i][0] - 1][1]
            endY = Vertices[Connections[i][1] - 1][1]
            startZ = 0
            endZ = 0

            a = myArrow3D([startX, endX], [startY, endY], [startZ, endZ], mutation_scale=5, lw=0.5,
                          arrowstyle="simple", color="blue", alpha=.7)
            ax.add_artist(a)

            '''ax.quiver(
                startX, startY, startZ,  # <-- początek wektora
                endX - startX, endY - startY, endZ - startZ,  # <-- kierunek wektora
                color='blue', alpha=.3, lw=0.9,
                arrow_length_ratio=0.02 #długość grotu
            )'''



            ep_no = list(ep_dictionary.keys())
            # rysowanie linii połączeń na dla elementów przetwarzających
            for i in range(0, len(eps)):
                startX = eps[i][0][0]
                endX = eps[i][1][0]
                startY = eps[i][0][1]
                endY = eps[i][1][1]
                startZ = 0
                endZ = 0

                ax.plot([startX, endX], [startY, endY], [startZ, endZ], "yellow", alpha=0.5, linestyle='dotted')

                Ep_name = "Ep[" + str(ep_no[i]) + "]"
                ax.text(endX, endY, endZ + 0.02, Ep_name, size=10)

            '''ax.quiver(
                    startX, startY, startZ,  # <-- początek wektora
                    endX - startX, endY - startY, endZ - startZ,  # <-- kierunek wektora
                    color='black', alpha=.6, lw=1,
                    arrow_length_ratio=0.085  # długość grotu
                )'''



        #ustawienie etykiet na punktach
        for i in range(len(Vertices)):
            x = Vertices[i][0]
            y = Vertices[i][1]
            z = 0
            label = str(x) + ", " + str(y)# + ", " + str(z)
            ax.text(x + 0.06, y + 0.06, z + 0.003, label, size=6)

        plt.show()