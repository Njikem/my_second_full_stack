from flask import Flask, request, make_response, jsonify
import dbhelpers, apihelpers, dbcreds

app = Flask(__name__)

#client Post Request
app.post("/api/client")
def post_client():
    error =apihelpers.check_endpoint_info(request.json, ["username", "email", "password", "image_url"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedure("call get_client(?,?)", [request.json.get("username"),request.json.get("email"),request.json.get("password"),request.json.get("image_url")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"), 500)

#Login post request
@app.post("/api/login")
def post_login():
    error =apihelpers.check_endpoint_info(request.json, ["username", "password"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedure("call get_login (?,?)", [request.json.get("username"),request.json.get("password")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"), 500)
    
#Delete login
@app.delete("/api/delete")
def delete_login():
    error = apihelpers.check_endpoint_info(request.json, ["token"])
    if(error != None):
        return error
    results = dbhelpers.run_procedure('call delete_token(?)', [request.json.get('token')])
    if(type(results) == list and results[0][0] == 1):
        return json.dumps(results, default=str)
    else:
        return "sorry, something went wrong"
    
    #Client get request
@app.get("/api/client")
def get_client():
    results = dbhelpers.run_procedure("call get_client(?,?,?,?,?)", ["id", "username", "email", "image_url", "bio"])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("sorry, something went wrong"), 500)
    

    
    app.run(debug=True)