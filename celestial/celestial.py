import os
import requests
import getpass
import json
import logging
BASE_URL = os.environ.get("CELESTIAL_BASE_URL") or 'https://celestial-automl.azurewebsites.net/'


def load_token():
    home = os.path.expanduser("~")
    path = f"{home}/.celestial/token"
    try:
        with open(path, 'r') as f:
            token = f.read()
        return token
    except OSError:
        return None


def get_new_token():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    response = requests.post(url=f'{BASE_URL}/client/tokens', auth=(username, password))
    payload = json.loads(response.content)
    return payload['token']

def _save_token(token):
    home = os.path.expanduser("~")
    path = f"{home}/.celestial"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f'{path}/token', 'w') as f:
        f.write(token)
        

def authenticate(func):
    def wrapper(*args, **kwargs):
        token = load_token() or get_new_token()
        _save_token(token)
        kwargs['token'] = token
        rval = func(*args, **kwargs)
        if 'error' in rval:
            token = get_new_token()
            _save_token(token)
            kwargs['token'] = token
            rval = func(*args, **kwargs)
        return rval
    return wrapper


class Trial(object):
    def __init__(self, study_id):
        self.base_url = BASE_URL
        self.study_id = study_id
        payload = self._get_parameters()
        self.parameters = payload['parameters']
        self.id = payload['meta']['id']

    @authenticate
    def _get_parameters(self, token):
        payload = requests.get(url=self._get_suggestion_url(),
                               headers={'Authorization': f'Bearer {token}'})
        logging.debug("Payload: " + str(payload))
        return payload.json()

    def _get_suggestion_url(self):
        return f"{self.base_url}/client/study/{self.study_id}/get-suggestion"

    def _add_result_url(self):
        return f"{self.base_url}/client/add-result"

    @authenticate
    def submit_result(self, **kwargs):
        if 'id' in kwargs:
            raise ValueError("Keyword argument with name 'id' not allowed.")
        token = kwargs.pop('token')
        data = kwargs.copy()
        data['id'] = self.id
        r = requests.post(url=self._add_result_url(),
                          json=data,
                          headers={'Authorization': f'Bearer {token}'})
        if r.status_code != 201:
            raise requests.ConnectionError(
                "Expected status code 201, but got {}".format(r.status_code))
        return r