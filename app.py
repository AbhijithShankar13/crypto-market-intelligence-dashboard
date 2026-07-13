import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(layout="wide")

st.title("Crypto Market Intelligence Dashboard")

# ----------------------------
# Load Crypto Market Data
# ----------------------------

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency":"usd",
    "order":"market_cap_desc",
    "per_page":20,
    "page":1
}

response = requests.get(url,params=params)

data=response.json()

crypto_df=pd.DataFrame(data)

crypto_df=crypto_df[[
"name",
"symbol",
"current_price",
"market_cap",
"price_change_percentage_24h",
"total_volume"
]]

# ----------------------------
# Market KPI Section
# ----------------------------

st.subheader("Market Overview")

col1,col2,col3=st.columns(3)

top_gainer=crypto_df.loc[crypto_df["price_change_percentage_24h"].idxmax()]
top_loser=crypto_df.loc[crypto_df["price_change_percentage_24h"].idxmin()]

col1.metric("Top Gainer",top_gainer["name"],f'{top_gainer["price_change_percentage_24h"]:.2f}%')
col2.metric("Top Loser",top_loser["name"],f'{top_loser["price_change_percentage_24h"]:.2f}%')
col3.metric("Total Coins Analysed",len(crypto_df))

# ----------------------------
# Crypto Price Chart
# ----------------------------

st.subheader("Crypto Price Comparison")

fig1=px.bar(
crypto_df,
x="name",
y="current_price",
color="price_change_percentage_24h",
title="Top Cryptocurrency Prices"
)

st.plotly_chart(fig1,use_container_width=True)

# ----------------------------
# Market Heatmap
# ----------------------------

st.subheader("Crypto Market Overview")

fig2=px.scatter(
crypto_df,
x="market_cap",
y="current_price",
size="market_cap",
color="price_change_percentage_24h",
hover_name="name",
title="Crypto Market Heatmap"
)

st.plotly_chart(fig2,use_container_width=True)

# ----------------------------
# Bitcoin Historical Trend
# ----------------------------

st.subheader("Bitcoin Price Trend (30 Days)")

btc_url="https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

params={
"vs_currency":"usd",
"days":"30"
}

btc_data=requests.get(btc_url,params=params).json()

btc_df=pd.DataFrame(btc_data["prices"],columns=["timestamp","price"])

btc_df["timestamp"]=pd.to_datetime(btc_df["timestamp"],unit="ms")

fig3=px.line(btc_df,x="timestamp",y="price")

st.plotly_chart(fig3,use_container_width=True)

# ----------------------------
# News Data
# ----------------------------

news_url="https://newsapi.org/v2/everything"

params={
"q":"cryptocurrency OR bitcoin OR ethereum",
"language":"en",
"sortBy":"publishedAt",
"apiKey":st.secrets["NEWS_API_KEY"]
}

news=requests.get(news_url,params=params).json()

articles=news["articles"]

headlines=[article["title"] for article in articles if article["title"]]

# ----------------------------
# Sentiment Analysis
# ----------------------------

analyzer=SentimentIntensityAnalyzer()

results=[]

for text in headlines:

    score=analyzer.polarity_scores(text)["compound"]

    if score>0.05:
        sentiment="Positive"
    elif score<-0.05:
        sentiment="Negative"
    else:
        sentiment="Neutral"

    results.append({
    "headline":text,
    "score":score,
    "sentiment":sentiment
    })

sentiment_df=pd.DataFrame(results)

# ----------------------------
# Sentiment Distribution
# ----------------------------

st.subheader("Market Sentiment Distribution")

sentiment_counts=sentiment_df["sentiment"].value_counts()

fig4=px.pie(
values=sentiment_counts.values,
names=sentiment_counts.index
)

st.plotly_chart(fig4,use_container_width=True)

# ----------------------------
# Sentiment Gauge
# ----------------------------

st.subheader("Sentiment Indicator")

avg_sentiment=sentiment_df["score"].mean()

fig5=go.Figure(go.Indicator(
mode="gauge+number",
value=avg_sentiment,
title={"text":"Market Sentiment"},
gauge={
"axis":{"range":[-1,1]},
"steps":[
{"range":[-1,-0.2],"color":"red"},
{"range":[-0.2,0.2],"color":"gray"},
{"range":[0.2,1],"color":"green"}
]
}
))

st.plotly_chart(fig5,use_container_width=True)

# ----------------------------
# Trading Signal Engine
# ----------------------------

st.subheader("Trading Signal")

if avg_sentiment>0.2:
    signal="BUY"
elif avg_sentiment<-0.2:
    signal="SELL"
else:
    signal="HOLD"

st.metric("Market Signal",signal)

# ----------------------------
# News Display
# ----------------------------

st.subheader("Latest Crypto News")

for headline in headlines[:10]:
    st.write("•",headline)

# ----------------------------
# Data Download
# ----------------------------

st.subheader("Download Data")

st.download_button(
"Download Crypto Data",
crypto_df.to_csv(index=False),
"crypto_data.csv"
)

st.download_button(
"Download Sentiment Data",
sentiment_df.to_csv(index=False),
"sentiment_data.csv"
)