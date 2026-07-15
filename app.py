import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Gerador de OS - Viva Passeios", layout="centered")

st.title("📄 Gerador de Ordem de Serviço")
st.write("Preencha os dados abaixo para gerar a Ordem de Serviço em PDF.")

# Formulário de entrada de dados
with st.form("os_form"):
    st.subheader("Informações Gerais")
    data_emissao = st.date_input("Data de Emissão", datetime.now())
    tipo_servico = st.text_input("Tipo de Serviço", "Traslado")
    status = st.selectbox("Status do Serviço", ["Confirmado", "Em Andamento", "Finalizado"])
    
    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome Completo do Cliente")
    whatsapp = st.text_input("Telefone / WhatsApp")
    cpf_cnpj = st.text_input("CPF / CNPJ")
    
    st.subheader("Programação e Rota")
    data_servico = st.date_input("Data do Serviço", datetime.now())
    hora_apresentacao = st.text_input("Hora Apresentação", "00:00")
    hora_partida = st.text_input("Hora Partida", "00:00")
    voo = st.text_input("Cia Aérea / Voo")
    origem = st.text_input("Ponto de Partida (Origem)")
    destino = st.text_input("Ponto de Chegada (Destino)")
    passageiros = st.text_area("Passageiros (Nomes)")
    qtd_pessoas = st.number_input("Qtd de Pessoas", min_value=1, value=1)
    bagagem = st.text_input("Franquia de Bagagem", "Padrão")
    
    st.subheader("Veículo & Motorista")
    veiculo_modelo = st.text_input("Modelo do Veículo")
    veiculo_placa = st.text_input("Placa / Cor")
    veiculo_cat = st.text_input("Categoria do Carro")
    motorista_nome = st.text_input("Nome do Motorista / Guia")
    motorista_tel = st.text_input("Telefone de Contato")

    submit = st.form_submit_button("Gerar Ordem de Serviço")

if submit:
    st.success("Dados processados com sucesso! Gerando arquivo...")
