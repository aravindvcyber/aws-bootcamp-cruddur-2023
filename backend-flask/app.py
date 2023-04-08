from flask import Flask
from flask import request

from flask_cors import CORS, cross_origin
import os
import sys
import uuid
from services.users_short import *
from services.home_activities import *
from services.notifications_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *

from lib.cognito_jwt_token import CognitoJwtToken, extract_access_token, TokenVerifyError
# HoneyComb ---------
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
# HoneyComb ---------
# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
# Show this in the logs within the backend-flask app (STDOUT)
# simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
# provider.add_span_processor(simple_processor)

trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

from time import strftime
# CloudWatch Logs ----

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
LOGGER.addHandler(console_handler)

import watchtower

cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(cw_handler)

# X-RAY ----------
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# from aws_xray_sdk.core.sampling.local.sampler import LocalSampler
# xray_recorder.configure(sampler=LocalSampler())

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception

app = Flask(__name__)

rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
ENVIRONMENT = os.getenv('ENVIRONMENT')
@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        rollbar_access_token,
        # environment name
        ENVIRONMENT,
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)

# HoneyComb ---------
# Initialize automatic instrumentation with Flask
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
backendGitpod = os.getenv('BACKEND_URL_GITPOD')
frontendGitpod = os.getenv('FRONTEND_URL_GITPOD')
pod = os.getenv('POD_HOST_URL')
origins = [frontend, backend, pod, backendGitpod, frontendGitpod]
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  #expose_headers="location,link",
  #allow_headers="content-type,if-modified-since,traceparent",
  allow_headers="*",
  headers=['Content-Type', 'Authorization'], 
  expose_headers='Authorization',
  methods="OPTIONS,GET,HEAD,POST"
)
print({os.getenv("AWS_COGNITO_USER_POOL_ID"), 
  os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
  os.getenv("AWS_DEFAULT_REGION")})
cognito_jwt_token = CognitoJwtToken(
  user_pool_id=os.getenv("AWS_COGNITO_USER_POOL_ID"), 
  user_pool_client_id=os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
  region=os.getenv("AWS_DEFAULT_REGION")
)

# X-RAY ----------
xray_url = os.getenv("AWS_XRAY_URL")
xray_sampling_path = '../../aws/json/xray.json'
#xray_recorder.configure(service='Crudder', dynamic_naming=xray_url, sampling=xray_sampling_path)
xray_recorder.configure(service='crudder-backend-flask', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)
xray_recorder.configure(sampling=False)

@xray_recorder.capture('before_request_segment')
@app.before_request
def before_request():
  with tracer.start_as_current_span("before-request-span"):
      xray_segment = xray_recorder.current_segment()
      xray_segment.set_user("aravindvcyber")
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      span.set_attribute("app.user", "aravindvcyber")
      span.set_attribute("app.kind", "server")
      span.set_attribute("http.route", request.path)
      span.set_attribute("http.referer", request.headers.get("Referer","Direct"))
      # print(request.headers)
      span.set_attribute("meta.traceparent", str(request.headers.get('traceparent')))
      #with xray_recorder.in_segment('after_request') as segment:
      timestamp = strftime('[%Y-%b-%d %H:%M]')
      span.set_attribute("app.request_timestamp", timestamp)
      xray_segment.put_annotation('time', now.isoformat())
      xray_segment = xray_recorder.begin_segment('before_request_sub_segment')
      xray_subsegment = xray_recorder.current_subsegment()
      xray_subsegment.put_metadata('time_sub', timestamp) if xray_subsegment is not None else xray_segment.put_annotation('time_sub', timestamp)
      #xray_recorder.end_subsegment()

@xray_recorder.capture('after_request_segment')
@app.after_request
def after_request(response):
  with tracer.start_as_current_span("after-request-span"):
      xray_segment = xray_recorder.current_segment()
      xray_segment.set_user("aravindvcyber")
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      span.set_attribute("app.user", "aravindvcyber")
      span.set_attribute("app.kind", "server")
      span.set_attribute("http.route", request.path)
      #with xray_recorder.in_segment('after_request') as segment:
      timestamp = strftime('[%Y-%b-%d %H:%M]')
      span.set_attribute("app.result_timestamp", timestamp)
      xray_segment.put_annotation('time', now.isoformat())
      xray_segment = xray_recorder.begin_segment('after_request_sub_segment')
      xray_subsegment = xray_recorder.current_subsegment()
      xray_subsegment.put_metadata('time_sub', timestamp) if xray_subsegment is not None else xray_segment.put_annotation('time_sub', timestamp)
      LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
      span.set_attribute("app.request_log", str({timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status}))
      span.set_attribute("http.status_code", response.status_code)
      #xray_recorder.end_subsegment()
  return response

@xray_recorder.capture('rollbar_test')
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"

@xray_recorder.capture('api_health_check')
@app.route('/api/health-check')
def health_check():
  # hello = None
  # hello()
  return {'success': True}, 200

@xray_recorder.capture('message_groups')
@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  # user_handle  = 'aravindvcyber'
  # model = MessageGroups.run(user_handle=user_handle)
  # if model['errors'] is not None:
  #   return model['errors'], 422
  # else:
  #   return model['data'], 200
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    cognito_user_id = claims['sub']
    model = MessageGroups.run(cognito_user_id=cognito_user_id)
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    return {}, 401

# @xray_recorder.capture('messages_handle')
# @app.route("/api/messages/@<string:handle>", methods=['GET'])
# def data_messages(handle):
#   user_sender_handle = 'aravindvcyber'
#   user_receiver_handle = request.args.get('handle')

#   model = Messages.run(user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
#   if model['errors'] is not None:
#     return model['errors'], 422
#   else:
#     return model['data'], 200
#   return

@xray_recorder.capture('messages_handle_message_group')
@app.route("/api/messages/<string:message_group_uuid>", methods=['GET'])
def data_messages(message_group_uuid):
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    cognito_user_id = claims['sub']
    print({cognito_user_id,
        message_group_uuid})
    model = Messages.run(
        cognito_user_id=cognito_user_id,
        message_group_uuid=message_group_uuid
      )
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    return {}, 401

@xray_recorder.capture('messages')
@app.route("/api/messages", methods=['POST','OPTIONS'])
@cross_origin()
def data_create_message():
  message_group_uuid   = request.json.get('message_group_uuid',None)
  user_receiver_handle = request.json.get('handle',None)
  message = request.json['message']
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    cognito_user_id = claims['sub']
    if message_group_uuid == None:
      # Create for the first time
      model = CreateMessage.run(
        mode="create",
        message=message,
        cognito_user_id=cognito_user_id,
        user_receiver_handle=user_receiver_handle
      )
    else:
      # Push onto existing Message Group
      model = CreateMessage.run(
        mode="update",
        message=message,
        message_group_uuid=message_group_uuid,
        cognito_user_id=cognito_user_id
      )
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    return {}, 401

  # model = CreateMessage.run(message=message,user_sender_handle=user_sender_handle,user_receiver_handle=user_receiver_handle)
  # if model['errors'] is not None:
  #   return model['errors'], 422
  # else:
  #   return model['data'], 200
  # return

@xray_recorder.capture('activities_home')
@app.route("/api/activities/home", methods=['GET'])
def data_home():
  with tracer.start_as_current_span("home-entry"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      span.set_attribute("meta.traceparent", str(request.headers.get('traceparent')))
      span.set_attribute("meta.trace_id", str(uuid.uuid4()))
      span.set_attribute("meta.span_id", str(uuid.uuid4()))
      access_token = extract_access_token(request.headers)
      try:
        claims = cognito_jwt_token.verify(access_token)
        # authenicatied request
        app.logger.debug("authenicated")
        app.logger.debug(claims)
        app.logger.debug(claims['username'])
        data = HomeActivities.run(cognito_user_id=claims['username'])
      except TokenVerifyError as e:
        # unauthenicatied request
        app.logger.debug(e)
        app.logger.debug("unauthenicated")
        data = HomeActivities.run()
      return data, 200

@xray_recorder.capture('activities_users')
@app.route("/api/activities/notifications", methods=['GET'])
def data_notifications():
  data = NotificationsActivities.run()
  return data, 200

@xray_recorder.capture('activities_handle')
@app.route("/api/activities/@<string:handle>", methods=['GET'])
def data_handle(handle):
  model = UserActivities.run(handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@xray_recorder.capture('activities_users')
@app.route("/api/activities/search", methods=['GET'])
def data_search():
  term = request.args.get('term')
  model = SearchActivities.run(term)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@xray_recorder.capture('activities')
@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities():
  user_handle  = 'aravindvcyber'
  message = request.json['message']
  ttl = request.json['ttl']
  model = CreateActivity.create_activity(user_handle, message, ttl)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@xray_recorder.capture('activities_activity')
@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
def data_show_activity(activity_uuid):
  data = ShowActivity.run(activity_uuid=activity_uuid)
  return data, 200

@xray_recorder.capture('activities_activity_reply')
@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities_reply(activity_uuid):
  user_handle  = 'aravindvcyber'
  message = request.json['message']
  model = CreateReply.run(message, user_handle, activity_uuid)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/users/<string:handle>/short", methods=['GET'])
def data_users_short(handle):
  data = UsersShort.run(handle)
  return data, 200

if __name__ == "__main__":
  app.run(debug=True)