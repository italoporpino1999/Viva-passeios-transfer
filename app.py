import streamlit as st
from datetime import datetime
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.set_page_config(page_title="Gerador de OS")
st.title("📄 Gerador de Ordem de Serviço")

# FORMULÁRIO
with st.form("os_form"):
    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome do Passageiro")
    # ... (demais campos)
    submitted = st.form_submit_button("Gerar OS Oficial")

if submitted:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # NOME DA EMPRESA (Topo)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(150, 750, "VIVA PASSEIOS E TRANSFER") # Altere para o nome da sua empresa
    c.setFont("Helvetica", 10)
    c.drawString(150, 735, "Seu transporte com segurança e conforto")
    c.line(50, 725, 550, 725)
    
    # Se você tiver um link da sua logo, descomente a linha abaixo:
    # c.drawImage("LINK_DA_SUA_LOGO_AQUI", 50, 730, width=80, height=50)

    # DADOS
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 680, f"Cliente: {nome_cliente}")
    # ... (resto do seu código)
    
    c.save()
    buffer.seek(0)
    st.download_button("📥 Baixar OS Oficial", buffer, "OS_Empresa.pdf", "application/pdf")
