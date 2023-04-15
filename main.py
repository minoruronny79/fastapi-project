from fastapi import FastAPI

app=FastAPI()

def root ():
    return {"message":"Hello world"}

