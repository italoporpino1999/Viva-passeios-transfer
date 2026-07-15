import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Gerador de Ordem de Serviço")
st.title("📄 Gerador de Ordem de Serviço")

with st.form("os_form"):
    st.subheader("Informações Gerais")
    data_emissao = st.date_input("Data de Emissão", datetime.now())
    tipo_servico = st.text_input("Tipo de Serviço", "Traslado")
    status = st.selectbox("Status do Serviço", ["CONFIRMADO", "PENDENTE"])

    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome Completo do Cliente")
    whatsapp = st.text_input("Telefone / WhatsApp")
    cpf_cnpj = st.text_input("CPF / CNPJ")

    st.subheader("Programação e Rota")
    data_servico = st.date_input("Data do Serviço", datetime.now())
    local_embarque = st.text_input("Local de Embarque")
    local_desembarque = st.text_input("Local de Desembarque")
    hora_servico = st.text_input("Hora do Serviço (ex: 10:00)")

    st.subheader("Dados do Motorista e Veículo")
    nome_motorista = st.text_input("Nome do Motorista")
    carro = st.text_input("Modelo do Carro")
    cor_carro = st.text_input("Cor do Carro")
    placa_carro = st.text_input("Placa / Número do Veículo")
    
    submitted = st.form_submit_button("Gerar PDF")

if submitted:
    st.success("Dados preenchidos com sucesso!")
