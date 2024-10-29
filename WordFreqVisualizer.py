import streamlit as st
import myTextMining as tm
import mySTVisualizer as stv
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from matplotlib import font_manager, rc
from wordcloud import WordCloud

#font_path = 'C:/Windows/Fonts/malgun.ttf'
#font_name = font_manager.FontProperties(fname=font_path).get_name()
#rc('font', family=font_name)

st.set_page_config(
    page_title="Word Frequency Visualizer",
    page_icon="📊",
    #layout="wide"
    #initial_sidebar_state="expanded"
)

@st.dialog("분석할 데이터 확인")
def view_raw_data(data_file):
    df = pd.read_csv(data_file)
    num_line = 10
    st.write(df.head(num_line))
    
with st.sidebar:    
    st.write('## 영화 키워드 분석 메뉴')
    filename = st.file_uploader("분석할 파일", type=['csv'])
    if filename:
        if st.button("분석할 데이터 보기"):
            view_raw_data(filename)
        col = st.text_input("분석할 컬럼")
        with st.form('my_form'):
            freq = st.checkbox('빈도수 그래프')
            freq_num = st.slider('단어수', 10, 30, 20, 1)
            wordcloud = st.checkbox('워드클라우드')
            wc_num = st.slider('단어수', 50, 1000, 50, 10)
            
            submitted = st.form_submit_button('분석 시작')
        
if submitted:
    status = st.info('분석중입니다.')
    #filename = '../daum_movie_review.csv'
    counter = tm.analyze_word_freq(filename, col)
    
    if counter:
        status.info('분석이 완료되었습니다.')
        if freq: stv.visualize_barhgraph(counter, freq_num)
        if wordcloud: stv.visualize_wordcloud(counter, wc_num)
        
    else:
        status.error('분석에 실패했습니다.')
