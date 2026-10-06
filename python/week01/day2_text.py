def parse_price_line(line):
    parts = line.split(",")
    if len(parts) != 3:
        raise ValueError(f"bad price line: {line}")
    return {
        "date": parts[0].strip(),
        "symbol": parts[1].strip(),
        "price": float(parts[2].strip())
            }
print(parse_price_line("hello"))
print(parse_price_line("2023-01-01, AAPL, 150.00"))