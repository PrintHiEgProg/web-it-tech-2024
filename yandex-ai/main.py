import uvicorn
from yandex_cloud_ml_sdk import YCloudML
import time
from fastapi import FastAPI, Request
import requests
from fastapi.middleware.cors import CORSMiddleware

sdk = YCloudML(folder_id="b1g13e6aphg2sg7uliib", auth="AQVNyoEkdL8yG3UFgbfPdd1eOMirL2D_Oyowvl3R")
app = FastAPI()
model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.5)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)


@app.post("/sendNotification")  
async def process_text(request: Request):
    # Получаем данные из запроса
    try:
        data = await request.json()
    except Exception as e:
        return {"error": "Invalid JSON in request body"}

    text = data.get("text")
    print(data)
    print(data['text'])

    # Открываем файл joined.txt и читаем его содержимое
    try:
        with open("joined.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return {"error": "File 'joined.txt' not found"}

    # Извлекаем id из каждой строки и выводим через print
    for line in lines:
        # Убираем лишние пробелы и символы переноса строки
        id_value = line.strip()
        # Проверяем, что строка не пустая
        if id_value:
            print(id_value)
            chat_id = id_value
            url = f'https://api.telegram.org/bot7970877206:AAGKEo257rO7-oj3tLMck50hixrJ8XPTgow/sendMessage?chat_id={chat_id}&text={text}'
            data = {
                'text': text,
            }
            response = requests.post(url, json=data)

    return {"message": "IDs printed successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7270)