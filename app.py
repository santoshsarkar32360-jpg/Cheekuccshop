from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

STORE_NAME = "cheekuccshop"
UPI_URL = "upi://pay?pa=7505961211@fam&pn=Rekha&cu=INR"

CARDS_DB = {
    1: {"id": 1, "type": "VISA", "price": 100, "number": "4111 8392 0192 1234", "exp": "08/28", "cvv": "482", "limit": "2,800", "name": "ARJUN YADAV"},
    2: {"id": 2, "type": "MC", "price": 150, "number": "5368 7965 1152 5678", "exp": "12/27", "cvv": "591", "limit": "3,299", "name": "MANISH TIWARI"},
    3: {"id": 3, "type": "RUPAY", "price": 420, "number": "6522 8810 5512 9012", "exp": "05/29", "cvv": "304", "limit": "12,500", "name": "SACHIN DESHMUKH"},
    4: {"id": 4, "type": "VISA", "price": 250, "number": "4532 7810 9921 3456", "exp": "10/26", "cvv": "129", "limit": "7,500", "name": "RAHUL SHARMA"},
    5: {"id": 5, "type": "MC", "price": 300, "number": "5412 7534 8819 7890", "exp": "03/30", "cvv": "782", "limit": "15,000", "name": "AMIT VERMA"},
    6: {"id": 6, "type": "RUPAY", "price": 500, "number": "6071 9923 4412 1122", "exp": "11/28", "cvv": "615", "limit": "25,000", "name": "VIKAS GUPTA"},
    7: {"id": 7, "type": "VISA", "price": 180, "number": "4222 1098 3341 3344", "exp": "01/27", "cvv": "934", "limit": "5,000", "name": "ROHIT KUMAR"},
    8: {"id": 8, "type": "MC", "price": 220, "number": "5555 4321 8876 5566", "exp": "07/29", "cvv": "248", "limit": "8,500", "name": "DEEPAK SINGH"},
    9: {"id": 9, "type": "RUPAY", "price": 350, "number": "6082 1190 5533 7788", "exp": "09/28", "cvv": "512", "limit": "10,000", "name": "AMAN GUPTA"},
    10: {"id": 10, "type": "VISA", "price": 400, "number": "4761 9082 1122 9900", "exp": "04/31", "cvv": "863", "limit": "18,000", "name": "SUNIL CHOUDHARY"},
    11: {"id": 11, "type": "MC", "price": 450, "number": "5105 3342 9988 1213", "exp": "02/27", "cvv": "409", "limit": "20,000", "name": "MANOJ VERMA"},
    12: {"id": 12, "type": "RUPAY", "price": 600, "number": "6521 7788 4433 1415", "exp": "06/30", "cvv": "175", "limit": "30,000", "name": "VIJAY PATEL"},
    13: {"id": 13, "type": "VISA", "price": 120, "number": "4155 8890 2211 1617", "exp": "08/29", "cvv": "328", "limit": "3,500", "name": "KAVITA SHARMA"},
    14: {"id": 14, "type": "MC", "price": 280, "number": "5390 1123 7766 1819", "exp": "12/28", "cvv": "694", "limit": "9,000", "name": "POOJA YADAV"},
    15: {"id": 15, "type": "RUPAY", "price": 320, "number": "6060 4455 3322 2021", "exp": "10/27", "cvv": "841", "limit": "11,500", "name": "ANIL KUMAR"},
    16: {"id": 16, "type": "VISA", "price": 550, "number": "4916 3322 1100 2223", "exp": "03/32", "cvv": "537", "limit": "28,000", "name": "SANDEEP GARG"},
    17: {"id": 17, "type": "MC", "price": 700, "number": "5255 9988 7744 2425", "exp": "05/29", "cvv": "902", "limit": "35,000", "name": "RAKESH MEENA"},
    18: {"id": 18, "type": "RUPAY", "price": 850, "number": "6083 2211 5566 2627", "exp": "11/30", "cvv": "216", "limit": "45,000", "name": "DINESH KUMAR"},
    19: {"id": 19, "type": "VISA", "price": 950, "number": "4000 5544 3322 2829", "exp": "01/31", "cvv": "768", "limit": "50,000", "name": "MANISH AGARWAL"},
    20: {"id": 20, "type": "MC", "price": 1000, "number": "5433 2211 9988 3031", "exp": "09/32", "cvv": "459", "limit": "75,000", "name": "RAJESH SINGH"}
}

@app.route('/')
def index():
    masked_cards = []
    for cid, card in CARDS_DB.items():
        c = card.copy()
        c['cvv'] = c['cvv'][:-1] + "*"
        c['exp'] = c['exp'][:-1] + "*"
        masked_cards.append(c)

    return render_template('index.html', store_name=STORE_NAME, upi_url=UPI_URL, cards=masked_cards)

@app.route('/verify_utr', methods=['POST'])
def verify_utr():
    data = request.json
    utr = data.get('utr')
    card_id = data.get('card_id')
    
    if utr and len(utr) >= 10 and int(card_id) in CARDS_DB:
        actual_card = CARDS_DB[int(card_id)]
        return jsonify({
            "status": "success", 
            "message": "Payment verified successfully!", 
            "card": actual_card
        })
    return jsonify({"status": "error", "message": "Invalid UTR or Card ID!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
