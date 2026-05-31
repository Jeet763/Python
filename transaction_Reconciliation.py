bank = [
    ("TXN1",500),
    ("TXN2",1000),
]

gateway = [
    ("TXN1",500),
    ("TXN2",1200),
    ("TXN3",700)
]

bank_dict = dict(bank)
gateway_dict = dict(gateway)

# Output- bank_dict = {
#     "TXN1": 500,
#     "TXN2": 1000
# }

# gateway_dict = {
#     "TXN1": 500,
#     "TXN2": 1200,
#     "TXN3": 700
# }

mismatched_amounts = []
missing_transactions = []
extra_transactions = []


for txn_id, amount in bank_dict.items():
    if txn_id not in gateway_dict:
        missing_transactions.append((txn_id, amount))
    elif amount != gateway_dict[txn_id]:
        mismatched_amounts.append(
    (txn_id, amount, gateway_dict[txn_id])
         )

for txn_id, amount in gateway_dict.items():
    if txn_id not in bank_dict:
        extra_transactions.append((txn_id, amount))

print('mismatched_amounts:', mismatched_amounts)
print('missing_transactions:',missing_transactions)
print('extra_transactions:',extra_transactions)