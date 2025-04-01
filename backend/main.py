from flask import Flask, request, jsonify
from googleapiclient.discovery import build
import os

app = Flask(__name__)

# Google Sheets API credentials (Replace with your actual details)
SHEET_ID = os.getenv("1g-9dJwYXMGdFoTzKIvTj809KllZUe9jw3kw1MPw25HE")
API_KEY = os.getenv("AIzaSyCkYITy6-zB8b9Uo5VVFqLTjrVqmF24qZA")

def get_google_sheet_service():
    service = build('sheets', 'v4', developerKey=API_KEY)
    return service

@app.route('/expenses', methods=['GET'])
def get_expenses():
    service = get_google_sheet_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range="Sheet1").execute()
    values = result.get('values', [])
    return jsonify(values)

@app.route('/add-expense', methods=['POST'])
def add_expense():
    data = request.json
    amount, category, description = data.get("amount"), data.get("category"), data.get("description")

    if not amount or not category:
        return jsonify({"error": "Amount and category are required!"}), 400

    new_expense = [[amount, category, description]]
    service = get_google_sheet_service()
    sheet = service.spreadsheets()
    sheet.values().append(
        spreadsheetId=SHEET_ID,
        range="Sheet1",
        valueInputOption="USER_ENTERED",
        body={"values": new_expense}
    ).execute()

    return jsonify({"message": "Expense added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
