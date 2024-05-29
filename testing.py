import asyncio

from environs import Env

from aioselectel_api.client import SelectelStorageClient, get_token

env = Env()
env.read_env('.env')

BASE_URL = 'https://cloud.api.selcloud.ru'
username = env('SELECTEL_USERNAME')
password = env('SELECTEL_PASSWORD')
account_id = env('SELECTEL_ACCOUNT_ID')


async def main():
    keystone_token = await get_token(username=username, password=password, account_id=account_id,
                                     project_name='My First Project')
    async with SelectelStorageClient(keystone_token=keystone_token, container_name='links') as client:
        print(await client.get_pubdomains())
        print(await client.get_containers_settings())


if __name__ == '__main__':
    asyncio.run(main())
