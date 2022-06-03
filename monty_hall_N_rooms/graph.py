import matplotlib.pyplot as plt


def drawGraph(wr_test_change, wr_test_keep, wr_math_change, wr_math_keep, nor):
    x_axis = []
    for i in range(3, nor + 1):
        x_axis.append(i)

    data_dict = {"winning_rate_test_change": wr_test_change,
                 "winning_rate_test_keep": wr_test_keep,
                 "winning_rate_math_change": wr_math_change,
                 "winning_rate_math_keep": wr_math_keep,
                 "x_axis": x_axis}

    plt.plot("x_axis", "winning_rate_test_change", data=data_dict, color='blue', linestyle='-', label="test(change)")
    plt.plot("x_axis", "winning_rate_test_keep", data=data_dict, color='red', linestyle='-', label="test(keep)")
    plt.plot("x_axis", "winning_rate_math_change", data=data_dict, color='cyan', linestyle='-', label="math(change)")
    plt.plot("x_axis", "winning_rate_math_keep", data=data_dict, color='magenta', linestyle='-', label="math(keep)")

    plt.axis([3, nor, 0, 100])
    plt.grid(True, axis="both")
    plt.xlabel("Number Of Rooms", loc="right")
    plt.ylabel("Winning Rate", loc="top")
    plt.legend(loc="upper right", fontsize=8, frameon=True, facecolor="white")

    plt.show()
