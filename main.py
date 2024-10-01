from flask import Flask, jsonify, request

app = Flask(__name__)

dealership_data = [
    {
        "Dealer_Name": "Bhuvan Maruti",
        "Brands": "Maruti",
        "Serviceable_Pin_Codes": ["132114"],
        "Cities": "Jalna"
    },
    {
        "Dealer_Name": "K S Motors Private Limited - M I Road",
        "Brands": "Mahindra",
        "Serviceable_Pin_Codes": [
            "679576", "302012", "302021", "302029", "303005", "303104", 
            "303120", "303338", "303804", "303908", "303906", "303330",
            "302009", "303339", "303703", "302031", "302036", "302005",
            "302018", "302026", "303002", "303012", "303109", "303305",
            "303601", "303712", "303903", "303308", "303907", "302014",
            "303802", "303902", "302052", "302030", "302002", "302015",
            "302023", "303122", "302039", "303106", "303302", "303022",
            "303806", "303340", "303324", "303116", "303209", "302037",
            "302053", "302032", "302011", "302020", "302028", "303119",
            "303331", "303603", "303803", "303905", "303111", "303309",
            "302008", "303608", "303607", "302004", "302017", "302025",
            "303001", "303009", "303706", "303611", "303010", "302010",
            "303606", "303349", "302035", "302001", "302013", "302022",
            "302040", "302033", "303006", "303105", "303348", "303701",
            "303805", "302060", "303306", "303115", "303118", "303307",
            "302034", "302051", "302055", "302006", "302019", "302027",
            "303003", "303102", "303110", "303329", "303602", "303801",
            "303904", "303101", "303113", "302007", "303117", "303314",
            "302003", "302016", "302024", "302054", "303107", "303704",
            "303807", "303011", "303609", "303114", "303112", "303121",
            "303119", "303331"
        ],
        "Cities": ["Dausa", "Jaipur", "Kotputli", "Jhalawar"]
    },
    {
        "Dealer_Name": "Model Fuels Private Limited. - धनसार",
        "Brands": "Mahindra",
        "Serviceable_Pin_Codes": [
            "826013", "828311", "828105", "828101", "828110", "828119", "828128", 
            "828201", "828302", "826124", "828107", "828115", "828206", "828130", 
            "828144", "826003", "828103", "828112", "828121", "828131", "828203", 
            "828304", "826015", "828109", "828117", "828127", "828142", "828301", 
            "828309", "828124", "826005", "828106", "828114", "828123", "828133", 
            "828205", "828306", "828504", "826001", "828102", "828111", "828120", 
            "828129", "828202", "828303", "828402", "826012", "826014", "828108", 
            "828116", "828126", "828135", "828207", "828308", "826004", "828104", 
            "828113", "828132", "828204", "828305"
        ],
        "Cities": "Dhanbad"
    },
    {
        "Dealer_Name": "Bhakra Hyundai",
        "Brands": "Hyundai",
        "Serviceable_Pin_Codes": ["122108", "140124", "524201"],
        "Cities": "Baddi, Nangal, Una"
    },
    {
        "Dealer_Name": "Bhakra Hyundai",
        "Brands": "Hyundai",
        "Serviceable_Pin_Codes": ["140118"],
        "Cities": "Anandpur Sahib"
    },
    {
        "Dealer_Name": "Bhakra Hyundai",
        "Brands": "Hyundai",
        "Serviceable_Pin_Codes": [
            "140115", "140126", "140101", "140112", "140123", "140307", 
            "140117", "140114", "140125", "140001", "140111", "140119", 
            "140108", "140116", "140133", "140102", "140113"
        ],
        "Cities": "Rupnagar"
    }
]

@app.route('/verify_dealer', methods=['GET'])
def verify_dealer():
    dealer_name = request.args.get('dealer_name')
    for dealer in dealership_data:
        if dealer['Dealer_Name'].lower() == dealer_name.lower():
            return jsonify({'status': 'found', 'dealer': dealer}), 200
    return jsonify({'status': 'not found'}), 404

@app.route('/verify_brand', methods=['GET'])
def verify_brand():
    brand_name = request.args.get('brand')
    result = [dealer for dealer in dealership_data if dealer['Brands'].lower() == brand_name.lower()]
    if result:
        return jsonify({'status': 'found', 'dealers': result}), 200
    return jsonify({'status': 'not found'}), 404

@app.route('/verify_pincode', methods=['GET'])
def verify_pincode():
    pin_code = request.args.get('pincode')
    for dealer in dealership_data:
        if pin_code in dealer['Serviceable_Pin_Codes']:
            return jsonify({'status': 'found', 'dealer': dealer}), 200
    return jsonify({'status': 'not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)