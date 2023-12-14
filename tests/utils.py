import json
import requests
from allure_commons.types import AttachmentType
import logging
import allure


def api_post(url, **kwargs):
    with allure.step("API Request"):
        result = requests.post(url="https://demowebshop.tricentis.com/addproducttocart/details" + url, **kwargs)
        allure.attach(body=result.request.method + " " + result.request.url, name="Request URL",
                      attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True), name="Request body",
                      attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(body=json.dumps(result.text, indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
        return result
