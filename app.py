import streamlit as st
from datetime import datetime
import io
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.set_page_config(page_title="Gerador de OS")
st.title("📄 Gerador de Ordem de Serviço")

with st.form("os_form"):
    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome Completo do Cliente")
    
    st.subheader("Programação")
    local_embarque = st.text_input("Local de Embarque")
    local_desembarque = st.text_input("Local de Desembarque")
    
    st.subheader("Motorista")
    nome_motorista = st.text_input("Nome do Motorista")
    telefone_motorista = st.text_input("Telefone do Motorista")
    
    st.subheader("Observações")
    obs = st.text_area("Observações")
    
    submitted = st.form_submit_button("Gerar OS Oficial")

if submitted:
    # Ler o molde original
    molde_path = "Molde_Ordem_de_Servico_Viva.pdf"
    reader = PdfReader(molde_path)
    writer = PdfWriter()

    # Criar camada de texto para escrever por cima
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    # Adicionar os dados (ajuste o x e y para alinhar com seu molde)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, 650, f"Cliente: {nome_cliente}")
    c.drawString(100, 630, f"Embarque: {local_embarque}")
    c.drawString(100, 610, f"Desembarque: {local_desembarque}")
    c.drawString(100, 590, f"Motorista: {nome_motorista} - {telefone_motorista}")
    c.drawString(100, 570, f"Obs: {obs}")
    
    c.save()
    packet.seek(0)
    
    # Combinar o molde com a nova camada de texto
    new_pdf = PdfReader(packet)
    page = reader.pages[0]
    page.merge_page(new_pdf.pages[0])
    writer.add_page(page)
    
    output = io.BytesIO()
    writer.write(output)
    output.seek(0)
    
    st.download_button("📥 Baixar OS Final", output, "OS_Final.pdf", "application/pdf")
    st.success("PDF gerado sobre o molde!")
