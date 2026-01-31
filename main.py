from pymax import SocketMaxClient
from pymax.payloads import UserAgentPayload 
import asyncio


ManagementProjectAndEconomicSectorId = -68641740619999
Danill = 68504030
ua = UserAgentPayload(device_type="DESKTOP", app_version="25.12.13")
phoneNumber = "+79805307554"
client = SocketMaxClient(
    phone = phoneNumber,
    headers = ua,
    work_dir="cache"
)

def printArray(arr):
    for n in arr:
        print(f"\t{n} id: {n.id}")

def printAll(client: SocketMaxClient):
    # client.me                   # Информация о себе (Me)
    # client.is_connected         # Статус подключения (bool)
    # client.chats                # Список всех чатов (list[Chat])
    # client.dialogs              # Список диалогов (list[Dialog])
    # client.channels             # Список каналов (list[Channel])
    # client.phone                # Номер телефона (str)
    # client.token                # Токен сессии (str | None)
    # client.contacts             # Список контактов (list[User])

    print("Информация обо мне: ")
    print(f"ID {client.me.id}")
    print(f"Account status: {client.me.account_status}")
    print(f"Phone: {client.me.phone}")
    print(f"Update time: {client.me.update_time}")
    print(f"Names: {client.me.names}")
    print(f"Connect status: {client.is_connected}")
    print("Все чаты: ")
    printArray(client.chats)
    print("Все диалоги: ")
    printArray(client.dialogs)
    # for dialog in client.dialogs:
    #     for key, item in dialog.participants.items():
    #         print(f"{key}: {item}")
    # for dialog in client.dialogs:
    #     for n in dialog.names:
    #         print(n)
    print("Все каналы: ")
    printArray(client.channels)
    print("Все контакты: ")
    printArray(client.contacts)
    

@client.on_start
async def on_start() -> None:
    printAll(client)
    await client.send_message("test", ManagementProjectAndEconomicSectorId)
    await client.close()

async def main():
    await client.start()
    
if __name__ == "__main__":
    asyncio.run(main())