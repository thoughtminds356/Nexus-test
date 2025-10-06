from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = os.getenv('AZURE_CONTAINER', 'videos')
    expiration_secs = None
    overwrite_files = True
    azure_ssl = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_domain = f'{self.account_name}.blob.core.windows.net'

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = os.getenv('AZURE_STATIC_CONTAINER', 'static')
    expiration_secs = None
    overwrite_files = True
    azure_ssl = True
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_domain = f'{self.account_name}.blob.core.windows.net'