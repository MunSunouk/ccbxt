from ccdxt.base.async_support.exchange import Exchange

if __name__ == "__main__" :

    exchange = Exchange()
    
    print(setattr(exchange, 'rateLimit',1000))
    print(getattr(exchange, 'rateLimit'))