def parse_price_line(line):
    parts = line.split(",")
    if len(parts) != 3:
        raise ValueError(f"bad price line: {line}")
    return {
        "date": parts[0].strip(),
        "symbol": parts[1].strip(),
        "price": float(parts[2].strip())
            }
print(parse_price_line("2023-01-01, AAPL, 150.00"))
def simple_return(prices):
    returns = []
    for i in range (1, len(prices)):
      returns.append(prices[i] / prices[i-1] - 1)
    return returns
def parse_price_lines(lines):
    return [parse_price_line(line) for line in lines]
def group_prices_by_symbol(rows):
    groups = {}
    for row in rows:
        symbol = row["symbol"]
        price = row["price"]
        if symbol in groups:
            groups[symbol].append(price)
        else:
            groups[symbol] = [price]
    return groups

rows = [
    {"date": "2023-01-01", "symbol": "AAPL", "price": 150.0},
    {"date": "2023-01-01", "symbol": "MSFT", "price": 240.0},
    {"date": "2023-01-02", "symbol": "AAPL", "price": 153.0},
]
def top_words(text, n):
    counts = {}
    for word in text.lower().split():
        word = word.strip(",.!?;")
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    pairs = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    return pairs[:n]

 
print(simple_return([100, 110, 120]))
print(parse_price_lines(["2023-01-01, AAPL, 150.00", "2023-01-02, AAPL, 153.00"]))
print(group_prices_by_symbol(rows))
print(top_words("the cat saw the dog and the bird", 3))