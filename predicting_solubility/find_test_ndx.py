import torch
from ase.io import *
from ase.io.trajectory import TrajectoryWriter
import numpy as np

traj = read('./all.xyz',':')
trajw = TrajectoryWriter('training_data.traj','a')

trainer = torch.load("/home/sva1syv/sd/PtCo/nequip_nnp/Pt_H/results/BOSCH-CMS-Pt-H/BOSCH-CMS-Pt-H/trainer.pth")
train_ids = trainer["train_idcs"].tolist()
valid_ids = trainer["val_idcs"].tolist()
test_ids =  [i for i in range(len(traj)) if i not in train_ids and i not in valid_ids]

# np.save('train_ids.npy',train_ids)                                                                                                                                                               
# np.save('valid_ids.npy',valid_ids)                                                                                                                                                               
# np.save('test_ids.npy',test_ids)                                                                                                                                                                 

for i in train_ids:
    atoms = traj[i]
    trajw.write(atoms)
