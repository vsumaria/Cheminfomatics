from ase.io import *
from nequip.ase import NequIPCalculator
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import ase
from ase.io.trajectory import TrajectoryWriter
from ase.calculators.singlepoint import SinglePointCalculator as SPC

def enn_(atoms,calc):
    atoms.set_calculator(calc)
    e_nn = atoms.get_potential_energy()
    return e_nn

traj = read('all.xyz',':')
calc = NequIPCalculator.from_deployed_model('../../../pt_H_deployed.pth', species_to_type_name={s:s for s in ase.data.chemical_symbols})

def f_(atoms, calc=None):
    if calc==None:
        f = atoms.get_forces()
    else:
        atoms.set_calculator(calc)
        f = atoms.get_forces()
    return f

edft, enn, fdft, fnn = [],[],[],[]
for atoms in tqdm(traj):
    enn.append(enn_(atoms, calc))
    fnn.append(f_(atoms,calc))

traj_nn = TrajectoryWriter('collect_nn.traj','a')

i=0
for atoms in tqdm(traj):
    e = enn[i]
    f = fnn[i]
    atoms.set_calculator(SPC(atoms, energy=e, forces=f))
    traj_nn.write(atoms)
    i+=1
