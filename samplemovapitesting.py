

import os

from datetime import date, datetime, timedelta
import statsmodels.api as sm
#from datetime import datetime
import json
import argparse
from pydantic.schema import model_schema
import uvicorn
import logging
import sys
import fastapi


import movementsamplemodspitest 
import ErrorCode
from typing import List, Optional, Set
from pydantic import BaseModel
from logging.handlers import TimedRotatingFileHandler

#C:\Users\212775463\Desktop\Valvaware Dev\main.py
# FastAPI and self-hosting REST API locally and/or offline
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request, status, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from movementsamplemodspitest import movementfunc
from ErrorCode import errorCode

import simplejson


import datetime

import pandas as pd
import os
import traceback
import ast
import re
import runpy

import logging
logger = logging.getLogger(__name__)

app = FastAPI(debug=True)
@app.post("/mov/")
async def movfunction( input : str = Form(...),config : str =Form(...)):

     try:

          input_json = ast.literal_eval(input)
          config_json = ast.literal_eval(config)
          
          minMove = config_json["Movement_Config"]["Min_Move"]
          maxMove = config_json["Movement_Config"]["Max_Move"]

          input_json.update({"MinMove":minMove, "MaxMove":maxMove})
          result = movementfunc(input_json,config_json)
          if isinstance(result, dict):


                         return {"response_code": 200, "result_":{"Movement_API":result}, "cd rrors":""}

          else:
                         
                         ErrMessage = errorCode().obtain_errorCode(result)
                         logger.warning({"Error":ErrMessage, "Valve_id": input_json["Valve_id"]})
                         return {"response_code": 204, "result_":"", "errors":[{"code":result, "message":"Movement API : " + ErrMessage }]}
          

     except Exception as error:

               logger.error({"Execution Error": str(traceback.format_exc())})
               return {"response_code": 204, "result_":"", "errors":[{"code":3888, "message":"Python execution error"}]}

         
     
 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)