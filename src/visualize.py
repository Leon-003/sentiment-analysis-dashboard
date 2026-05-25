import matplotlib.pyplot as plt

def create_graph(emotions):

    fig, ax1 = plt.subplots()

    ax1.bar(
        emotions.keys(),
        emotions.values()
    )

    fig.autofmt_xdate()

    plt.savefig(
        'outputs/graphs/emotion_graph.png'
    )

    plt.close()