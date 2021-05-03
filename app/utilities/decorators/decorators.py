from functools import wraps
from werkzeug.exceptions import InternalServerError, BadRequest, NotFound, Unauthorized

from app.utilities.utils.utils import json_response


def api_resource_endpoint():
    """
    Wrapper function to handle API endpoint
    :param logger: DB logger to save a log record
    :param error_code: Int, Custom http error code. Ie, 500
    :param is_view: Bool, the endpoint is a view (lendingportal) or not ?. Ie, False
    :return decorator_function: the decorator itself
    """

    def wrapper_function(function):
        """
        Decorator used in API endpoints to handle the exceptions possibly raised
        :param function: function to be decorated. Function
        :return decorator_function: the decorator itself
        """

        @wraps(function)
        def decorator_function(*args, **kwargs):

            try:
                return function(*args, **kwargs)

            except Unauthorized as e:
                return json_response(e.description, e.code)

            except NotFound as e:
                return json_response(e.description, e.code)

            except BadRequest as e:
                return json_response(e.description, e.code)

            except InternalServerError as e:
                return json_response(e.description, e.code)

            except Exception as e:
                raise e

        return decorator_function

    return wrapper_function
