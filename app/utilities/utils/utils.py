import json
from flask import Response


def json_response(data, status=200):
    """
    Prepare data and make the response
    :param data: dict, contains the data that is going in he response
    :param status: integer, code status. Ie, 200
    :return: Response, the response object to return
    """

    data_as_str = json.JSONEncoder().encode(data)
    return Response(response=data_as_str, status=status, mimetype='application/json')
