#!/usr/bin/python3

from openapi_core.shortcuts import RequestValidator
import requests

def get_api_spec():
    # Load OpenAPI specification file
    with open('openapi.json', 'r') as file:
        api_spec = file.read()
    return api_spec

api_spec = get_api_spec()
request_validator = RequestValidator(api_spec)

def test_example_api():
    url = 'https://musicverse.onrender.com/'
    method = 'get'
    headers = {}
    data = None

    # Validate the request against the OpenAPI specification
    request = requests.Request(method, url, headers=headers, data=data).prepare()
    request_validator.validate(request)

    # Send the actual API request
    response = requests.get(url, headers=headers, data=data)

    # Validate the response against the OpenAPI specification
    response_validator = request_validator.validate_response(url, method, response.status_code, response.headers, response.text)
    response_validator.validate()

    assert response.status_code == 200
    assert 'key' in response.json()
