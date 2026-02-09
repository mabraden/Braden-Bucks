import json
import hashlib

LEDGER_FILE = "ledger.json"

def load_ledger():
    with open(LEDGER_FILE, "r") as f:
        return json.load(f)

def save_ledger(data):
    with open(LEDGER_FILE, "w") as f:
        json.dump(data, f, indent=2)

def hash_transaction(tx):
    tx_string = f"{tx['from']}{tx['to']}{tx['amount']}"
    return hashlib.sha256(tx_string.encode()).hexdigest()

def add_transaction(sender, receiver, amount):
    ledger = load_ledger()
    balances = ledger["balances"]

    if balances.get(sender, 0) < amount:
        print("Transaction rejected: insufficient funds.")
        return

    balances[sender] -= amount
    balances[receiver] = balances.get(receiver, 0) + amount

    tx = {"from": sender, "to": receiver, "amount": amount}
    tx["hash"] = hash_transaction(tx)

    ledger["transactions"].append(tx)
    save_ledger(ledger)
    print("Transaction approved and recorded with hash.")

add_transaction("Braden","Paolo",15)
