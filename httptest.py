# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    a: int = None
    b: int = None

@app.get('/')
def index():
    return {'message': '你已经正确创建 FastApi 服务！'}


@app.post('/test')
def cal(request_data: Item):
    a = request_data.a
    b = request_data.b
    c = a + b
    res = {"res": c}
    return res


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
