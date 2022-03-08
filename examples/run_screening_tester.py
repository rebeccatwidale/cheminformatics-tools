import timeit
code = """from toolkit.mol_align import mol_2_crippen_align, mol_2_o3d_align
from toolkit.utils import create_output_directory
import pandas as pd
import os
from rdkit import Chem
import subprocess



smiles = pd.read_csv("../data/mcule_smiles_toscore.csv", delimiter="\t", names=['smiles', "ID"])

smiles_list = smiles['smiles'].tolist()

ph4 = Chem.SDMolSupplier("../data/new_t2_ph4_test.sdf")[0]

for root, dirs, files in os.walk("../data/test"):
    for file in files:
        mol = Chem.SDMolSupplier(f"../data/test/{file}")[0]
        if Chem.MolToSmiles(mol) in smiles_list:
            conformers = Chem.SDMolSupplier(f"../data/test/{file}")
            with create_output_directory():
                ca_poses = mol_2_crippen_align(conformers, ph4)
                oa_poses = mol_2_o3d_align(conformers, ph4)
                subprocess.call('conda activate shapeit', shell=True)
                subprocess.call("shape-it -r ../../data/new_t2_ph4_test.sdf -d probe_CA.sdf -o probe_CASS.sdf --scoreOnly --noRef -x -e -k 'mmff94'", shell=True)
                subprocess.call('conda deactivate', shell=True)"""

execution_time = timeit.timeit(code, number=1)
print(execution_time)