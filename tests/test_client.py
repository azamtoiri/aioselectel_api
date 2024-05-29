import asyncio

from aioselectel_api import SelectelStorageClient


async def test_get_account_info():
    async with SelectelStorageClient(keystone_token='your_keystone_token', project_id='your_project_id') as client:
        account_info = await client.get_account_info()
        assert 'X-Account-Container-Count' in account_info


async def test_list_containers():
    async with SelectelStorageClient(keystone_token='your_keystone_token', project_id='your_project_id') as client:
        containers = await client.list_containers()
        assert isinstance(containers, str)  # Assuming the response is a string list of containers


async def test_set_account_metadata():
    async with SelectelStorageClient(keystone_token='your_keystone_token', project_id='your_project_id') as client:
        response = await client.set_account_metadata({'Test': 'Value'})
        assert response is None  # Assuming successful metadata setting returns no content


async def main():
    await test_get_account_info()
    await test_list_containers()
    await test_set_account_metadata()


if __name__ == '__main__':
    asyncio.run(main())
