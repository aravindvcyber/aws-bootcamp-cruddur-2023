import uuid
from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("create.reply")
class CreateReply:
  def run(message, user_handle, activity_uuid):
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
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['user_handle_blank']

      if activity_uuid == None or len(activity_uuid) < 1:
        model['errors'] = ['activity_uuid_blank']

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
          'message': message,
          'reply_to_activity_uuid': activity_uuid
        }
        model['data'] = results
        span.set_attribute("app.result_length", len(model['data']))
        subsegment = xray_recorder.begin_subsegment('mock-data')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
      else:
        now = datetime.now(timezone.utc).astimezone()
        results = {
          'uuid': uuid.uuid4(),
          'display_name': 'Andrew Brown',
          'handle':  user_handle,
          'message': message,
          'created_at': now.isoformat(),
          'reply_to_activity_uuid': activity_uuid
        }
        model['data'] = results
        span.set_attribute("app.result_length", len(model['data']))
        subsegment = xray_recorder.begin_subsegment('mock-data')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
    return model
