import asyncio

from environs import Env

from aioselectel_api.client import get_token, SelectelLogsClient

env = Env()
env.read_env('.env')

BASE_URL = 'https://cloud.api.selcloud.ru'
username = env('SELECTEL_USERNAME')
password = env('SELECTEL_PASSWORD')
account_id = env('SELECTEL_ACCOUNT_ID')


async def main():
    keystone_token = await get_token(username=username, password=password, account_id=account_id,
                                     project_name='My First Project')
    # async with SelectelStorageClient(keystone_token=keystone_token, container_name='links') as client:
    #     print(await client.get_pubdomains())
    #     print(await client.get_containers_settings())

    async with SelectelLogsClient(keystone_token=keystone_token) as client:
        task = {
            "data": {
                "container": "links",
                "delete_after": 0,
                # "fields": [
                #     ""
                # ],
                # "filters": {
                #     "additionalProp1": {},
                #     "additionalProp2": {},
                #     "additionalProp3": {}
                # },
                # "provider": "",
                "since": "2024-05-30T06:00:00",
                "till": "2024-05-30T06:00:00"
            },
            # "type": ""

        }
        await client.create_logs_task(task)
        print(await client.get_logs_task_info('12466c12-4301-4051-9fa4-d4f0b2860c33'))


if __name__ == '__main__':
    asyncio.run(main())
