import os
import requests

PRODIA_API = os.environ["PRODIA_API"]


class Prodia:

    def __init__(self):
        self.url = "https://api.prodia.com/v1/sd/generate"
        self.url_img = "https://api.prodia.com/v1/job/"

    def create(self, prompt: str):
        payload = {
            "model": "absolutereality_V16.safetensors [37db0fc3]",
            "prompt": f"{prompt}",
            "negative_prompt": "badly drawn",
            "steps": 25,
            "cfg_scale": 7,
            "seed": -1,
            "upscale": False
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": f"{PRODIA_API}"
        }

        response = requests.post(self.url, json=payload, headers=headers)

        print(response.text)

        return response.text

    def download(self, n_job: str):
        url = f"{self.url_img}{n_job}"

        headers = {
            "accept": "application/json",
            "X-Prodia-Key": f"{PRODIA_API}"
        }

        response_img = requests.get(url, headers=headers)

        print(response_img.text)

        return response_img
