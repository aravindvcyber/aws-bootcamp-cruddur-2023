import uuid
from datetime import datetime, timedelta, timezone

from lib.db import db
from lib.ddb import Ddb

from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("create.message")
class CreateMessage:
  # def run(message, user_sender_handle, user_receiver_handle):
  # mode indicates if we want to create a new message_group or using an existing one
  def run(mode, message, cognito_user_id, message_group_uuid=None, user_receiver_handle=None):
    with tracer.start_as_current_span("create-message-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('create_message')
      model = {
        'errors': None,
        'data': None
      }
      # if user_sender_handle == None or len(user_sender_handle) < 1:
      #   model['errors'] = ['user_sender_handle_blank']

      # if user_receiver_handle == None or len(user_receiver_handle) < 1:
      #   model['errors'] = ['user_reciever_handle_blank']

      if (mode == "update"):
        if message_group_uuid == None or len(message_group_uuid) < 1:
          model['errors'] = ['message_group_uuid_blank']

      if cognito_user_id == None or len(cognito_user_id) < 1:
        model['errors'] = ['cognito_user_id_blank']

      if (mode == "create"):
        if user_receiver_handle == None or len(user_receiver_handle) < 1:
          model['errors'] = ['user_reciever_handle_blank']

      if message == None or len(message) < 1:
        model['errors'] = ['message_blank'] 
      elif len(message) > 1024:
        model['errors'] = ['message_exceed_max_chars'] 

      if model['errors']:
        # return what we provided
        span.set_attribute("app.result_errors", model['errors'])
        subsegment = xray_recorder.begin_subsegment('mock-data-errors')
        dict = {
          "now": now.isoformat(),
          "results-errors": model['errors']
        }
        subsegment.put_metadata('key', dict, 'namespace')
        model['data'] = {
          'display_name': 'Andrew Brown',
          'handle':  user_sender_handle,
          'message': message
        }
        span.set_attribute("app.result_length", len(model['data']))
        subsegment = xray_recorder.begin_subsegment('mock-data')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
      else:
        # now = datetime.now(timezone.utc).astimezone()
        # model['data'] = {
        #   'uuid': uuid.uuid4(),
        #   'display_name': 'Andrew Brown',
        #   'handle':  user_sender_handle,
        #   'message': message,
        #   'created_at': now.isoformat()
        # }
        sql = db.template('users','create_message_users')

        if user_receiver_handle == None:
          rev_handle = ''
        else:
          rev_handle = user_receiver_handle
        users = db.query_array_json(sql,{
          'cognito_user_id': cognito_user_id,
          'user_receiver_handle': rev_handle
        })
        print("USERS =-=-=-=-==")
        print(users)

        my_user    = next((item for item in users if item["kind"] == 'sender'), None)
        other_user = next((item for item in users if item["kind"] == 'recv')  , None)

        print("USERS=[my-user]==")
        print(my_user)
        print("USERS=[other-user]==")
        print(other_user)

        ddb = Ddb.client()

        if (mode == "update"):
          data = Ddb.create_message(
            client=ddb,
            message_group_uuid=message_group_uuid,
            message=message,
            my_user_uuid=my_user['uuid'],
            my_user_display_name=my_user['display_name'],
            my_user_handle=my_user['handle']
          )
        elif (mode == "create"):
          data = Ddb.create_message_group(
            client=ddb,
            message=message,
            my_user_uuid=my_user['uuid'],
            my_user_display_name=my_user['display_name'],
            my_user_handle=my_user['handle'],
            other_user_uuid=other_user['uuid'],
            other_user_display_name=other_user['display_name'],
            other_user_handle=other_user['handle']
          )
        model['data'] = data
        span.set_attribute("app.result_length", len(model['data']))
        subsegment = xray_recorder.begin_subsegment('mock-data')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
    return model