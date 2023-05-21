# import uuid
from datetime import datetime, timedelta, timezone

from lib.db import db


from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("create.reply")
class CreateReply:
  def run(message, cognito_user_id, activity_uuid):
    with tracer.start_as_current_span("create-reply-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('create_reply')
      user_sender_handle = ''
      model = {
        'errors': None,
        'data': None
      }
      if cognito_user_id == None or len(cognito_user_id) < 1:
        model['errors'] = ['cognito_user_id_blank']

      if activity_uuid == None or len(activity_uuid) < 1:
        model['errors'] = ['activity_uuid_blank']

      if message == None or len(message) < 1:
        model['errors'] = ['message_blank'] 
      elif len(message) > 1024:
        model['errors'] = ['message_exceed_max_chars_1024'] 

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
          # 'display_name': 'Andrew Brown',
          # 'handle':  user_sender_handle,
          'message': message,
          'reply_to_activity_uuid': activity_uuid
        }
        span.set_attribute("app.result_length", len(model['data']))
        subsegment = xray_recorder.begin_subsegment('mock-data')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
      else:
    #     now = datetime.now(timezone.utc).astimezone()
    #     results = {
    #       'uuid': uuid.uuid4(),
    #       'display_name': 'Andrew Brown',
    #       'handle':  user_handle,
    #       'message': message,
    #       'created_at': now.isoformat(),
    #       'reply_to_activity_uuid': activity_uuid
    #     }
    #     model['data'] = results
    #     span.set_attribute("app.result_length", len(model['data']))
    #     subsegment = xray_recorder.begin_subsegment('mock-data')
    #     dict = {
    #       "now": now.isoformat(),
    #       "results-size": len(model['data'])
    #     }
    #     subsegment.put_metadata('key', dict, 'namespace')
    # return model
          uuid = CreateReply.create_reply(cognito_user_id,activity_uuid,message)

      object_json = CreateReply.query_object_activity(uuid)
      model['data'] = object_json
    return model

  def create_reply(cognito_user_id, activity_uuid, message):
    sql = db.template('activities','reply')
    uuid = db.query_commit(sql,{
      'cognito_user_id': cognito_user_id,
      'reply_to_activity_uuid': activity_uuid,
      'message': message,
    })
    return uuid
  def query_object_activity(uuid):
    sql = db.template('activities','object')
    return db.query_object_json(sql,{
      'uuid': uuid
    })
