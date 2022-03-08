"""
Functions for filtering a list of smiles strings without processing
"""

def smiles_length(df, min_length=10, max_length=50):
    df_filtered = df[df['smiles'].apply(lambda x: max_length > len(x) > min_length)]
    return df_filtered


def remove_elements(df, remove=["Se", "Si", "se", "si", "B", "I", "Cu", "cu", "Mn", "mn", "As", "as", "Ni", "ni"]):
    df_filtered = df[df['smiles'].apply(lambda x: any([char in remove for char in x]) == False)]
    return df_filtered


def remove_salts(df):
    df_filtered = df[df['smiles'].apply(lambda x: "." not in x)]
    return df_filtered


def get_het_carbon_ratio(smiles):
    hets = ["N", "O", "S", 'n', 'o', 's']
    if sum(map(smiles.count, ['C', 'c'])) > 0:
        ratio = sum(map(smiles.count, hets)) / sum(map(smiles.count, ['C', 'c']))
    else:
        ratio = 1

    return ratio


def het_carbon_ratio(df, min_ratio=0.2, max_ratio=0.8):
    df_filtered = df[df['smiles'].apply(lambda x: max_ratio > get_het_carbon_ratio(x) > min_ratio)]
    return df_filtered



