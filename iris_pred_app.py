import streamlit as st

ps = st.navigation(
    [
       st.Page("pages\page1.py",title="IRIS品種預測",icon="🌺" ), #path , title 圖示 有點像首頁的感覺
       st.Page("pages\page2.py",title="IRIS樣本分布",icon="🔮" ) #path , title 圖示
    ]
)

ps.run()
