from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from lib.db import db
from opentelemetry import trace
tracer = trace.get_tracer("user.activities")
class UserActivities:
  def run(user_handle):
    with tracer.start_as_current_span("user-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('user_activities')
      model = {
        'errors': None,
        'data': None
      }
      now = datetime.now(timezone.utc).astimezone()
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
        span.set_attribute("app.result_errors", model['errors'])
      else:
        sql = db.template('users','activities')
        user_activites = db.query_array_json(sql,{
        'handle': user_handle
        })

        now = datetime.now()
        
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
          'created_at': (now - timedelta(days=1)).isoformat(),
          'expires_at': (now + timedelta(days=31)).isoformat()
        }]
        model['data'] = results
        # print(user_activites)
        if(len(user_activites) > 0):
          model['data'] = user_activites
        
        span.set_attribute("app.result_length", len(model['data']))
        try:
          subsegment = xray_recorder.begin_subsegment('mock-data')
          dict = {
            "now": now.isoformat(),
            "results-size": len(model['data'])
          }
          subsegment.put_metadata('key', dict, 'namespace')
          xray_recorder.end_subsegment()
        finally:
          xray_recorder.end_subsegment()
    return model