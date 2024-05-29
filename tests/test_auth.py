import aiohttp
import pytest

from aioselectel_api.client import AuthClient
from testing import Env

env = Env()
env.read_env('.env')


@pytest.mark.asyncio
async def test_authenticate_success():
    base_url = 'https://cloud.api.selcloud.ru'
    username = env('SELECTEL_USERNAME')
    account_id = env('SELECTEL_ACCOUNT_ID')
    password = env('SELECTEL_PASSWORD')
    project_name = 'My First Project'

    client = AuthClient(base_url=base_url)
    result = await client.authenticate(
        username=username, account_id=account_id, password=password,
        project_name=project_name
    )

    assert result != ''
    assert client.token != ''


@pytest.mark.asyncio
async def test_get_container_options():
    base_url = 'https://cloud.api.selcloud.ru'
    username = env('SELECTEL_USERNAME')
    account_id = env('SELECTEL_ACCOUNT_ID')
    password = env('SELECTEL_PASSWORD')
    project_name = 'My First Project'

    client = AuthClient(base_url=base_url)
    keystone_token = await client.authenticate(
        username=username, account_id=account_id, password=password,
        project_name=project_name
    )

    headers = {
        'X-Auth-Token': keystone_token
    }

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.ru-1.storage.selcloud.ru/v2/containers/private-insighter-1/options',
                               headers=headers) as response:
            print(response.status)
            assert response.status == 200
