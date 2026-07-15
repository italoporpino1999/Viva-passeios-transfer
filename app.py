import streamlit as st
import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
from PyPDF2 import PdfReader, PdfWriter

st.set_page_config(page_title="Gerador de Ordem de Serviço")

st.title("📄 Gerador de Ordem de Serviço")
st.write("Preencha os dados abaixo para gerar sua OS.")

# Nome do seu arquivo molde
TEMPLATE_PDF = "Molde_Ordem_de_Servico_Viva.pdf"

# Formulário de entrada de dados
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
    
    submitted = st.form_submit_button("Gerar PDF")

if submitted:
    st.write("Processando a criação do PDF...")
    # Aqui entraria a lógica de preenchimento do PDF que você tinha antes
