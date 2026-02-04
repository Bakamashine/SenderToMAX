from pymax import SocketMaxClient
from pymax.payloads import UserAgentPayload
import asyncio
from datetime import datetime

dateFormat = "%d"
currentDate = datetime.today().strftime(dateFormat)

themes = {
    "04": "Разработка технического задания",
    "05": "Проектирование интерфейса",
    "06": "Разработка интерфейса",
    "07": "Разработка меню",
    "08": "Создание информационного контента приложения",
    "09": "Форматирование контента приложения",
    "10": "Разработка адаптивного дизайна приложения",
    "11": "Разработка формы обратной связи",
    "12": "Оценка качества и надёжности приложения",
    "13": "Составление отчётной документации",
}
message = ""

ManagementProjectAndEconomicSectorId = -68641740619999
NeedId = -70723001985604
Danill = 68504030
ua = UserAgentPayload(device_type="DESKTOP", app_version="25.12.13")
phoneNumber = "+79805307554"
client = SocketMaxClient(phone=phoneNumber, headers=ua, work_dir="cache")


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
    print("Все каналы: ")
    printArray(client.channels)
    print("Все контакты: ")
    printArray(client.contacts)


@client.on_start
async def on_start() -> None:
    printAll(client)
    if message:
        await client.send_message(message, NeedId)
        await client.close()
    else:
        raise Exception("Сообщение не сформировано.")


async def main():
    await client.start()


if __name__ == "__main__":
    for index, item in themes.items():
        if currentDate == index:
            message = f'Здравствуйте. К практике приступил с 9:00 по 14:00, работаю над темой "{item}"'
            break
    if len(message) == 0:
        message = "Здравствуйте. Сегодня продолжаю делать прошлую тему."
    print(f"Message result: {message}")
    print(f"Current date to day: {currentDate}")
    print()
    asyncio.run(main())
