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
