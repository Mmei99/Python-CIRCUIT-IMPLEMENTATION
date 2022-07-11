import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 6 * np.pi, 100)

    fig1, (ax1, ax2) = plt.subplots(nrows=2)
    plot(x, np.sin(x), ax1)
    plot(x, np.random.random(100), ax2)

    fig2 = plt.figure()
    plot(x, np.cos(x))

    plt.show()

def plot(x, y, ax=None):
    if ax is None:
        ax = plt.gca()
    line, = ax.plot(x, y, 'go')
    ax.set_ylabel('Yabba dabba do!')
    return line

if __name__ == '__main__':
    main()