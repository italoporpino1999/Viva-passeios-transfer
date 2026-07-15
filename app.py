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
    nome_cliente = st.text_input("Nome do Passageiro")
    tel_passageiro = st.text_input("Celular do Passageiro")
    num_passageiros = st.number_input("Número de Passageiros", min_value=1, value=1)
    
    st.subheader("Programação e Voo")
    data_servico = st.date_input("Data do Serviço")
    hora_servico = st.time_input("Hora do Serviço")
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
    try:
        molde_path = "Molde_Ordem_de_Servico_Viva.pdf"
        reader = PdfReader(molde_path)
        writer = PdfWriter()

        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)
        
        # Ajuste as coordenadas (x, y) conforme necessário
        c.setFont("Helvetica", 10)
        c.drawString(100, 700, f"Passageiro: {nome_cliente} | Tel: {tel_passageiro} | Qtd: {num_passageiros}")
        c.drawString(100, 680, f"Data: {data_servico} | Hora: {hora_servico} | Voo: {num_voo}")
        c.drawString(100, 660, f"Origem: {local_embarque} | Destino: {local_desembarque}")
        c.drawString(100, 640, f"Motorista: {nome_motorista} | Tel: {tel_motorista}")
        c.drawString(100, 620, f"Veículo: {modelo_carro} | Placa: {placa_carro}")
        c.drawString(100, 600, f"Obs: {obs}")
        
        c.save()
        packet.seek(0)
        
        new_pdf = PdfReader(packet)
        page = reader.pages[0]
        page.merge_page(new_pdf.pages[0])
        writer.add_page(page)
        
        output = io.BytesIO()
        writer.write(output)
        output.seek(0)
        
        st.download_button("📥 Baixar OS Final", output, "OS_Final.pdf", "application/pdf")
        st.success("PDF gerado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao gerar PDF: {e}. Verifique se o arquivo 'Molde_Ordem_de_Servico_Viva.pdf' está na raiz do seu GitHub.")
