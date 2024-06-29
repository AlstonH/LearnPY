import requests
import streamlit as st
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import source
from source import Root
import pandas as pd

try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))
        
    def area_change():
        sarea_name = st.session_state.sarea
        display_data = []
        for item in data:
            if item['行政區'] == sarea_name:
                display_data.append(item)
        
        st.title("新北市youbike各行政區站點資料")
        col1, col2 = st.columns([1, 6])
    
        with col1:
            st.subheader(sarea_name)
            
        with col2:
            df1 = pd.DataFrame(display_data,
                                columns=['站點名稱','日期時間','地址','總數','可借','可還','經度','緯度'])
            st.dataframe(data=df1)
        
        tableContainer = st.container()    
        with tableContainer:
            df0 = pd.DataFrame(display_data,
                                columns=['站點名稱','總數'])
            st.scatter_chart(df0,
                            x='站點名稱',
                            y='總數',
                            color='#00ff00',
                            size='總數')
            df2 = pd.DataFrame(display_data,
                                columns=['站點名稱','總數','可借'])
            st.scatter_chart(df2,
                            x='站點名稱',
                            y='可借',
                            color='#800080',
                            size='可借')
            df3 = pd.DataFrame(display_data,
                                columns=['站點名稱','總數','可還'])
            st.scatter_chart(df3,
                            x='站點名稱',
                            y='可還',
                            size='可還')

        
    with st.sidebar:
        st.selectbox(":purple[請選擇行政區:]",options=areas,on_change=area_change,key='sarea')
    
