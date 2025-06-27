import pandas as pd

def aplicar_formulas():
    print("Aplicando fórmulas...")
    df = pd.read_csv("../dados/vendas_limpo.csv")
    df['Valor Total'] = df['Quantidade'] * df['Preço Unitário']

    df_resumo = df.groupby('Região').agg(
        total_vendas=('Valor Total', 'sum'),
        qtd_pedidos=('Produto', 'count')
    ).reset_index()

    df.to_excel("../output/vendas_processado.xlsx", index=False, sheet_name="Detalhes")
    with pd.ExcelWriter("../output/vendas_processado.xlsx", mode='a', engine='openpyxl') as writer:
        df_resumo.to_excel(writer, sheet_name="Resumo", index=False)

    print("Fórmulas aplicadas e salvas.")
