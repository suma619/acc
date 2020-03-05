from chalice import Chalice
from chalicelib.Controller import controller
app = Chalice(app_name='ZEE5_CHALICE')


@app.on_s3_event(bucket="zee5transcoding-news-staging",events=['s3:ObjectCreated:*'])
#@app.route('/')
def index(event):

	#print("our first chalce deployemnet handler is triggereed")
	#calling controller
	print("recieved event")
	controller.controller(event)
	return {'hello': 'world'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
