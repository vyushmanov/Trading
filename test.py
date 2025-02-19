from pybit.unified_trading import HTTP
session = HTTP(testnet=True)
print(session.get_kline(
    category="linear",
    symbol="BTCUSD",
    interval=30,
    start=1582070803000,
    end=1582106803000,
))