import json
from typing import Any, Union
from fastapi import FastAPI
from logging import getLogger
logger = getLogger(__file__)
from pydantic import BaseModel, Field
import datetime
import time

app = FastAPI()


@app.post("/")
async def root():
    return {"Message": "Hello World"}
