import json
import psycopg2
import os

def lambda_handler(event, context):
    print(json.dumps(event))
    user = event['request']['userAttributes']
    print('userAttributes')
    print(json.dumps(user))

    user_display_name  = user['name']
    user_email         = user['email']
    user_handle        = user['preferred_username']
    user_cognito_id    = user['sub']
    try:
      print('entered-try')
      sql = f"""
         INSERT INTO public.users (
          display_name, 
          email,
          handle, 
          cognito_user_id
          ) 
        VALUES(
          '{user_display_name}', 
          '{user_email}', 
          '{user_handle}', 
          '{user_cognito_id}'
        )
        RETURNING uuid;
      """
      print('SQL Statement ----')
      print(sql)
      conn = psycopg2.connect(os.getenv('CONNECTION_URL'))
      cur = conn.cursor()
      cur.execute(sql)
      print(cur.fetchone()[0])
      conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    finally:
      if conn is not None:
          cur.close()
          conn.close()
          print('Database connection closed.')
    return event