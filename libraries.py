from loguru import logger
from config.uipapiconfig import (
    uipclient_folders,
    uipclient_libraries,
    FetchUIPathToken
)

import asyncio
from config.settings import settings

from helpers import clear_output, download_libs, get_versions, compare_versions, upload_libs
# Get PRE versions

def UpdateLibs():
    host_pre = f"https://cloud.uipath.com/{settings.UIP_LOGICAL_NAME}/{settings.UIP_TENANT_PRE}/orchestrator_"
    host_pro = f"https://cloud.uipath.com/{settings.UIP_LOGICAL_NAME}/{settings.UIP_TENANT_PRO}/orchestrator_"
    uipclient_libraries.api_client.configuration.access_token = FetchUIPathToken()
    clear_output()
    versionspre = get_versions(host_pre)
    versionspro = get_versions(host_pro)
    compared = compare_versions(versionspre, versionspro)
    logger.info(compared)
    uipclient_libraries.api_client.configuration.host = host_pre
    downloaded = download_libs(compared)
    uipclient_libraries.api_client.configuration.host = host_pro
    upload_libs(downloaded)
    
