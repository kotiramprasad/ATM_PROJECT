# ATM Interface

This project simulates an ATM (Automated Teller Machine) interface using a web-based application. The application includes features such as login, balance enquiry, withdrawal, PIN change, and logout. It is implemented with HTML, CSS, JavaScript, and Flask (Python).

---

## Features

1. **Login**
   - Users enter their 4-digit PIN to access the main menu.

2. **Balance Enquiry**
   - Users can view their current account balance.

3. **Withdraw**
   - Users can withdraw a specified amount if their balance is sufficient.

4. **Change PIN**
   - Users can update their PIN by entering a new PIN and confirming it.

5. **Logout**
   - Users can log out and receive a "Thank You" message.

---

## Technologies Used

### Frontend
- **HTML**: Structure of the web pages.
- **CSS**: Styling for a user-friendly interface.
- **JavaScript**: Dynamic behavior and interaction with the backend.

### Backend
- **Flask**: Python web framework for handling server-side logic.

---

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies:**
   Ensure you have Python installed. Then, install Flask:
   ```bash
   pip install flask
   ```

3. **Run the Application:**
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the Interface:**
   Open a browser and navigate to `http://127.0.0.1:5000/`.

---

## File Structure

- **`templates/atm1.html`**: The frontend HTML file for the ATM interface.
- **`app.py`**: The Flask backend for handling API requests.

---

## API Endpoints

### POST `/atm`

- **Request Body:**
  ```json
  {
    "action": "<action>",
    "pin": "<pin>",
    "amount": "<amount>" (optional),
    "new_pin": "<new_pin>" (optional),
    "confirm_pin": "<confirm_pin>" (optional)
  }
  ```

- **Actions:**
  - `login`: Verify PIN and grant access.
  - `balance_enquiry`: Return the current account balance.
  - `withdraw`: Deduct the specified amount from the balance.
  - `change_pin`: Update the user PIN.
  - `thank_you`: Display a thank-you message.

- **Responses:**
  - Success:
    ```json
    {
      "message": "<success-message>"
    }
    ```
  - Error:
    ```json
    {
      "error": "<error-message>"
    }
    ```

---

## Example Workflow

1. **Login:**
   - Enter a valid PIN (default: `1819`).

2. **Balance Enquiry:**
   - View your balance (default: ₹5000).

3. **Withdraw:**
   - Enter an amount to withdraw.
   - Ensure the balance is sufficient.

4. **Change PIN:**
   - Enter and confirm a new PIN.

5. **Logout:**
   - End the session and display a "Thank You" message.

---

## Customization

- **Default PIN:**
  - Modify the `pin` variable in `app.py`.

- **Default Balance:**
  - Modify the `balance` variable in `app.py`.

---

## Future Enhancements

- Add support for multiple users.
- Implement session management for enhanced security.
- Include transaction history tracking.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Author
Developed by [koti ram prasad].
