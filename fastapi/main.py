from fastapi import FastAPI
import db

app = FastAPI()

@app.get('/')
async def root():
    return db.token

@app.get('/{token}')
async def check_token(token):
    tokens = db.token
    if token in tokens:
        return { 'Available': True, 'Token': token }
    else:
        return { 'Available': False, 'Token': token }
