import requests
import streamlit as st
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer

class Site(BaseModel):
    站點名稱:str = Field(alias="sna")
    行政區:str = Field(alias="sarea")
    日期時間:str = Field(alias="mday")
    地址:str = Field(alias="ar")
    總數:int = Field(alias="tot")
    可借:int = Field(alias="sbi")
    可還:int = Field(alias="bemp")
    狀態:bool = Field(alias="act")
    緯度:float = Field(alias="lat")
    經度:float = Field(alias="lng")

class Root(RootModel):
    root:list[Site]
    
@st.cache_data
def download_youbike() -> str:
    youbike_url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=2000"
    try:
        response = requests.get(youbike_url)
    except Exception as e:
        print(e)
    else:
        return response.text

data_str = download_youbike()
Root.model_