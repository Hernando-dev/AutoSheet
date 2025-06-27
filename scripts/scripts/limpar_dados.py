import pandas as pd

def limpar_dados():
    print("Limpando dados...")
    df = pd.read_excel("../planilhas/vendas_brutas.xlsx")

    # Limpeza básica
    df['Quantidade'] = df['Quantidade'].fillna(0).astype(int)
    df['Preço Unitário'] = df['Preço Unitário'].str.replace('R\$', '', regex=True).str.strip().astype(float)
    df['Data de Venda'] = pd.to_datetime(df['Data de Venda'], errors='coerce')

    df.to_csv("../dados/vendas_limpo.csv", index=False)
    print("Dados limpos salvos.")
