import pandas as pd
from konlpy.tag import Komoran
import streamlit as st
from collections import Counter

def load_data(filename, col):
    review_df = pd.read_csv(filename)
    review_df = review_df.dropna()
    review_corpus = list(review_df[col])
    return review_corpus

def tokenize_data(corpus):
    komo = Komoran()
    my_tags = ['NNG', 'NNP', 'VA']
    my_stopwords = ['없', '같', '많', '영화', '좋', '안', '!!']
    result_tokens = []
    
    for doc in corpus:
        tokens = [word for word, tag in komo.pos(doc) if tag in my_tags and word not in my_stopwords]
        result_tokens.extend(tokens)
        
    return result_tokens

@st.cache_data
def analyze_word_freq(filename, col):
    review_corpus = load_data(filename, col)
    review_tokens = tokenize_data(review_corpus)
    
    return Counter(review_tokens)

def generate_wordcloud(counter, num_words, font_path):
        # 워드클라우드 시각화
    from wordcloud import WordCloud

    # WordCloud 객체 생성
    wordcloud = WordCloud(
        font_path = font_path,
        #max_font_size = 200,
        width = 800, #이미지 너비 지정
        height = 600, #이미지 높이 지정
        max_words=num_words,
        background_color='ivory' #이미지 배경색 지정
    )
    wordcloud=wordcloud.generate_from_frequencies(counter)
    return wordcloud