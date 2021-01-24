from rdkit import Chem




f1 = open('train.source', 'r')
f2 = open('train.target', 'r')
f3 = open('train.source_2fold', 'w')
f4 = open('train.target_2fold', 'w')
l1 = f1.readlines()
l2 = f2.readlines()
t = 0

for i in range(len(l1)):
    reactant1= str(l1[i]).replace('\n','')
    product1 = str(l2[i]).replace('\n', '')

    reactant1_mol = Chem.MolFromSmiles(reactant1)
    product1_mol = Chem.MolFromSmiles(product1)
    list_reactant = []
    list_product = []
    t += 1
    print(t)
    flag = True
    while flag:
        try:
            reactant1_equvalent_smiles = Chem.MolToSmiles(reactant1_mol, doRandom=True)
            product1_equvalent_smiles = Chem.MolToSmiles(product1_mol, doRandom=True)

            if (reactant1_equvalent_smiles not in list_reactant) and \
                    (reactant1_equvalent_smiles != reactant1) and \
                    (len(list_reactant) <= 0):
                list_reactant.append(reactant1_equvalent_smiles)

            if (product1_equvalent_smiles not in list_product) and \
                    (product1_equvalent_smiles != product1)and \
                    (len(list_product) <= 0):
                list_product.append(product1_equvalent_smiles)

            if len(list_reactant) > 0 and len(list_product) > 0:
                flag = False

                break

        except RuntimeError:
            print('this is timeEroor')
            continue

    f3.write(reactant1 + '\n' )
    f4.write(product1 + '\n')
    for h in range(len(list_reactant)):
        reactant0 = list_reactant[h]
        product0 = list_product[h]
        f3.write(reactant0 + '\n')
        f4.write(product0 + '\n')

