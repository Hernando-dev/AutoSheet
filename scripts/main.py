from limpar_dados import limpar_dados
from aplicar_formulas import aplicar_formulas
from formatar_planilha import formatar_planilha
from gerar_grafico_excel import gerar_grafico

if __name__ == "__main__":
    limpar_dados()
    aplicar_formulas()
    formatar_planilha()
    gerar_grafico()
    print("✅ Processamento completo. Arquivo final disponível em output/vendas_processado.xlsx")
