
import fasttext
from pythainlp import word_tokenize
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model = ''

# def word_predict(text,topn=4):
#     global model
#     text = ' '.join(word_tokenize(text))
#     obj = model.predict(text, k=topn)
#     l = []
#     for i in range(0,topn):
#         label = obj[0][i]
#         score = obj[1][i]
#         l.append({'label':label, 'score':score})
#     return l

@app.get("/")
def main():
    return 'Hello wellcome to yama-service'

# @app.get("/load")
# def load_model():
#     global model
#     model = fasttext.load_model('test.model')
#     return True

# @app.get("/predict")
# def predict(text:str="อยากสอบถามร้าน มีเบอร์ให้ติดต่อไหม", topn:int=3):
#     global model
#     result = word_predict(text, topn)
#     return result
