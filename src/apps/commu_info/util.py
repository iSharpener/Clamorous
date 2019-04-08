def json_response(status, msg, data={}):
    resp = dict(
        meta = dict(
            status = status,
            msg = msg,
        ),
        data = data
    )
    return resp