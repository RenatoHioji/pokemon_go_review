import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import numpy as np


data = {
    'ProdutoId': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],
    'Produto':[
        "Laptop", "Mouse",
        "Laptop", "Teclado",
        "Monitor", "Mouse",
        "Teclado", "Mouse",
        "Notebook", "Notebook",
        "Teclado", "Teclado",
        "Mouse", "Notebook",
        "Mouse", "Teclado",
        "Mouse", "Monitor",
        "Teclado", "Mouse"
    ]
}

df = pd.DataFrame(data)

cesta = df.pivot_table(index='ProdutoId', columns="Produto", aggfunc=lambda x:1, fill_value=0)

frequencia = apriori(cesta, min_support=0.05, use_colnames=True)

regras = association_rules(frequencia, metric="confidence", min_threshold=0.5)
if not regras.empty:
    jitter_strenght=0.002

    suporte_jitter =regras['support'] + np.random.uniform(-jitter_strenght, jitter_strenght, size=len(regras))

    confianca_jitter = regras['confidence'] + np.random.uniform(-jitter_strenght, jitter_strenght, size=len(regras))

    cores = plt.cm.tab10(np.linspace(0,1, len(regras)))

    plt.figure(figsize=(8,6))

    for i, row in regras.iterrows():
        antecedente = ', '.join(list(row['antecedents']))
        consequente = ', '.join(list(row['consequents']))
        label_regra = f"{antecedente} -> {consequente}"
        
        plt.scatter(suporte_jitter[i], confianca_jitter[i],
                    s=row['lift']*200,
                    alpha=0.6,
                    color=cores[i],
                    label=label_regra)
        
        plt.xlabel("Suporte")
        plt.ylabel("Confiança")
        plt.title("Regras de Associação")
        plt.legend(fontsize=8, bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
    plt.show()
    
else: 
    print("Nenhuma regra de associação encontrada. Tente diminuir o suporte mínimo ainda mais.")
    