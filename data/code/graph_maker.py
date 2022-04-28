import matplotlib.pyplot as plt


class graph_maker_class():
    def graph_maker(self, yoko, total, zandaka_0, normal_graph, zandaka_graph, total_graph):


        print("@@@ @@@ @@@ @@@")
        plt.plot(yoko, normal_graph, label='qwerty')   # 普通のグラフ
        plt.plot(yoko, zandaka_graph, label='asdfgh')   # 借入額で横一線
        plt.plot(yoko, total_graph, label='zxcvbn')   # 最終的な総支払額で横一線
        # plt.plot(64, tate)
        # plt.plot(tate)

        print(total)
        for i in range(len(total)):
            if (total[i] > zandaka_0):
                print(total[i])
                plt.plot(i, total[i], marker='o', markersize=10)
                plt.text(i, total[i], "(" + str(i) + ", " + str(total[i]) + ")")
                # plt.scatter(i, total[i], c='k', s=5)
                break


        plt.legend()
        plt.savefig("./img.png")
        # plt.show()
