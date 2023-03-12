import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    params = req.params
    # if shipperId == "" or shipperId == None:
    if "shipperId" not in params:
        return func.HttpResponse(
        json.dumps({"status":"400","message":"Bad request: no shipperId provided"}),
        status_code=400,
        mimetype="application/json")

    try: 
        users_json = []
        for shipment in doc:
            user_json = {
            "Date": shipment['Date'],
            "WarehouseID": shipment['WarehouseID'],
            "ShippingPO": shipment['ShippingPO'],
            "ShipmentID": shipment['ShipmentID'],
            "BoxesRcvd" : shipment['BoxesRcvd']
            }
            users_json.append(user_json)
        
        response = {"Received":users_json}

        if users_json == []:
            return func.HttpResponse(
                json.dumps({"status":"201","message":"No shipment whose shipperId matches the provided shipperId"}),
                status_code=401,
                mimetype="application/json")
                
        return func.HttpResponse(
                json.dumps({"status":"200", "message":response}),
                status_code=200,
                mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"status":"500", "message":str(e)}),
            status_code = 500,
            mimetype="application/json"
        )

