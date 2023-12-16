import subprocess
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def gerar_relatorio_fornecedores(file_path, fornecedor_data):
    pdf = SimpleDocTemplate(file_path, pagesize=landscape(letter))

    # Lista para armazenar dados da tabela
    table_data = []

    # Adiciona cabeçalho da tabela
    table_data.append(["ID Fornecedor", "Nome do Fornecedor", "Contato", "Email", "Telefone", "Endereço"])

    # Adiciona dados dos fornecedores
    for fornecedor in fornecedor_data:
        table_data.append([fornecedor.get('id'), fornecedor.get('nome'), fornecedor.get('contato'), fornecedor.get('email'), fornecedor.get('telefone'), fornecedor.get('endereco')])

    # Cria a tabela
    fornecedor_table = Table(table_data, colWidths=[60, 150, 100, 150, 100, 200])

    # Aplica estilos à tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    fornecedor_table.setStyle(style)

    # Constrói o PDF com a tabela
    pdf.build([fornecedor_table])

    # Abre o visualizador de PDF padrão do sistema
    subprocess.Popen(["start", "", file_path], shell=True)

# Dados para o relatório de fornecedores
dados_fornecedores = [
    {"id": 1, "nome": "Fornecedor A", "contato": "João Silva", "email": "joao@fornecedorA.com", "telefone": "123-456-7890", "endereco": "123 Supplier Street"},
    {"id": 2, "nome": "Fornecedor B", "contato": "Maria Oliveira", "email": "maria@fornecedorB.com", "telefone": "987-654-3210", "endereco": "456 Supply Avenue"},
    {"id": 3, "nome": "Fornecedor C", "contato": "Carlos Santos", "email": "carlos@fornecedorC.com", "telefone": "555-123-4567", "endereco": "789 Provider Road"}
]

def gerar():
    gerar_relatorio_fornecedores("relatorio_fornecedores.pdf", dados_fornecedores)
