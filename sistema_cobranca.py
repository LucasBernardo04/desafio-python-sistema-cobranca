# ==========================================
# DESAFIO 1 - SISTEMA DE COBRANÇA DE CLIENTES
# ==========================================

clientes = [
    {"nome": "Maria", "divida": 500},
    {"nome": "João", "divida": 350},
    {"nome": "Carlos", "divida": 800}
]

for cliente in clientes:

    nome = cliente["nome"]
    divida = cliente["divida"]
    total_pago = 0

    print("\n-----------------------------")
    print(f"Cliente: {nome}")
    print(f"Saldo devedor: R$ {divida:.2f}")

    while total_pago < divida:

        parcela = float(input("Digite o valor do pagamento: R$ "))

        if parcela <= 0:
            print("Valor inválido. Digite um valor maior que zero.")
        else:
            total_pago += parcela
            restante = divida - total_pago

            print(f"Total pago: R$ {total_pago:.2f}")

            if restante > 0:
                print(f"Falta pagar: R$ {restante:.2f}")
            else:
                print("Dívida quitada com sucesso!")

print("\nTodos os clientes foram processados.")
