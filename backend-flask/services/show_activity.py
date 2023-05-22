from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("show.activities")
from lib.db import db

class ShowActivity:
  def run(activity_uuid):
    with tracer.start_as_current_span("show-activities-mock-data"):
      model = {
        'errors': None,
        'data': None
      }
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('show_activities')
      now = datetime.now(timezone.utc).astimezone()
      sql = db.template('activities','show')
      results = db.query_array_json(sql,{
        'uuid': activity_uuid
      })
      model['data'] = results
      span.set_attribute("app.result_length", len(model['data']))
      subsegment = xray_recorder.begin_subsegment('mock-data')
      dict = {
        "now": now.isoformat(),
        "results-size": len(results)
      }
      subsegment.put_metadata('key', dict, 'namespace')
    return results