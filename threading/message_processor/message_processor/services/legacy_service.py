import requests

class LegacyService:
  def __init__(self, url):
    self.service_url = url
  def register_user(self, user):
    response = requests.post(self.service_url, json=user)
    return response.json()
  def get_user_status(self, user_id):
    response = requests.get(f'{self.service_url}/{user_id}')
    user_status = response.json()
    print(f'User current status is {user_status}')
    return response.json()['user']