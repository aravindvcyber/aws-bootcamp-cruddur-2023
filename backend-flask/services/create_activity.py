import uuid
from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("create.activity")
class CreateActivity:
  def run(message, user_handle, ttl):
    with tracer.start_as_current_span("create-activity-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('create_activity')
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      if (ttl == '30-days'):
        ttl_offset = timedelta(days=30) 
      elif (ttl == '7-days'):
        ttl_offset = timedelta(days=7) 
      elif (ttl == '3-days'):
        ttl_offset = timedelta(days=3) 
      elif (ttl == '1-day'):
        ttl_offset = timedelta(days=1) 
      elif (ttl == '12-hours'):
        ttl_offset = timedelta(hours=12) 
      elif (ttl == '3-hours'):
        ttl_offset = timedelta(hours=3) 
      elif (ttl == '1-hour'):
        ttl_offset = timedelta(hours=1) 
      else:
        model['errors'] = ['ttl_blank']

      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['user_handle_blank']

      if message == None or len(message) < 1:
        model['errors'] = ['message_blank'] 
      elif len(message) > 280:
        model['errors'] = ['message_exceed_max_chars'] 

      if model['errors']:
        span.set_attribute("app.result_errors", model['errors'])
        subsegment = xray_recorder.begin_subsegment('mock-data-errors')
        dict = {
          "now": now.isoformat(),
          "results-errors": model['errors']
        }
        subsegment.put_metadata('key', dict, 'namespace')
        model['data'] = {
          'handle':  user_handle,
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
        model['data'] = {
          'uuid': uuid.uuid4(),
          'display_name': 'Andrew Brown',
          'handle':  user_handle,
          'message': message,
          'created_at': now.isoformat(),
          'expires_at': (now + ttl_offset).isoformat()
        }
        span.set_attribute("app.result_length", len(model['data']))
        subsegment = xray_recorder.begin_subsegment('mock-data')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
    return model