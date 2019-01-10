stock_dict = {
    'GM': 'General Motors',
    'CAT':'Caterpillar',
    'EK':"Eastman Kodak",
    'GE':"General Electric",
     }

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ('GM', 200, '11-sep-2007', 35),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ('GM', 50, '4-apr-1987', 53),
    ('EK', 450, '37-apr-1987', 13),
    ( 'GE', 200, '1-jul-1998', 56 )
    ]

report = {}
for purchase in purchases:
    abbrev = purchase[0]
    full_name = stock_dict[abbrev]
    shares_cost = purchase[1] * purchase[3]
    purchase_date = purchase[2]
    print(f"I purchased {full_name} stock on {purchase_date} for ${shares_cost}")
    try:
        report[abbrev].append(purchase)
    except KeyError:
        report[abbrev] = list()
        report[abbrev].append(purchase)

for abbrev, purchases in report.items():
    print(f"-----{abbrev}------")
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print(f"{purchase}")
    print(f"total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")


