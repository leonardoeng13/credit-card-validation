card_url = "https://<sua-conta>.blob.core.windows.net/<seu-container>/<nome-do-arquivo>"

try:
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient

    AZURE_DOC_INT_ENDPOINT = "https://doc-ai102-fraud.cognitiveservices.azure.com/"
    AZURE_DOC_INT_KEY = "7TyUOsqYYrGzI1pkIKwtFCwTYyrxgiQgr8mfYyxPYQ1axaDcL799JQQJ99AKACYeBjFXJ3w3AAALACOGBcjG"

    client = DocumentIntelligenceClient(AZURE_DOC_INT_ENDPOINT=AZURE_DOC_INT_ENDPOINT, credential=AzureKeyCredential(AZURE_DOC_INT_KEY))
    poller = client.begin_analyze_document(model_id="prebuilt-creditCard", document_url=card_url)
    result = poller.result()

    for document in result.documents:
        print("Card Name:", document.fields.get("CardHolderName", {}).get("value"))
        print("Card Number:", document.fields.get("CardNumber", {}).get("value"))
        print("Expiry Date:", document.fields.get("ExpirationDate", {}).get("value"))
        print("Bank Name:", document.fields.get("IssuingBank", {}).get("value"))

except Exception as e:
    print(f"Erro: {e}")
