import streamlit as st
import os
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
from PyPDF2 import PdfReader, PdfWriter

st.set_page_config(page_title="Gerador de OS - Viva Passeios", layout="centered")

st.title("📄 Gerador de Ordem de Serviço")
st.write("Preencha os dados abaixo para gerar a Ordem de Serviço em PDF.")

# Nome do seu arquivo molde que está no GitHub
TEMPLATE_PDF = "Molde_Ordem_de_Servico_Viva_Passeios.pdf"

# Formulário de entrada de dados
with st.form("os_form"):
    st.subheader("Informações Gerais")
    data_emissao = st.date_input("Data de Emissão", datetime.now())
    tipo_servico = st.text_input("Tipo de Serviço", "Traslado")
    status = st.selectbox("Status do Serviço", ["CONFIRMADO", "EM ANDAMENTO", "FINALIZADO"])
    
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
    if not os.path.exists(TEMPLATE_PDF):
        st.error(f"Erro: O arquivo modelo '{TEMPLATE_PDF}' não foi encontrado no servidor.")
    else:
        try:
            # 1. Desenhar as informações do formulário em um PDF temporário na memória usando o ReportLab
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFont("Helvetica", 9) # Usar fonte padrão limpa
            
            # --- COORDENADAS DE ESCRITA (Ajustáveis X, Y) ---
            # Seção: Informações Gerais
            can.drawString(55, 582, data_emissao.strftime('%d/%m/%Y'))
            can.drawString(205, 582, tipo_servico)
            can.drawString(55, 545, status)
            
            # Seção: Dados do Cliente
            can.drawString(335, 582, nome_cliente)
            can.drawString(335, 545, whatsapp)
            can.drawString(510, 545, cpf_cnpj)
            
            # Seção: Programação e Rota
            can.drawString(55, 480, data_servico.strftime('%d/%m/%Y'))
            can.drawString(205, 480, hora_apresentacao)
            can.drawString(335, 480, hora_partida)
            can.drawString(460, 480, voo)
            
            can.drawString(55, 450, origem)
            can.drawString(335, 450, destino)
            
            # Escrever lista de passageiros (com quebra de linha simples se for grande)
            p_lines = passageiros.split('\n')
            y_pos = 415
            for line in p_lines[:3]: # Limita a 3 linhas visuais para não estourar o campo
                can.drawString(55, y_pos, line)
                y_pos -= 12
                
            can.drawString(335, 415, str(qtd_pessoas))
            can.drawString(460, 415, bagagem)
            
            # Seção: Veículo Alocado
            can.drawString(55, 335, veiculo_modelo)
            can.drawString(170, 335, veiculo_placa)
            can.drawString(55, 310, veiculo_cat)
            
            # Seção: Motorista
            can.drawString(335, 335, motorista_nome)
            can.drawString(335, 310, motorista_tel)
            
            can.save()
            packet.seek(0)
            
            # 2. Ler o PDF temporário e mesclar com o PDF de molde usando o PyPDF2
            new_pdf = PdfReader(packet)
            existing_pdf = PdfReader(open(TEMPLATE_PDF, "rb"))
            output = PdfWriter()
            
            # Mesclar a primeira página do molde com os textos que desenhamos
            page = existing_pdf.pages[0]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)
            
            # Salvar o resultado na memória para o Streamlit disponibilizar para download
            output_stream = io.BytesIO()
            output.write(output_stream)
            output_bytes = output_stream.getvalue()
            
            st.success("✨ Ordem de Serviço gerada com sucesso!")
            
            # Botão de download do PDF pronto
            st.download_button(
                label="📥 Baixar Ordem de Serviço (PDF)",
                data=output_bytes,
                file_name=f"OS_{nome_cliente.replace(' ', '_')}_{data_servico.strftime('%d-%m-%Y')}.pdf",
                mime="application/pdf"
            )
            
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar o PDF: {e}")
