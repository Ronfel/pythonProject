import subprocess
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_report(file_path, order_data):
    pdf = SimpleDocTemplate(file_path, pagesize=landscape(letter))

    # Lista para armazenar dados da tabela
    table_data = []

    # Adiciona itens do pedido
    table_data.append(["Número do\n Pedido:", "Data do Pedido:", "Cliente:", "Produto", "Quant.", "Preço Unitário", "Subtotal"])
    for item in order_data['itens']:
        table_data.append([order_data['numero_pedido'], order_data['data_pedido'], order_data['cliente'], item['produto'], str(item['qtde']), f"R${item['valor_unt']:.2f}", f"R${item['subtotal']:.2f}"])

    # Adiciona informações do recibo
    total_amount = sum(item['subtotal'] for item in order_data['itens'])
    table_data.append(["Recibo:", "", "", "", "", "", f"Total: R${total_amount:.2f}"])

    # Cria a tabela
    order_table = Table(table_data, colWidths=[60, 100, 100, 150, 50, 100, 100])

    # Aplica estilos à tabela
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, 1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    order_table.setStyle(style)

    # Constrói o PDF com a tabela
    pdf.build([order_table])

    # Abre o visualizador de PDF padrão do sistema
    subprocess.Popen(["start", "", file_path], shell=True)

# Dados para o relatório
dados_pedido = {
    "numero_pedido": "123456",
    "data_pedido": "01/12/2023",
    "cliente": "SpaceX",
    "itens": [
        {"produto": "Produto A", "qtde": 2, "valor_unt": 50.00, "subtotal": 100.00},
        {"produto": "Produto B", "qtde": 1, "valor_unt": 30.00, "subtotal": 30.00},
        {"produto": "Produto C", "qtde": 3, "valor_unt": 20.00, "subtotal": 60.00}
    ]
}

# Estudando geração de relatório
generate_report("pedido_e_recibo_colunado_com_titulo.pdf", dados_pedido)
