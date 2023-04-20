import re
from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


class KeyNameInNewKeyCommand(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, str]:
        name: str = str()
        name += message.text
        name = re.sub(r'\/\w+\s', '', name)
        if name.casefold() == ('/new_key'):
            name = ''

        if name:
            return {'name': name}
        return {'name': None}
