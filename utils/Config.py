import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    AZURE_DOC_INT_ENDPOINT = os.getenv("AZURE_DOC_INT_ENDPOINT")
    AZURE_DOC_INT_KEY = os.getenv("AZURE_DOC_INT_KEY")
    AZURE_STORAGE_CONNECTION = os.getenv("AZURE_STORAGE_CONNECTION")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")


