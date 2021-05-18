from flask import Flask, request, jsonify
db = {"1": 25, "2": 30, "3": 40, "4": 38, "5": 27,
      "6": 2, "7": 39, "8": 60, "9": 58, "180199": 77}
app = Flask(__name__)


@app.route('/coins', methods=['POST'])
def check():
    data = request.json
    rn = data["rollno"]
    return jsonify({"coins": db[str(rn)]})


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)


