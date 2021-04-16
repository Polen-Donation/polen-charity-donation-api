import requests
import json


class PolenCharityDonationAPI:
    base_url = 'https://api.polen.com.br/api/v2'

    def __init__(self, api_token: str):
        self.api_token = api_token

    # Cause

    def get_all_cause(self, params={}):
        """Método que retorna todas as causas cadastradas
            Parameter
            ----------
              params: dict
                Dicionário com as configurações adicionais
        """

        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/cause/all', params=params)

    def get_all_categories(self, params={}):
        """Método que retorna todas as categorias cadastradas
              Parameter
              ----------
                params: dict
                  Dicionário com as configurações adicionais
        """

        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/cause/categories', params=params)

    def get_own_cause(self, params: dict):
        """Método que retorna todas as causas de uma loja
            Parameter
            ----------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/cause', params=params)

    # Company

    def get_company_detail(self, params: dict):
        """Método que retorna os detalhes de uma empresa
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/company/detail', params=params)

    def get_company_list(self, params: dict):
        """Método que retorna uma lista com as empresas de uma conta
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/company/list', params=params)

    def get_company_stores(self, params: dict):
        """Método que retorna uma lista de lojas de uma empresa
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
        """
        params['api_token'] = self.api_token
        return requests.get(f'{self.base_url}/company/stores', params=params)

    def update_company(self, body: dict, params: dict):
        """Método que atualiza uma empresa
            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.put(f'{self.base_url}/company/update', params=params, data=json.dump(body))

    def create_company(self, body: dict, params={}):
        """Método que cria uma nova empresa

            Parameter
            ---------
              params: dict
                Dicionário com as configurações adicionais
              body: dict
                Dicionário com o corpo da requisição
        """
        params['api_token'] = self.api_token
        return requests.post(f'{self.base_url}/company/update', params=params, json=body)
