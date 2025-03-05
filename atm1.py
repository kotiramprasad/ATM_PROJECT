from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variables to store PIN and balance
pin = 1819
balance = 5000

@app.route('/')
def home():
    return render_template('atm1.html')

@app.route('/atm', methods=['POST'])
def atm():
    global pin, balance
    try:
        data = request.get_json()
        action = data.get('action')
        entered_pin = int(data.get('pin'))

        if entered_pin != pin:
            return jsonify({"error": "Invalid PIN"})

        if action == "login":
            return jsonify({"message": "Login successful"})

        elif action == "balance_enquiry":
            return jsonify({"message": f"Your balance is: ₹{balance}"})

        elif action == "withdraw":
            amount = int(data.get('amount', 0))
            if amount <= 0:
                return jsonify({"error": "Invalid withdrawal amount"})
            if amount > balance:
                return jsonify({"error": "Insufficient balance"})
            balance -= amount
            return jsonify({"message": f"Withdrawal successful. Remaining balance: ₹{balance}"})

        elif action == "change_pin":
            new_pin = int(data.get('new_pin'))
            confirm_pin = int(data.get('confirm_pin'))
            if new_pin != confirm_pin:
                return jsonify({"error": "PINs do not match"})
            pin = new_pin
            return jsonify({"message": "PIN successfully changed"})

        elif action == "thank_you":
            return jsonify({"message": "Thank you for using the ATM!"})

        else:
            return jsonify({"error": "Invalid action"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
