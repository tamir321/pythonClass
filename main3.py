_str = "asdasdasdaifhhsdfhgiu3769kecnjkssiwwer"

amount = {}

for ch in _str:
    amount[ch] = amount.get(ch,0)+1

print(amount)