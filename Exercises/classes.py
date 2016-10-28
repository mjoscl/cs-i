class Coin():
    __slots__ = ('coin_name', 'denomination')


dollar = Coin()
dollar.coin_name = "dollar"
dollar.denomination = 100

print(dollar.coin_name)
print(dollar.denomination)

print(dollar)