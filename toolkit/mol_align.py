from rdkit.Chem import rdMolDescriptors, rdMolAlign
from rdkit import Chem


def protonate_ligand(mol_noh):

    mol = Chem.AddHs(mol_noh, addCoords=True)
    # Check for carboxylate groups
    carboxylic_acid = Chem.MolFromSmarts("[CX3](=O)[OX2H1]")
    atom_indices = mol.GetSubstructMatch(carboxylic_acid)
    if len(atom_indices) > 0:
        # find the protonated oxygen and deprotonate it
        for idx_ in atom_indices:
            atom = mol.GetAtomWithIdx(idx_)
            if atom.GetTotalNumHs(includeNeighbors=True) != 0:
                atom.SetFormalCharge(-1)
                for n_atom in atom.GetNeighbors():
                    if n_atom.GetAtomicNum() == 1:
                        w_mol = Chem.RWMol(mol)
                        w_mol.RemoveAtom(n_atom.GetIdx())
    else:
        w_mol = mol

    return w_mol


def mol_2_crippen_align(probe_list, ref) -> list:

    score_list = []
    mol_list = []
    for conf, probe in enumerate(probe_list):
        probe = protonate_ligand(probe)
        crippen_probe = rdMolDescriptors._CalcCrippenContribs(probe)
        crippen_ref = rdMolDescriptors._CalcCrippenContribs(ref)
        crippenO3A = rdMolAlign.GetCrippenO3A(probe, ref, crippen_probe, crippen_ref)
        score = crippenO3A.Align()
        score_list.append(score)
        mol_list.append(probe)

    writer = Chem.SDWriter("probe_CA.sdf")
    for mol in mol_list:
        #w_mol = protonate_ligand(mol)
        writer.write(mol)

    return mol_list


def mol_2_o3d_align(probe_list, ref) -> list:

    score_list = []
    mol_list = []
    for conf, probe in enumerate(probe_list):
        probe = protonate_ligand(probe)
        o3d = rdMolAlign.GetO3A(probe, ref)
        score = o3d.Align()
        score_list.append(score)
        mol_list.append(probe)

    writer = Chem.SDWriter("probe_OA.sdf")
    for mol in mol_list:
        writer.write(mol)

    return mol_list

