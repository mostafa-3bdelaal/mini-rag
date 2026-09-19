# =====================================================================
# This is the entry point of the FastAPI application.
# It creates the app instance and connects it to the routers
# defined inside the routes/ folder
# =====================================================================

from fastapi import FastAPI
import motor
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings


app=FastAPI()

@app.on_event("startup") # Once the app starts, this function will be called to connect to the MongoDB database
async def startup_db_client(): 
    
    settings = get_settings()
    app.mong_connect = AsyncIOMotorClient(settings.MONGODB_URI)  
    app.db_client = app.mong_connect[settings.MONGODB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mong_connect.close()


app.include_router(base.base_router)
app.include_router(data.data_router)