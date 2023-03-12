import azure.functions as func
import json

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:

    json_body = req.get_json()
    if json_body.get("shipperId") == None or json_body.get("shipperId")=="":
        return func.HttpResponse(json.dumps({"status":"400","message":"missing shipperId"}), status_code=400)
    elif json_body.get("Date") == None or json_body.get("Date") == "":
        return func.HttpResponse(json.dumps({"status":"400","message":"missing Date"}), status_code=400)
    elif json_body.get("WarehouseID") == None or json_body.get("WarehouseID") == "":
        return func.HttpResponse(json.dumps({"status":"400","message":"missing WarehouseID"}), status_code=400)
    elif json_body.get("ShippingPO") == None or json_body.get("ShippingPO") == "":
        return func.HttpResponse(json.dumps({"status":"400","message":"missing ShippingPO"}), status_code=400)
    elif json_body.get("ShipmentID") == None or json_body.get("ShipmentID") == "":
        return func.HttpResponse(json.dumps({"status":"400","message":"missing ShipmentID"}), status_code=400)
    elif json_body.get("BoxesRcvd") == None or json_body.get("BoxesRcvd") == "":
        return func.HttpResponse(json.dumps({"status":"400","message":"missing BoxesRcvd"}), status_code=400)


    request_body = req.get_body()
    
    doc.set(func.Document.from_json(request_body))

    return func.HttpResponse(json.dumps({"status":"200", "message":"Added shipment information successfully"}), status_code=200, mimetype="application/json" )
