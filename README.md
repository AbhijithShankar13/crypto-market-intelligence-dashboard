# Crypto Market Intelligence Dashboard

## Overview

The **Crypto Market Intelligence Dashboard** is an interactive Business Intelligence application developed as part of an MSc Business Analytics **Product Development Project** at the University of Greenwich.

The application integrates real-time cryptocurrency market information with cryptocurrency news sentiment analysis to provide users with a consolidated view of current market conditions.

The dashboard combines:

- Real-time cryptocurrency market data
- Cryptocurrency news headlines
- Automated sentiment analysis
- Interactive data visualisations
- Market sentiment indicators
- Rule-based BUY, HOLD and SELL signals
- Downloadable market and sentiment data

The purpose of the product is to reduce information fragmentation by bringing quantitative market information and qualitative news sentiment together within a single analytical environment.

## Live Application

The live version of the dashboard is available here:

**https://crypto-market-intelligence-dashboard-ee24b7k6rkok8dq8vfjm9o.streamlit.app/**

## Project Objectives

The project was developed to demonstrate how Business Intelligence, Natural Language Processing and real-time data integration can be combined to support cryptocurrency market analysis.

The main objectives are to:

1. Integrate real-time cryptocurrency market data using the CoinGecko API.
2. Collect recent cryptocurrency news using NewsAPI.
3. Apply VADER sentiment analysis to cryptocurrency news headlines.
4. Develop an interactive Business Intelligence dashboard using Streamlit and Plotly.
5. Generate transparent BUY, HOLD and SELL signals based on aggregated sentiment.
6. Provide users with an accessible environment for monitoring cryptocurrency market conditions.
7. Evaluate the functionality and practical feasibility of the developed prototype.

## Key Features

### Market Overview

The dashboard retrieves the top 20 cryptocurrencies according to market capitalisation and displays:

- Cryptocurrency name
- Symbol
- Current price
- Market capitalisation
- 24-hour price change
- Total trading volume

The Market Overview section also identifies:

- Top-performing cryptocurrency based on 24-hour percentage change
- Lowest-performing cryptocurrency based on 24-hour percentage change
- Total number of cryptocurrencies analysed

### Cryptocurrency Price Comparison

An interactive Plotly bar chart presents cryptocurrency prices for the selected market dataset.

The chart allows users to compare current prices visually while also considering 24-hour price performance.

### Market Visualisation

A Plotly scatter chart is used to visualise relationships between:

- Market capitalisation
- Current cryptocurrency price
- 24-hour percentage change

The size and position of each point provide a visual representation of market characteristics.

### Bitcoin Historical Trend

The dashboard retrieves approximately 30 days of Bitcoin historical price data from CoinGecko and displays the results using an interactive time-series chart.

This allows users to observe recent Bitcoin price movements and trends.

### Cryptocurrency News

The application retrieves recent English-language news articles using NewsAPI.

The current news search includes:

```text
cryptocurrency OR bitcoin OR ethereum
