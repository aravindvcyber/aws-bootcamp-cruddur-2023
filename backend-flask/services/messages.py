from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("list.messages")
class Messages:
  def run(user_sender_handle, user_receiver_handle):
    with tracer.start_as_current_span("list-messages-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('messages')
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      results = [
        {
          'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a' ,
          'display_name': 'Andrew Brown',
          'handle':  'andrewbrown',
          'message': 'Cloud is fun!',
          'created_at': now.isoformat()
        },
        {
          'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
          'display_name': 'Andrew Brown',
          'handle':  'andrewbrown',
          'message': 'This platform is great!',
          'created_at': now.isoformat()
      }]
      model['data'] = results
      span.set_attribute("app.result_length", len(model['data']))
      subsegment = xray_recorder.begin_subsegment('mock-data')
      dict = {
        "now": now.isoformat(),
        "results-size": len(model['data'])
      }
      subsegment.put_metadata('key', dict, 'namespace')
    return model