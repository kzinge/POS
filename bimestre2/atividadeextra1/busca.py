import requests

def buscar_pedido():
    pedido = int(input("Insira o número do pedido: "))

    r = requests.get(f'http://localhost:8000/pedidos/{pedido}')
        
    if r.status_code == 200:
        dados = r.json()
        
        print("\n--- Detalhes do Pedido ---")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

    else:
        print("Pedido não encontrado")

buscar_pedido()