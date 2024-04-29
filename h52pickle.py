import numpy as np
import pandas as pd
import pickle
import h5py
#tem = {'num_atoms':num_atoms, 'charges':charges, 'fragments':fragments, 'positions':positions, 'rxn':rxn}

def H52pickel(data, path, file_name, idx = None):
    reaction = [key for key in f.keys()]
    num_atoms, charges, rxn, fragments, _idx =   [], [], [], [], []
    r_pos, ts_pos, p_pos = [], [], []

    if idx == None:
        for i, rx in enumerate(reaction):
            RG, TSG, PG = f[rx]['RG'][()], f[rx]['TSG'][()],f[rx]['PG'][()]
            charge      = f[rx]['elements'][()]
            num_atom    = len(charge)
            fr          = [i for i in range(len(charge))]
            rxn.append(rx)
            num_atoms.append(num_atom)
            charges.append(charge)
            r_pos.append(RG)
            ts_pos.append(TSG)
            p_pos.append(PG)
            fragments.append(fr)
            _idx.append(i)
    else:

        i, rx = 0, reaction[int(idx)]
        RG, TSG, PG = f[rx]['RG'][()], f[rx]['TSG'][()],f[rx]['PG'][()]
        charge      = f[rx]['elements'][()]
        num_atom    = len(charge)
        fr          = [i for i in range(len(charge))]
        rxn.append(rx)
        num_atoms.append(num_atom)
        charges.append(charge)
        r_pos.append(RG)
        ts_pos.append(TSG)
        p_pos.append(PG)
        fragments.append(fr)
        _idx.append(i)

    sf = [0 for i in range(len(_idx))]
    r_ = {'num_atoms':num_atoms, 'charges':charges, 'positions':r_pos ,   'fragments':fragments,    'rxn':rxn}
    ts_= {'num_atoms':num_atoms, 'charges':charges, 'positions':ts_pos,   'fragments':fragments,    'rxn':rxn}
    p_ = {'num_atoms':num_atoms, 'charges':charges, 'positions':p_pos ,   'fragments':fragments,    'rxn':rxn}


    data_ = {'reactant':r_, 'product':p_, 'transition_state': ts_, "single_fragment":sf, "use_ind":_idx}

    with open(path + file_name + '.pkl', 'wb')  as ff:
        pickle.dump(data_, ff)


if __name__ == "__main__":

    f = h5py.File('db.h5','r')
    #data = H52pickel(f, './', 'db2')
    data = H52pickel(f, './', 'db19000', 19000)
