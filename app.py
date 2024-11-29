from flask import Flask, jsonify, request

app = Flask(__name__)

# テスト用のクーポンデータ
coupons = {
    "12345": {"status": "unused", "pin": "6789"}
}

@app.route("/api/check_coupon", methods=["GET"])
def check_coupon():
    coupon_id = request.args.get("coupon_id")
    if coupon_id in coupons:
        return jsonify({"status": coupons[coupon_id]["status"]})
    return jsonify({"error": "Coupon not found"}), 404

@app.route("/api/use_coupon", methods=["POST"])
def use_coupon():
    data = request.json
    coupon_id = data.get("coupon_id")
    pin = data.get("pin")
    if coupon_id in coupons and coupons[coupon_id]["pin"] == pin:
        coupons[coupon_id]["status"] = "used"
        return jsonify({"message": "Coupon used successfully"})
    return jsonify({"error": "Invalid coupon or pin"}), 400

if __name__ == "__main__":
    app.run(debug=True)
