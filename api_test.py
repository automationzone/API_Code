from flask import Flask, request, jsonify
import datetime
from enum import Enum

app = Flask(__name__)


@app.route('/', methods=['POST'])
def parse_json():
    data = request.get_json()  # Parse JSON data from the request
    # Process the parsed JSON data as needed
    response = process_json(data)

    # Return a response with the processed data
    return jsonify(response)


def process_json(data):
    # Perform operations on the JSON data
    # ...
    # For example, let's assume we want to return the sum of two numbers

    data["Comment"] = ""
    respose = RunLotSizeRule(data)
    if type(respose) is str: data["Comment"] = respose
    respose = RunValidSymbolRule(data)
    if type(respose) is str: data["Comment"] = f"{respose} | {data['Comment']}"
    respose = RunPriceRule(data)
    if type(respose) is str: data["Comment"] = f"{respose} | {data['Comment']}"
    respose = badPriceRejectRule(data)
    if type(respose) is str: data["Comment"] = f"{respose} | {data['Comment']}"

    if data["Comment"] =="":
        data["RequestType"] = "NEW_ORDER_CONFIRM"
        data["OrderID"] = "some rules Can be discussed to generate this"
    else:
        data["RequestType"] = "REJECT"
    data["TimeStamp"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    processed_request = data

    return processed_request


def RunLotSizeRule(data):
    product = data.get('Symbol')
    minimum_lot_size = getMinLotSize(product)
    return True if float(data.get('Quantity')) % minimum_lot_size == 0 else "Quantity is not in multiple of lot size"

def getMinLotSize(product):
    # this data will be come from some database or third part app
    # for now lets hard code it as 5
    return 5

def RunValidSymbolRule(data):
    valid_sybmol = ["vod.l", "appl.l", "IFEU.BRN"] # this data will be come from some database or third part app
    return True if data.get('Symbol') in valid_sybmol else "Not a valid MDSymbol"

def RunPriceRule(data):
    product = data.get('Symbol')
    threshold_price = getThreasholdPrice(product)
    return True if float(data.get('Price')) < threshold_price else "Price is above the Threshold"

def getThreasholdPrice(product):
    # this data will be come from some database or third part app
    # for now lets hard code it as 5
    return 160

def badPriceRejectRule(data):
    return True if float(data.get('Price')) != "123" else "Price values 123 is prohibited"


if __name__ == '__main__':
    app.run()


