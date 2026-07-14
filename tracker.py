# Simple Python Finance Tracker
# Zero-cost wealth tool
import json
from datetime import datetime

def track_transaction(amount, category, note=''):
    data = {'date': datetime.now().isoformat(), 'amount': amount, 'category': category, 'note': note}
    try:
        with open('transactions.json', 'r+') as f:
            txns = json.load(f)
            txns.append(data)
            f.seek(0)
            json.dump(txns, f)
    except:
        with open('transactions.json', 'w') as f:
            json.dump([data], f)
    print('Tracked:', data)

# Example
if __name__ == '__main__':
    track_transaction(100, 'income', 'Freelance template sale')