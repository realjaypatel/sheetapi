from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, Path, Request, status,Query
import json
import database
import pandas as pd
import numpy as np
templates = Jinja2Templates(directory="templates")














router = APIRouter(
    # prefix='/',
    tags=['home']
)


@router.get('/', status_code=status.HTTP_200_OK)
async def return_home(request: Request):

    


    return templates.TemplateResponse("home.html", {"request": request})

@router.get('/api/{custom_string}', status_code=status.HTTP_200_OK)
async def return_home(custom_string,gid: str = Query(None), id: str = Query(None)):
    try:
        id = custom_string

        r = (f'https://docs.google.com/spreadsheets/d/{id}/export?format=csv')

        if gid:
            r = (f'https://docs.google.com/spreadsheets/d/{id}/export?format=csv&gid={gid}')
        print('step: 1')
        data = pd.read_csv(r)
        data = data.fillna('')
        print('step: 2')
        print('data',data)
        data.replace([np.inf, -np.inf], np.nan, inplace=True)
        data = data.to_dict(orient='records')

        return JSONResponse(content=data)
    except :
        return {'status':'error while loading Data'}



