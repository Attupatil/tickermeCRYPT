import streamlit as st

try:
    import datetime
    import matplotlib.pyplot as plt
    import plotly.express as px
    import yfinance as yf
    from yahoo_fin import stock_info
    from PIL import Image
    import pandas as pd
    from pandas_datareader import data as pdr
    import plotly.graph_objs as ago


except ModuleNotFoundError as e:
    st.error(
        f"Looks like requirements are not installed: '{e}'. Run the following command to install requirements"
    )

    st.code(
        "pip install streamlit matplotlib yfinance yahoo_fin pillow pandas"
    )
else:

    def Nifty50():

        with st.sidebar:
            st.write("Nifty50 Inputs")
            symbol = st.selectbox("Select Symbol",stock_info.tickers_nifty50())
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            

        cdata = yf.download(tickers=symbol, start=a, end=b)
        tickerData = yf.Ticker(symbol)
        string_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(string_logo, unsafe_allow_html=True)
        string_name = tickerData.info['longName']
        st.header('**%s**' % string_name)
        
        
        fig = ago.Figure()


        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))

        fig.update_layout(title=' live share price evolution',yaxis_title='Stock Price (INR per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)
        string_summary = tickerData.info['longBusinessSummary']
        st.info(string_summary)
    

    def DOW():

        with st.sidebar:
            st.write("DOW Inputs")
            symbol = st.selectbox("Select Symbol",stock_info.tickers_dow())
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            

        cdata = yf.download(tickers=symbol, start=a, end=b)
        tickerData = yf.Ticker(symbol)
        string_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(string_logo, unsafe_allow_html=True)
        string_name = tickerData.info['longName']
        st.header('**%s**' % string_name)
        
        
        fig = ago.Figure()


        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))

        fig.update_layout(title=' live share price evolution',yaxis_title='Stock Price (INR per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)
        string_summary = tickerData.info['longBusinessSummary']
        st.info(string_summary)

    def NSE():

        with st.sidebar:
            st.write("NSE Inputs")
            tickers = pd.read_html('https://ournifty.com/stock-list-in-nse-fo-futures-and-options.html#:~:text=NSE%20F%26O%20Stock%20List%3A%20%20%20%20SL,%20%201000%20%2052%20more%20rows%20')[0]
            tickers = tickers.SYMBOL.to_list()
            for count in range(len(tickers)):
                tickers[count] = tickers[count]
            symbol = st.selectbox("Select Symbol", tickers)
            
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            # from_date = st.date_input(
            #     "From date", datetime.date.today() - datetime.timedelta(30)
            # )

            # to_date = st.date_input("To Date", datetime.date.today())

        cdata = yf.download(tickers=symbol  + ".NS", start=a, end=b)
        # Ticker information
        tickerData = yf.Ticker(symbol + ".ns")
        string_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(string_logo, unsafe_allow_html=True)
        string_name = tickerData.info['longName']
        st.header('**%s**' % string_name)
        
        
        fig = ago.Figure()

        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))

        fig.update_layout(title='live share price evolution',yaxis_title='Stock Price (INR per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)
        string_summary = tickerData.info['longBusinessSummary']
        st.info(string_summary)
        

    def NASDAQ():

        with st.sidebar:
            st.write("NASDAQ Inputs")
            symbol = st.selectbox("Select Symbol",stock_info.tickers_nasdaq())
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            # from_date = st.date_input(
            #     "From date", datetime.date.today() - datetime.timedelta(30)
            # )

            # to_date = st.date_input("To Date", datetime.date.today())

        cdata = yf.download(tickers=symbol, start=a, end=b)
        tickerData = yf.Ticker(symbol)
        string_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(string_logo, unsafe_allow_html=True)
        string_name = tickerData.info['longName']
        st.header('**%s**' % string_name)
        



        fig = ago.Figure()


        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))

        fig.update_layout(title='live share price evolution',yaxis_title='Stock Price (USD per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)
        string_summary = tickerData.info['longBusinessSummary']
        st.info(string_summary)

        

    def SNP500():

        with st.sidebar:
            st.write("SNP500 Inputs")
            symbol = st.selectbox("Select Symbol",stock_info.tickers_sp500())
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            # from_date = st.date_input(
            #     "From date", datetime.date.today() - datetime.timedelta(30)
            # )

            # to_date = st.date_input("To Date", datetime.date.today())

        cdata = yf.download(tickers=symbol, start=a, end=b)
        tickerData = yf.Ticker(symbol)
        string_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(string_logo, unsafe_allow_html=True)
        string_name = tickerData.info['longName']
        st.header('**%s**' % string_name)
        



        fig = ago.Figure()


        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))

        fig.update_layout(title='live share price evolution',yaxis_title='Stock Price (USD per Shares)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)
        string_summary = tickerData.info['longBusinessSummary']
        st.info(string_summary)

        
    def DIV():

        with st.sidebar:
            st.write("DIV Inputs")
            symbol = "NASDAQ"
            segment = st.selectbox("Select Stock exchange", ["NASDAQ", "SNP500","DOW","NSE"])
            if segment == "NASDAQ":
                symbol = st.selectbox("Select Symbol",stock_info.tickers_nasdaq())
                dd=stock_info.get_dividends(symbol)
                
            elif segment == "SNP500":
                symbol = st.selectbox("Select Symbol",stock_info.tickers_sp500())
                dd=stock_info.get_dividends(symbol)
                
            elif segment == "DOW":
                symbol = st.selectbox("Select Symbol",stock_info.tickers_dow())
                dd=stock_info.get_dividends(symbol)
                
            else:
                tickers = pd.read_html('https://ournifty.com/stock-list-in-nse-fo-futures-and-options.html#:~:text=NSE%20F%26O%20Stock%20List%3A%20%20%20%20SL,%20%201000%20%2052%20more%20rows%20')[0]
                tickers = tickers.SYMBOL.to_list()
                for count in range(len(tickers)):
                    tickers[count] = tickers[count]
                symbol = st.selectbox("Select Symbol", tickers)
                symbol = symbol + '.ns'
                tickerDdd = yf.Ticker(symbol)
                dd=tickerDdd.dividends


        tickerData = yf.Ticker(symbol)
        string_logo = '<img src=%s>' % tickerData.info['logo_url']
        st.markdown(string_logo, unsafe_allow_html=True)
        string_name = tickerData.info['longName']
        st.header('**%s**' % string_name)
        

        st.write(dd)   
        string_summary = tickerData.info['longBusinessSummary']
        st.info(string_summary) 
                

    def crypto_display():

        with st.sidebar:
            st.write("Crypto Inputs")
            symbol = st.selectbox("Select Symbol",stock_info.get_top_crypto())
            a = st.date_input("From date", datetime.date.today() - datetime.timedelta(30)) 
            b = st.date_input("To Date", datetime.date.today())

            # from_date = st.date_input(
            #     "From date", datetime.date.today() - datetime.timedelta(30)
            # )

            # to_date = st.date_input("To Date", datetime.date.today())

        cdata = yf.download(tickers=symbol, start=a, end=b)
        tickerData = yf.Ticker(symbol)
        string_name = tickerData.info['shortName']
        st.header('**%s**' % string_name)
        

        fig = ago.Figure()
        fig.add_trace(ago.Candlestick(x=cdata.index,open=cdata['Open'],high=cdata['High'],low=cdata['Low'],close=cdata['Close'], name = 'market data'))
        fig.update_layout(title=f'{symbol} live share price evolution',yaxis_title='Stock Price (USD per Shares)')
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")])))
        st.write(fig)
        string_summary = tickerData.info['description']
        st.info(string_summary)

    analysis_dict = {
        "Nifty50": Nifty50,
        "NSE Stock Delivery": NSE,
        # __________________
        "Crypto": crypto_display, 
        "NASDAQ": NASDAQ,
        "SNP500": SNP500,
        "DOW": DOW,
        "DIVIDENDS": DIV,
    }

    with st.sidebar:
        image = Image.open('logo.jpg')
        st.image(image, caption='By TickerMe financial solutions')
        st.markdown('<h1 style="float: left;">WITH LOVE :)</h1>',unsafe_allow_html=True,)
        selected_analysis = st.radio("Select Analysis", list(analysis_dict.keys()))
        st.write("---")

    st.header(selected_analysis)

    analysis_dict[selected_analysis]()
