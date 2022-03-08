import pandas as pd
from toolkit.smiles_filters import *



mcule_data = pd.read_csv("../data/mcule_purchasable_instock_v1.smi",
                         delimiter="\t",
                         names=['smiles', 'ID'])

print(len(mcule_data))

df_filtered = smiles_length(mcule_data, max_length=60)
print(len(df_filtered))

df_filtered2 = remove_elements(df_filtered)
print(len(df_filtered2))

df_filtered3 = remove_salts(df_filtered2)
print(len(df_filtered3))

df_filtered4 = het_carbon_ratio(df_filtered3)
print(len(df_filtered4))

df_filtered4.to_csv("../data/mcule_filtered2.csv")
