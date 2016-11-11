import scipy.signal as sig
import matplotlib.pyplot as plt
import math


def link_reaction_1(K, T):
    W = [sig.lti([el1], [el2, 1]) for el1, el2 in zip(K, T)]
    st = [sig.step(el) for el in W]
    im = [sig.impulse(el) for el in W]
    Graph(st, im, len(W))
    return st, im

def link_reaction_2(K, T1, T2):
    W = [sig.lti([el1], [el3 ** 2, el2, 1]) for el1, el2, el3 in zip(K, T1, T2)]
    st = [sig.step(el) for el in W]
    im = [sig.impulse(el) for el in W]
    Graph(st, im, len(W))
    return st, im

def link_reaction_3(K, T):
    W = [sig.lti([el1], [el2, 0, 1]) for el1, el2 in zip(K, T)]
    st = [sig.step(el) for el in W]
    im = [sig.impulse(el) for el in W]
    Graph(st, im, len(W))
    return st, im

def Graph(st, im, N):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    for i in range(N):
        ax[0].plot(st[i][0], st[i][1], 'r')
        ax[1].plot(im[i][0], im[i][1], 'b') 
        fig.tight_layout()
    ax[0].set_xlabel('time', fontsize=10)
    ax[0].set_ylabel('Amplituda', fontsize=10)
    ax[1].set_xlabel('time', fontsize=10)
    ax[1].set_ylabel('Amplituda', fontsize=10)
    plt.show()