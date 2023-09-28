import streamlit as st

count = 0

# ページ描画
st.markdown("## マークダウンもかける")

# 関数定義
# チェックボタン
check = st.checkbox("見てみる？")
if check:
    count += 10

    # スライダー
    slider = st.slider("slider", 0, 100, count)
    if slider > 80:
        st.markdown("でかすぎ！！！")

    if slider < 10:
        st.markdown("ちっちゃくない？")
