from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Data
from dotenv import load_dotenv
import os

# Conectando ao workspace do Azure ML
load_dotenv()
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
workspace = os.getenv("AZURE_ML_WORKSPACE")

ml_client = MLClient(
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace,
    credential=DefaultAzureCredential()
)

# Definindo caminho e informações do dataset
path_to_data = os.path.join("..", "data", "INMET_DF_processado.csv")

data = Data(
    name="INMET_DF_processado",
    version="1",
    description="Dados processados do INMET de Brasília em 2024",
    path=path_to_data,
    type="uri_file",
)

# Carregando o dataset para o workspace
ml_client.data.create_or_update(data)