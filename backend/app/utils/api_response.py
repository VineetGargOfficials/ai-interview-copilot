def success_response(data):
    return {
        "sucess": True,
        "data": data
    }

def failure_response(data):
    return {
        "sucess": False,
        "data": data
    }