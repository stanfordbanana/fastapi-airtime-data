from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()

class AirtimeAcceptRequest(BaseModel):
    merchantReference: str
    quotationId: str
    reference: str


class DataAcceptRequest(BaseModel):
    merchantReference: str
    quotationId: str
    reference: str

@app.get("/")
def root():
    return {"message":"FastAPI Airtime and Data API"}



@app.get("/airtime/quote/")
async def get_airtime_quote(
    productname: str,
    amount: float,
    receivernumber: str
):
 
    return {"productname": productname, "amount": amount, "receivernumber": receivernumber}




@app.post("/airtime/accept/")
async def accept_airtime_quote(airtime_accept_request: AirtimeAcceptRequest = Body(...)):
    
    return {"status": "success"}


@app.get("/data/quote/")
async def get_data_quote(
    productname: str,
    amount: float,
    receivernumber: str):
 
    return {"productname": productname, "amount": amount, "receivernumber": receivernumber}


@app.post("/data/accept/")
async def accept_data_quote(airtime_data_request: DataAcceptRequest = Body(...)):
    
    return {"status": "success"}

