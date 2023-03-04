from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("search.activities")
class SearchActivities:
  def run(search_term):
    with tracer.start_as_current_span("search-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('search_activities')
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      if search_term == None or len(search_term) < 1:
        model['errors'] = ['search_term_blank']
        span.set_attribute("app.result_errors", model['errors'])
        subsegment = xray_recorder.begin_subsegment('mock-data-errors')
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['errors'])
        }
        subsegment.put_metadata('key', dict, 'namespace')
      else:
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
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