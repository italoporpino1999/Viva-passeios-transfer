import streamlit as st
from datetime import datetime
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.set_page_config(page_title="Gerador de OS - Viva Passeios")
st.title("📄 Gerador de Ordem de Serviço")

with st.form("os_form"):
    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome do Passageiro")
    tel_passageiro = st.text_input("Celular do Passageiro")
    num_passageiros = st.number_input("Número de Passageiros", min_value=1, value=1)
    
    st.subheader("Programação")
    data_servico = st.date_input("Data do Serviço")
    hora_servico = st.text_input("Hora do Serviço (ex: 10:00)")
    num_voo = st.text_input("Número do Voo")
    local_embarque = st.text_input("Local de Embarque")
    local_desembarque = st.text_input("Local de Desembarque")
    
    st.subheader("Dados do Motorista e Veículo")
    nome_motorista = st.text_input("Nome do Motorista")
    tel_motorista = st.text_input("Telefone do Motorista")
    modelo_carro = st.text_input("Modelo do Carro")
    placa_carro = st.text_input("Placa do Veículo")
    
    st.subheader("Observações")
    obs = st.text_area("Observações")
    
    submitted = st.form_submit_button("Gerar OS Oficial")

if submitted:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Cabeçalho da Empresa
    c.setFont("Helvetica-Bold", 22)
    c.drawString(120, 750, "VIVA PASSEIOS E TRANSFER")
    c.line(50, 740, 550, 740)
    
    # Dados no PDF
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 700, f"Passageiro: {nome_cliente} | Tel: {tel_passageiro}")
    c.drawString(50, 680, f"Data: {data_servico} | Hora: {hora_servico} | Voo: {num_voo}")
    c.drawString(50, 660, f"Origem: {local_embarque} | Destino: {local_desembarque}")
    c.drawString(50, 640, f"Motorista: {nome_motorista} (Tel: {tel_motorista})")
    c.drawString(50, 620, f"Veículo: {modelo_carro} | Placa: {placa_carro}")
    c.drawString(50, 580, f"Observações: {obs}")
    
    c.save()
    buffer.seek(0)
    
    st.download_button("📥 Baixar OS Final", buffer, "OS_Viva_Passeios.pdf", "application/pdf")
    st.success("PDF pronto para baixar!")
