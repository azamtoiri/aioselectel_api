from abc import ABC, abstractmethod


class IClient(ABC):
    @abstractmethod
    async def authenticate(self, *args, **kwargs):
        ...
