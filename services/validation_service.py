import requests

def luhn_algorithm(card_number):
    """Valida o número do cartão usando o algoritmo de Luhn."""
    card_number = card_number.replace(" ", "")  # Remover espaços
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Duplicar os dígitos em posições ímpares
            n *= 2
            if n > 9:  # Se maior que 9, subtrair 9
                n -= 9
        total += n
    return total % 10 == 0


def get_card_issuer(bin_number):
    """Consulta o emissor do cartão usando o BIN."""
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            data = response.json()
            return {
                "bank": data.get("bank", {}).get("name"),
                "scheme": data.get("scheme"),
                "type": data.get("type"),
            }
        else:
            return {"error": "BIN não encontrado ou inválido."}
    except Exception as e:
        return {"error": str(e)}
