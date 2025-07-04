import json
import os
import sys
from pathlib import Path

# Adicionar o diretório do projeto ao Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pallet_controller.settings')

import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpRequest
from django.urls import resolve
from django.utils.encoding import force_str
import urllib.parse

# Inicializar Django
django.setup()
application = get_wsgi_application()


def handler(event, context):
    """
    Função serverless para processar requests Django no Netlify
    """
    try:
        # Extrair informações do evento Netlify
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        query_string = event.get('queryStringParameters') or {}
        headers = event.get('headers', {})
        body = event.get('body', '')

        # Remover prefixo /.netlify/functions/django se presente
        if path.startswith('/.netlify/functions/django'):
            path = path[len('/.netlify/functions/django'):]

        if not path.startswith('/'):
            path = '/' + path

        # Construir query string
        query_string_encoded = urllib.parse.urlencode(query_string) if query_string else ''

        # Criar objeto request Django
        environ = {
            'REQUEST_METHOD': http_method,
            'PATH_INFO': path,
            'QUERY_STRING': query_string_encoded,
            'CONTENT_TYPE': headers.get('content-type', ''),
            'CONTENT_LENGTH': str(len(body)) if body else '0',
            'SERVER_NAME': headers.get('host', 'localhost'),
            'SERVER_PORT': '443',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'https',
            'wsgi.input': None,
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
        }

        # Adicionar headers HTTP
        for key, value in headers.items():
            key = key.upper().replace('-', '_')
            if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                environ[f'HTTP_{key}'] = value

        # Processar body para POST requests
        if body and http_method in ['POST', 'PUT', 'PATCH']:
            if headers.get('content-type', '').startswith('application/json'):
                environ['wsgi.input'] = body.encode('utf-8')
            else:
                environ['wsgi.input'] = body.encode('utf-8')

        # Capturar resposta Django
        response_data = []
        response_status = [200]
        response_headers = []

        def start_response(status, headers, exc_info=None):
            response_status[0] = int(status.split(' ')[0])
            response_headers.extend(headers)

        # Executar aplicação Django
        response = application(environ, start_response)

        # Coletar dados da resposta
        for data in response:
            if data:
                response_data.append(data)

        # Construir resposta para Netlify
        response_body = b''.join(response_data).decode('utf-8')

        # Converter headers para formato Netlify
        netlify_headers = {}
        for header_name, header_value in response_headers:
            netlify_headers[header_name] = header_value

        return {
            'statusCode': response_status[0],
            'headers': netlify_headers,
            'body': response_body
        }

    except Exception as e:
        # Log do erro
        print(f"Erro na função Django: {str(e)}")
        import traceback
        traceback.print_exc()

        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'error': 'Internal Server Error',
                'message': str(e)
            })
        }


# Alias para compatibilidade
lambda_handler = handler

