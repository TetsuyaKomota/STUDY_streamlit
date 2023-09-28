import numpy as np
import pandas as pd
import streamlit as st

dataframe = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# 線グラフ
st.line_chart(dataframe)

# チャート
st.area_chart(dataframe)

# 棒グラフ
st.bar_chart(dataframe)
