from parser.celery import parser
from service import get_xml_response


@parser.task
def get_links():
    base_url = 'https://zakupki.gov.ru'
    result = get_xml_response(base_url)
    return result
