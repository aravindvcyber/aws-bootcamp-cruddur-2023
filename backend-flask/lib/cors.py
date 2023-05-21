from flask_cors import CORS
import os

def init_cors(app):
#   frontend = os.getenv('FRONTEND_URL')
#   backend = os.getenv('BACKEND_URL')
#   origins = [frontend, backend]
#   cors = CORS(
#     app, 
#     resources={r"/api/*": {"origins": origins}},
#     headers=['Content-Type', 'Authorization'], 
#     expose_headers='Authorization',
#     methods="OPTIONS,GET,HEAD,POST"
#   )
  frontend = os.getenv('FRONTEND_URL')
  backend = os.getenv('BACKEND_URL')
  backendGitpod = os.getenv('BACKEND_URL_GITPOD')
  frontendGitpod = os.getenv('FRONTEND_URL_GITPOD')
  backendCodespace = os.getenv('BACKEND_URL_CODESPACE')
  frontendCodespace = os.getenv('FRONTEND_URL_CODESPACE')
  localhost = "http://localhost:3000"
  localhost2 = "http://127.0.0.1:3000"
  pod = os.getenv('POD_HOST_URL')
  origins = [frontend, backend, pod, backendGitpod, frontendGitpod, backendCodespace, frontendCodespace, localhost,localhost2]
  print(origins)
  cors = CORS(
    app, 
    resources={r"/api/*": {"origins": origins}},
    #expose_headers="location,link",
    #allow_headers="content-type,if-modified-since,traceparent",
    allow_headers="*",
    headers=['Content-Type', 'Authorization'], 
    expose_headers='Authorization',
    methods="OPTIONS,GET,HEAD,POST"
  )
  print({os.getenv("AWS_COGNITO_USER_POOL_ID"), 
    os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
    os.getenv("AWS_DEFAULT_REGION")})