import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📊 Dashboard de Vendas", layout="wide")
st.title("📊 Dashboard Interativo de Vendas")

@st.cache_data
def carregar_dados():
    df_resumo = pd.read_excel("output/vendas_processado.xlsx", sheet_name="Resumo")
    df_detalhes = pd.read_excel("output/vendas_processado.xlsx", sheet_name="Detalhes")
    return df_resumo, df_detalhes

df_resumo, df_detalhes = carregar_dados()

with st.sidebar:
    st.header("🔄 Atualização")
    if st.button("Atualizar Dados"):
        from scripts.main import main
        main()
        st.cache_data.clear()
        st.success("✅ Dados atualizados!")

aba = st.tabs(["📈 Resumo Geral", "🔍 Detalhes"])

with aba[0]:
    st.subheader("Total de Vendas por Região")
    fig_bar = px.bar(df_resumo, x='Região', y='total_vendas', color='Região', text_auto=True)
    st.plotly_chart(fig_bar, use_container_width=True)

    st.subheader("Distribuição de Produtos Vendidos")
    df_produto = df_detalhes['Produto'].value_counts().reset_index()
    df_produto.columns = ['Produto', 'Quantidade']
    fig_pie = px.pie(df_produto, values='Quantidade', names='Produto', title='Produtos Vendidos')
    st.plotly_chart(fig_pie, use_container_width=True)

with aba[1]:
    st.subheader("Tabela de Vendas")
    st.dataframe(df_detalhes, use_container_width=True)

    st.subheader("Vendas ao Longo do Tempo")
    df_detalhes['Data de Venda'] = pd.to_datetime(df_detalhes['Data de Venda'])
    df_timeline = df_detalhes.resample('D', on='Data de Venda')['Valor Total'].sum().reset_index()
    fig_line = px.line(df_timeline, x='Data de Venda', y='Valor Total', title='Vendas por Data')
    st.plotly_chart(fig_line, use_container_width=True)
