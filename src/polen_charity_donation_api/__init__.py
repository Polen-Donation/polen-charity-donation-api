import requests
import json

class PolenCharityDonationAPI:
    base_url = 'https://api.polen.com.br/api/v2'

    def __init__(self, api_token: str):
        self.api_token = api_token

