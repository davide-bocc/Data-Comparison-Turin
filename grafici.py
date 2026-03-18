import matplotlib.pyplot as plt
import numpy as np

def plot_singolo(serie, titolo, ylabel, colore='steelblue'):
    plt.figure(figsize=(10, 5))
    plt.plot(serie.index, serie.values, '-o', markersize=3, color=colore)
    plt.title(titolo)
    plt.xlabel('Anno')
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def plot_normalizzato(serie_dict):
    nomi = list(serie_dict.keys())
    serie_list = list(serie_dict.values())

    colori = ['steelblue', 'seagreen', 'tomato', 'black']
    labels_y = [
        'Population (n. inhabitants)',
        'Remuneration (€)',
        'ICT companies (n. companies)',
        'Bike lanes (km)',
    ]

    fig, ax1 = plt.subplots(figsize=(13, 5))
    axes = [ax1]

    ax2 = ax1.twinx()
    axes.append(ax2)

    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 70))
    axes.append(ax3)

    ax4 = ax1.twinx()
    ax4.spines['right'].set_position(('outward', 140))
    axes.append(ax4)

    linee = []
    for i, (ax, nome, serie, colore, label_y) in enumerate(
            zip(axes, nomi, serie_list, colori, labels_y)
    ):
        l, = ax.plot(serie.index, serie.values, '-o', markersize=3,
                     color=colore, label=nome)
        ax.set_ylabel(label_y, color=colore)
        ax.tick_params(axis='y', labelcolor=colore)
        linee.append(l)

    ax1.set_xlabel('Anno')
    ax1.set_title('Torino – Full-scale comparison')

    etichette = [l.get_label() for l in linee]
    ax1.legend(
        linee, etichette,
        loc='center left',
        bbox_to_anchor=(0, 0.65),
        borderaxespad=0
    )

    fig.tight_layout()
    fig.subplots_adjust(left=0.2)
    plt.show()