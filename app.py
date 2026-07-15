import streamlit as st
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

st.set_page_config(page_title="Gerador de Ordem de Serviço")
st.title("📄 Gerador de Ordem de Serviço")

with st.form("os_form"):
    st.subheader("Informações Gerais")
    data_emissao = st.date_input("Data de Emissão", datetime.now())
    tipo_servico = st.text_input("Tipo de Serviço", "Traslado")
    
    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome Completo do Cliente")
    whatsapp = st.text_input("Telefone / WhatsApp")
    
    st.subheader("Programação e Rota")
    local_embarque = st.text_input("Local de Embarque")
    local_desembarque = st.text_input("Local de Desembarque")

    st.subheader("Dados do Motorista e Veículo")
    nome_motorista = st.text_input("Nome do Motorista")
    telefone_motorista = st.text_input("Telefone do Motorista")
    carro = st.text_input("Modelo do Carro")
    
    st.subheader("Informações Adicionais")
    observacoes = st.text_area("Observações")
    
    submitted = st.form_submit_button("Gerar PDF")

if submitted:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    c.drawString(100, 750, f"Ordem de Serviço - {tipo_servico}")
    c.drawString(100, 730, f"Cliente: {nome_cliente}")
    c.drawString(100, 710, f"Embarque: {local_embarque}")
    c.drawString(100, 690, f"Desembarque: {local_desembarque}")
    c.drawString(100, 670, f"Motorista: {nome_motorista} (Tel: {telefone_motorista})")
    c.drawString(100, 650, f"Carro: {carro}")
    c.drawString(100, 630, f"Observações: {observacoes}")
    
    c.save()
    buffer.seek(0)
    
    st.download_button(
        label="📥 Baixar PDF Gerado",
        data=buffer,
        file_name="Ordem_de_Servico.pdf",
        mime="application/pdf"
    )
    st.success("PDF pronto para baixar!")
