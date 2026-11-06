# ==========================================
# PROJETO 1: CLI de Validação de Pedidos e Carrinho
# Autor: João Pedro
# Objetivo: Validação de regras de negócio, cupons e cálculo de frete
# ==========================================

print("=== BEM-VINDO AO SISTEMA DE PEDIDOS ===")

# 1. Entrada de dados
nome_cliente = input("Digite o nome do cliente: ")
valor_item1 = float(input("Digite o valor do 1º item (R$): "))
valor_item2 = float(input("Digite o valor do 2º item (R$): "))
cupom = input("Possui cupom de desconto? (Digite IFOOD10 ou Nao): ").strip().upper()

# 2. Processamento dos valores
subtotal = valor_item1 + valor_item2
desconto = 0.0

# Aplicação da regra do cupom
if cupom == "IFOOD10":
    desconto = subtotal * 0.10
    print("✅ Cupom IFOOD10 aplicado! (10% OFF)")
elif cupom != "NAO" and cupom != "":
    print("❌ Cupom inválido. Nenhum desconto aplicado.")

valor_com_desconto = subtotal - desconto

# Regra de Frete Grátis (pedidos a partir de R$ 50,00)
VALOR_MINIMO_FRETE_GRATIS = 50.0
TAXA_FRETE = 7.00

if valor_com_desconto >= VALOR_MINIMO_FRETE_GRATIS:
    frete = 0.0
    print("🚀 Parabéns! Seu pedido atingiu o valor para FRETE GRÁTIS.")
else:
    frete = TAXA_FRETE
    falta_para_frete_gratis = VALOR_MINIMO_FRETE_GRATIS - valor_com_desconto
    print(f"🚚 Frete: R$ {frete:.2f} (Faltam R$ {falta_para_frete_gratis:.2f} para frete grátis).")

total_final = valor_com_desconto + frete

# 3. Exibição do resumo do pedido
print("\n" + "="*35)
print(f"RESUMO DO PEDIDO - CLIENTE: {nome_cliente.upper()}")
print("="*35)
print(f"Subtotal dos itens : R$ {subtotal:.2f}")
print(f"Desconto aplicado  : R$ {desconto:.2f}")
print(f"Taxa de Entrega    : R$ {frete:.2f}")
print("-" * 35)
print(f"TOTAL A PAGAR      : R$ {total_final:.2f}")
print("="*35)





    