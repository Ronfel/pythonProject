import subprocess
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def gerar_relatorio_clientes(file_path, client_data):
    pdf = SimpleDocTemplate(file_path, pagesize=landscape(letter))

    # Lista para armazenar dados da tabela
    table_data = []

    # Adiciona cabeçalho da tabela
    table_data.append(["ID Cliente", "Nome", "Email", "Telefone", "Endereço"])

    # Adiciona dados dos clientes
    for client in client_data:
        table_data.append([client.get('id'), client.get('nome'), client.get('email'), client.get('telefone'), client.get('endereco')])

    # Cria a tabela
    client_table = Table(table_data, colWidths=[60, 150, 150, 100, 200])

    # Aplica estilos à tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    client_table.setStyle(style)

    # Constrói o PDF com a tabela
    pdf.build([client_table])

    # Abre o visualizador de PDF padrão do sistema
    subprocess.Popen(["start", "", file_path], shell=True)

# Dados para o relatório de clientes
dados_clientes = [
    {"id": 1, "nome": "Elon Musk", "email": "elon@musk.com", "telefone": "123-456-7890", "endereco": "123 SpaceX Avenue"},
    {"id": 2, "nome": "Jeff Bezos", "email": "jeff@bezos.com", "telefone": "987-654-3210", "endereco": "456 Blue Origin Street"},
    {"id": 3, "nome": "Satya Nadella", "email": "satya@ms.com", "telefone": "555-123-4567", "endereco": "789 Microsoft Road"}
]

def gerar():
    gerar_relatorio_clientes("relatorio_clientes.pdf", dados_clientes)
