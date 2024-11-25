import streamlit as st
import requests
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card 
from services.validation_service import luhn_algorithm


# Função para buscar informações do cartão via Binlist
def get_card_info(bin_number):
    """
    Consulta a API do Binlist para obter informações sobre o cartão com base no BIN/IIN.
    """
    try:
        url = f"https://lookup.binlist.net/{bin_number}"
        headers = {"Accept-Version": "3"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:  # Requisição bem-sucedida
            data = response.json()
            return {
                "bank": data.get("bank", {}).get("name", "Informações indisponíveis"),
                "scheme": data.get("scheme", "Não identificado"),
                "type": data.get("type", "Não identificado"),
                "country": data.get("country", {}).get("name", "Desconhecido"),
                "country_emoji": data.get("country", {}).get("emoji", ""),
                "prepaid": data.get("prepaid", "Não identificado"),
            }
        else:  # Caso a API retorne um erro
            return {"error": f"Erro na API Binlist: {response.status_code}"}
    except Exception as e:
        return {"error": f"Erro ao consultar a API Binlist: {e}"}


def configure_interface():
    st.title("Upload arquivo DIO - Desafio 1 Python Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        file_name = uploaded_file.name
        blob_url = upload_blob(uploaded_file, file_name)

        if blob_url:
            st.write(f"Arquivo {file_name} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analize_credit_card(blob_url)

            if credit_card_info:
                # Validação do Algoritmo de Luhn
                card_number = credit_card_info.get("card_number", "")
                is_valid_luhn = luhn_algorithm(card_number)

                # Buscar informações do cartão com BIN Lookup
                if card_number:
                    bin_number = card_number.replace(" ", "")[:6]  # Captura os primeiros 6 dígitos
                    card_issuer = get_card_info(bin_number)
                else:
                    card_issuer = {"bank": "Não identificado", "scheme": "Não identificado", "type": "Não identificado"}

                show_image_and_validation(blob_url, credit_card_info, is_valid_luhn, card_issuer)
            else:
                st.error("Erro ao analisar as informações do cartão.")
        else:
            st.error(f"Erro ao tentar enviar o arquivo {file_name} para o Azure Blob Storage")


def show_image_and_validation(blob_url, credit_card_info, is_valid_luhn, card_issuer):
    st.image(blob_url, caption="Imagem Enviada", use_container_width=True)
    st.write("Resultado da validação:")

    if credit_card_info.get("card_name"):
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"**Nome do Titular:** {credit_card_info['card_name']}")
        st.write(f"**Banco Emissor:** {card_issuer.get('bank', 'Informações indisponíveis')}")
        st.write(f"**Esquema do Cartão:** {card_issuer.get('scheme', 'Não identificado')}")
        st.write(f"**Tipo:** {card_issuer.get('type', 'Não identificado')}")
        st.write(f"**País:** {card_issuer.get('country', 'Desconhecido')} {card_issuer.get('country_emoji', '')}")
        st.write(f"**Pré-pago:** {'Sim' if card_issuer.get('prepaid') else 'Não'}")
        st.write(f"**Data de Validade:** {credit_card_info['expiry_date']}")
        st.write(f"**Número do Cartão:** {credit_card_info['card_number']}")
        st.write(f"**Validação do Número pelo Algoritmo de Luhn:** {'✅ Válido' if is_valid_luhn else '❌ Inválido'}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Não foi possível validar este cartão.")


if __name__ == "__main__":
    configure_interface()
