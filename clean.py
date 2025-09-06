import nbformat

# carica il notebook
with open("Copia_di_Ernesto_BI.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# cancella i metadati problematici
nb.metadata.pop("widgets", None)

# salva un nuovo file pulito
with open("Copia_di_Ernesto_BI_clean.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
