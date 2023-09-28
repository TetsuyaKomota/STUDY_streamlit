import numpy as np
import pandas as pd
import streamlit as st

dataframe = pd.DataFrame(np.random.randn(5, 20))
st.dataframe(dataframe)  # pandasのデータフレーム
st.table(dataframe)  # 静的な表
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")  # 指標
