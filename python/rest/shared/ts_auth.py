import base64
from datetime import datetime
import hmac
import pytz
import uuid


def add_basic(request_properties, customer_id, api_key):
    new_request_properties = request_properties
    new_request_properties['headers']['Authorization'] = create_basic_auth_string(customer_id, api_key)
    return new_request_properties['headers']

def add_digest(request_properties, customer_id, api_key):
    new_request_properties = request_properties
    new_request_properties['path_url'] = get_path(new_request_properties['url'])
    method = new_request_properties['method']
    # Add any missing headers with default values
    new_request_properties['headers']['x-ts-auth-method'] = new_request_properties['headers'].get('x-ts-auth-method', 'HMAC-SHA256')
    new_request_properties['headers']['x-ts-nonce'] = new_request_properties['headers'].get('x-ts-nonce', uuid.uuid1().hex)

    if method in ("PUT", "POST"):
        new_request_properties['headers']['Content-Type'] = new_request_properties['headers'].get('Content-Type', 'application/x-www-form-urlencoded')

    if 'Date' not in new_request_properties['headers'] and 'x-ts-date' not in new_request_properties['headers']:
        new_request_properties['headers']['Date'] = format_current_date()

    signature = generate_signature(customer_id, api_key, new_request_properties)
    new_request_properties['headers']['Authorization'] = 'TSA ' + customer_id + ':' + signature
    # Sort the headers in alpha order
    new_headers = {k: request_properties['headers'][k] for k in sorted(request_properties['headers'])}
    return new_headers

def create_basic_auth_string(customer_id, api_key):
    auth_string = customer_id + ":" + api_key
    auth_string = base64.b64encode(auth_string.encode())
    auth_string = auth_string.decode("utf-8")
    auth_string = "Basic " + auth_string
    return auth_string

def format_current_date():
    now = datetime.now(pytz.utc)
    return now.strftime('%a, %d %b %Y %H:%M:%S %Z').replace('UTC', 'GMT')

def generate_signature(customer_id, api_key, new_request_properties):
    method = new_request_properties['method']

    if new_request_properties['headers']['x-ts-auth-method'] == 'HMAC-SHA1' or new_request_properties['headers']['x-ts-auth-method'] == 'HMAC-SHA256':
        auth_method = new_request_properties['headers']['x-ts-auth-method'].split('-')[1]
    else:
        auth_method = new_request_properties['headers']['x-ts-auth-method']

    new_request_properties['body'] = new_request_properties.get('body', None)
    fields = new_request_properties['body']

    string_to_sign = method + '\n'
    string_to_sign += new_request_properties['headers'].get('Content-Type', '') + '\n'
    string_to_sign += new_request_properties['headers'].get('Date', '') + '\n'
    string_to_sign += 'x-ts-auth-method:' + new_request_properties['headers']['x-ts-auth-method'] + '\n'

    if 'x-ts-date' in new_request_properties['headers']:
        string_to_sign += 'x-ts-date:' + new_request_properties['headers']['x-ts-date'] + '\n'

    if 'x-ts-nonce' in new_request_properties['headers']:
        string_to_sign = string_to_sign + 'x-ts-nonce:' + new_request_properties['headers']['x-ts-nonce'] + '\n'

    if fields and fields is not None:
        if new_request_properties['headers']['Content-Type'] == 'application/json':
            string_to_sign += fields.decode('UTF-8') + '\n'
        elif new_request_properties['headers']['Content-Type'] == 'application/x-www-form-urlencoded':
            string_to_sign += fields + '\n'
        else:
            raise ValueError("Can't generate signature for this content type.")

    string_to_sign += new_request_properties['path_url']

    encoded_string_to_sign = string_to_sign.encode(encoding='utf-8')
    decoded_api_key = base64.b64decode(api_key)
    hmac_obj = hmac.new(decoded_api_key, encoded_string_to_sign, digestmod=auth_method)
    signature = base64.b64encode(hmac_obj.digest()).decode('utf-8')
    return signature

def get_hostname(url):
    parts = url.split('//')
    return parts[1].split('/')[0]

def get_path(url):
    parts = url.split('//')
    parts2 = parts[1].split('/')
    parts2.pop(0)
    path = ('/' + '/'.join(parts2))
    return path

def pretty_print_request(req):
    print('{}\n{}\r\n{}\r\n\r\n{}\n'.format(
        'Request:',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

