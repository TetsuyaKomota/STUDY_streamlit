import streamlit as st

# タイトル
st.title("サンプルタイトル")

# ヘッダー
st.header("ヘッダー")

# マークダウンで表示
st.markdown("## マークダウンもかける")
st.markdown(
    """
### 概要
- hogehoge
- hogehoge
"""
)

st.markdown("## いろんなウィジェットが使える")

# チェックボタン
check = st.checkbox("見てみる？")

if check:
    # ボタン
    st.button("button")

    # セレクトボックス
    st.selectbox("selectbox", ("select1", "select2"))

    # 複数選択可能なセレクトボックス
    st.multiselect("multiselectbox", ("select1", "select2"))

    # ラジオボタン
    st.radio("radiobutton", ("radio1", "radio2"))

    # 文字入力(1行)
    st.text_input("text input")

    # 文字入力(複数行)
    st.text_area("text area")

    # スライダー
    slider = st.slider("slider", 0, 100, 50)
    if slider > 80:
        st.markdown("でかすぎ！！！")

    if slider < 10:
        st.markdown("ちっちゃくない？")

    # ファイルアップロード
    st.file_uploader("Choose file")
