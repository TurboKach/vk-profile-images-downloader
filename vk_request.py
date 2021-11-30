import os

import dotenv
import requests

dotenv.load_dotenv()


class VkRequest:
    BASE_URL = 'https://api.vk.com/method'
    API_V = '5.131'
    ACCESS_TOKEN = os.getenv('VK_ACCESS_TOKEN')
    USER_ID = os.getenv('USER_ID', 0)

    params = {
        'access_token': ACCESS_TOKEN,
        'v': API_V,
    }

    @classmethod
    def photos_get_albums(cls, user_id=USER_ID):
        method = 'photos.getAlbums'
        params = cls.params
        params['owner_id'] = user_id
        params['need_system'] = 1
        response = requests.get(f'{cls.BASE_URL}/{method}', params=params)
        return response.json()

    @classmethod
    def photos_get(cls, user_id=USER_ID):
        method = 'photos.get'
        params = cls.params
        params['owner_id'] = user_id
        response = requests.get(f'{cls.BASE_URL}/{method}', params=params)
        return response.json()

    @classmethod
    def photos_get_all(cls, user_id=USER_ID):
        method = 'photos.getAll'
        params = cls.params
        params['owner_id'] = user_id
        response = requests.get(f'{cls.BASE_URL}/{method}', params=params)
        return response.json()

    @classmethod
    def photos_get_wall_photos(cls, user_id=USER_ID, limit=None, offset=0):
        method = 'photos.get'
        params = cls.params
        params['owner_id'] = user_id
        params['album_id'] = 'wall'
        params['offset'] = offset
        params['count'] = limit
        params['photo_sizes'] = 1
        response = requests.get(f'{cls.BASE_URL}/{method}', params=params)
        return response.json()
