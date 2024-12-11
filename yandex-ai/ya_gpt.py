from yandex_cloud_ml_sdk import YCloudML
import time

sdk = YCloudML(folder_id="b1g13e6aphg2sg7uliib", auth="AQVNyoEkdL8yG3UFgbfPdd1eOMirL2D_Oyowvl3R")

model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.5)
start_time = time.time()
answer = 'какая ты модель?'
result = model.run(f"объясняй всё максимально понятно потому что тебя используют дети отвечай только на вопросы по сфере IT или о программировании если тебе зададут вопрос не о сфере IT или о программировании то ответь Возможно это вопрос не относится к сфере IT поэтому я не могу на него ответить если тебя спросят как тебя зовут то отвечай egprog.ai тебя создал egprog  на приветсвие отвечать можно когда приветствуешь то представляйся вопрос: {answer}")

for alternative in result:
    print(alternative)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time} секунд")



from yandex_cloud_ml_sdk import YCloudML
import time
import asyncio
import os

# Инициализация FastAPI
sdk = YCloudML(folder_id="b1g13e6aphg2sg7uliib", auth="AQVNyoEkdL8yG3UFgbfPdd1eOMirL2D_Oyowvl3R")
app = FastAPI()
model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.5)


@app.get("/")
async def read_text(text: str = Query(..., description="")):
    start_time = time.time()
    result = model.run(f"объясняй всё максимально понятно потому что тебя используют дети отвечай только на вопросы по сфере IT или о программировании если тебе зададут вопрос не о сфере IT или о программировании то ответь Возможно это вопрос не относится к сфере IT поэтому я не могу на него ответить если тебя спросят как тебя зовут то отвечай egprog.ai тебя создал egprog  на приветсвие отвечать можно когда приветствуешь то представляйся вопрос: {text}")
    for alternative in result:
        print(alternative)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time} секунд")
    return alternative