from lib.ddb import Ddb
from lib.db import db

from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
tracer = trace.get_tracer("message.groups")
class MessageGroups:
  # def run(user_handle):
  def run(cognito_user_id):
    with tracer.start_as_current_span("message-groups-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      segment = xray_recorder.begin_segment('message_groups')
      model = {
        'errors': None,
        'data': None
      }

      # now = datetime.now(timezone.utc).astimezone()
      # results = [
      #   {
      #     'uuid': '24b95582-9e7b-4e0a-9ad1-639773ab7552',
      #     'display_name': 'Andrew Brown',
      #     'handle':  'andrewbrown',
      #     'created_at': now.isoformat()
      #   },
      #   {
      #     'uuid': '417c360e-c4e6-4fce-873b-d2d71469b4ac',
      #     'display_name': 'Worf',
      #     'handle':  'worf',
      #     'created_at': now.isoformat()
      # }]
      # model['data'] = results

      sql = db.template('users','uuid_from_cognito_user_id')
      my_user_uuid = db.query_value(sql,{
        'cognito_user_id': cognito_user_id
      })

      print(f"UUID: {my_user_uuid}")

      ddb = Ddb.client()
      data = Ddb.list_message_groups(ddb, my_user_uuid)
      print("list_message_groups:",data)

      model['data'] = data

      span.set_attribute("app.result_length", len(model['data']))
      subsegment = xray_recorder.begin_subsegment('mock-data')
      dict = {
        "now": now.isoformat(),
        "results-size": len(model['data'])
      }
      subsegment.put_metadata('key', dict, 'namespace')
    return model