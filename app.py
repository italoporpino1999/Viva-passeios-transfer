import streamlit as st
import io
import requests
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

st.set_page_config(page_title="Gerador de OS - Viva Passeios")
st.title("📄 Gerador de Ordem de Serviço")

# Link da sua logo extraído do seu perfil
LINK_LOGO = "https://scontent-gru2-1.cdninstagram.com/v/t51.2885-19/460775586_1189445105658604_2628286955938883713_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-gru2-1.cdninstagram.com&_nc_cat=105&_nc_ohc=8x2q_5fE5K8Q7kNvgFv0Xl-&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AYBvG7K21L2fB-zB8W0YlXg8P9-n1XWv24tLg4zVwWb6YQ&oe=669B0C55&_nc_sid=547c13"

with st.form("os_form"):
    st.subheader("Dados do Cliente")
    nome_cliente = st.text_input("Nome do Passageiro")
    tel_passageiro = st.text_input("Celular do Passageiro")
    num_passageiros = st.number_input("Número de Passageiros", min_value=1, value=1)
    
    st.subheader("Programação e Voo")
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
    
    # Desenhar Logo
    try:
        response = requests.get(LINK_LOGO, timeout=10)
        img_data = io.BytesIO(response.content)
        c.drawImage(img_data, 50, 680, width=80, height=80)
    except:
        pass # Caso a logo não carregue, o PDF é gerado mesmo assim

    # Nome da Empresa e Cabeçalho
    c.setFont("Helvetica-Bold", 20)
    c.drawString(150, 730, "VIVA PASSEIOS E TRANSFER")
    c.setFont("Helvetica", 10)
    c.drawString(150, 715, "Seu transporte com segurança e conforto")
    c.line(50, 670, 550, 670)
    
    # Dados no PDF
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 640, f"PASSAGEIRO: {nome_cliente}")
    c.drawString(300, 640, f"CEL: {tel_passageiro}")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, 610, f"DATA: {data_servico}   HORA: {hora_servico}   VOO: {num_voo}")
    c.drawString(50, 590, f"EMBARQUE: {local_embarque}")
    c.drawString(50, 570, f"DESEMBARQUE: {local_desembarque}")
    
    c.drawString(50, 530, f"MOTORISTA: {nome_motorista}")
    c.drawString(300, 530, f"CEL: {tel_motorista}")
    c.drawString(50, 510, f"VEÍCULO: {modelo_carro}    PLACA: {placa_carro}")
    
    c.drawString(50, 470, f"OBSERVAÇÕES: {obs}")
    
    c.save()
    buffer.seek(0)
    
    st.download_button("📥 Baixar OS Oficial", buffer, "OS_Viva_Passeios.pdf", "application/pdf")
    st.success("PDF gerado com sucesso!")
