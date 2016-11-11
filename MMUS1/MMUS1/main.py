import numpy as np
import func as f

K = np.linspace(0.1, 5, 5)
T = np.linspace(3, 8, 5)
T1 = np.linspace(6, 11, 5)
T2 = np.linspace(0.1, 5, 5)
st, im = f.link_reaction_1(K, T)
st1, im1 = f.link_reaction_2(K, T1, T2)
st2, im2 = f.link_reaction_3(K, T)

