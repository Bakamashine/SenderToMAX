import asyncio
import json
from datetime import datetime
from typing import Dict, List

from pymax import SocketMaxClient, MaxClient
from pymax.payloads import UserAgentPayload

# @dataclass
# class Days:
#     date: str
#     description: str

dateFormat = "%d.%m.%y"
currentDate = datetime.today().strftime(dateFormat)

message = ""

# ManagementProjectAndEconomicSectorId = -68641740619999
NeedId = -73608632930884
# Danill = 68504030
ua = UserAgentPayload(device_type="WEB", app_version="25.12.13")
phoneNumber = "+79805307554"
client = MaxClient(phone=phoneNumber, headers=ua, work_dir="cache")


def print_array(arr) -> None:
    for n in arr:
        print(f"\t{n} id: {n.id}")


def print_all(current_client: SocketMaxClient):
    # client.me                   # Информация о себе (Me)
    # client.is_connected         # Статус подключения (bool)
    # client.chats                # Список всех чатов (list[Chat])
    # client.dialogs              # Список диалогов (list[Dialog])
    # client.channels             # Список каналов (list[Channel])
    # client.phone                # Номер телефона (str)
    # client.token                # Токен сессии (str | None)
    # client.contacts             # Список контактов (list[User])

    print("Информация обо мне: ")
    print(f"ID {current_client.me.id}")
    print(f"Account status: {current_client.me.account_status}")
    print(f"Phone: {current_client.me.phone}")
    print(f"Update time: {current_client.me.update_time}")
    print(f"Names: {current_client.me.names}")
    print(f"Connect status: {current_client.is_connected}")
    print("Все чаты: ")
    print_array(current_client.chats)
    print("Все диалоги: ")
    print_array(current_client.dialogs)
    print("Все каналы: ")
    print_array(current_client.channels)
    print("Все контакты: ")
    print_array(current_client.contacts)


@client.on_start
async def on_start() -> None:
    print_all(client)
    if message:
        await client.send_message(message, NeedId)
        await client.close()
    else:
        raise Exception("Сообщение не сформировано.")


async def main():
    await client.start()

def debug_message(text: str) -> None:
    with open("debug.txt", "w") as f:
        f.write(text)
    exit(1)

if __name__ == "__main__":
    with open("./exercise.json", "r", encoding='utf-8') as file:
        themes: List[Dict[str, str]] = json.loads(file.read())

    print(f"themes: {themes}")

    for item in themes:
        if currentDate == item.get('date'):
            message = f'Здравствуйте. К практике приступил с 10:00, работаю над темой "{item.get('description')}"'
            break
    if len(message) == 0:
        message = "Здравствуйте. Сегодня продолжаю делать прошлую тему."
    print(f"Message result: {message}")
    print(f"Current date to day: {currentDate}")
    print()

    # debug_message(message)
    asyncio.run(main())
