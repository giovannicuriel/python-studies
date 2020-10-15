def build_legacy_service(requests, url):
  class LegacyService:
    def register_user(self, user):
      response = requests.post(url, json=user)
      return response.json()['result']
    def get_user_status(self, user_id):
      response = requests.get(f'{url}/{user_id}')
      user_status = response.json()
      print(f'User current status is {user_status}')
      return response.json()['result']
  return LegacyService
