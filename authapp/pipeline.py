import urllib
from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.conf import settings
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from GeekShop.settings import BASE_DIR
from authapp.models import ShopUserProfile, ShopUser


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_max_orig')),
                                                access_token=response['access_token'],
                                                v='5.124')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.about_me = data['about']

    if data['photo_max_orig']:

        urllib.request.urlretrieve(data['photo_max_orig'], f'{settings.MEDIA_ROOT}/users_avatars/{user.pk}.jpg')
        user.avatar = f'users_avatars/{user.pk}.jpg'

        # get_photo = requests.get(data['photo_200'])
        # with open(f'{BASE_DIR}/media/users_avatars/{user.id}.jpg', 'wb') as photo:
        #     photo.write(get_photo.content)
        # user.avatar = f'users_avatars/{user.id}.jpg'

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    user.save()

