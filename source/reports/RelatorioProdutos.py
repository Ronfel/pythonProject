import subprocess
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def gerar_relatorio_produtos(file_path, product_data):
    pdf = SimpleDocTemplate(file_path, pagesize=landscape(letter))

    # Lista para armazenar dados da tabela
    table_data = []

    # Adiciona cabeçalho da tabela
    table_data.append(["ID Produto", "Nome do Produto", "Descrição", "Preço Unitário", "Estoque"])

    # Adiciona dados dos produtos
    for product in product_data:
        table_data.append([product.get('id'), product.get('nome'), product.get('descricao'), f"R${product.get('preco_unitario'):.2f}", product.get('estoque')])

    # Cria a tabela
    product_table = Table(table_data, colWidths=[60, 150, 200, 100, 60])

    # Aplica estilos à tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    product_table.setStyle(style)

    # Constrói o PDF com a tabela
    pdf.build([product_table])

    # Abre o visualizador de PDF padrão do sistema
    subprocess.Popen(["start", "", file_path], shell=True)

# Dados para o relatório de produtos
dados_produtos = [
    {"id": 1, "nome": "Produto A", "descricao": "Descrição do Produto A", "preco_unitario": 50.00, "estoque": 100},
    {"id": 2, "nome": "Produto B", "descricao": "Descrição do Produto B", "preco_unitario": 30.00, "estoque": 50},
    {"id": 3, "nome": "Produto C", "descricao": "Descrição do Produto C", "preco_unitario": 20.00, "estoque": 200}
]

def gerar():
    gerar_relatorio_produtos("relatorio_produtos.pdf", dados_produtos)
