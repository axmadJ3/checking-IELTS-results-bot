import asyncio
import logging

import requests
import selenium
from bs4 import BeautifulSoup as bs


logger = logging.getLogger(__name__)

def run_parser(url: str) -> int:
    try:
        request = requests.get(url)
        logger.info('Парсер успешно отработал')
        return request.status_code
    
    except Exception as e:
        logger.error(f'Ошибка: {e}')
        return None
