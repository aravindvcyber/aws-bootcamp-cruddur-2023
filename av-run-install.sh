cd /workspace
wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
cd $THEIA_WORKSPACE_ROOT

cd $THEIA_WORKSPACE_ROOT/frontend-react-js
rm -rf node_modules
npm install
cd ..

cd $THEIA_WORKSPACE_ROOT
bundle update --bundler
pip install cfn-lint
cargo install cfn-guard
gem install cfn-toml

cd $THEIA_WORKSPACE_ROOT/aws/lambdas/lambda-authorizer/
npm install

cd $THEIA_WORKSPACE_ROOT/aws/lambdas/cruddur-upload-avatar/
# rm lambda_function.zip
# rm -rf vendor/bundle
# bundle install --path vendor/bundle
# bundle update
# zip -r lambda_function.zip function.rb .bundle/ vendor/

rm lambda_function_slim.zip
bundle install
bundle update
zip -r lambda_function_slim.zip function.rb Gemfile Gemfile.lock


cd $THEIA_WORKSPACE_ROOT/backend-flask
pip install -r requirements.txt
cd ..

cd $THEIA_WORKSPACE_ROOT/bin/db
pip install -r requirements.txt
cd ..




cd $THEIA_WORKSPACE_ROOT
mkdir tmp
cd tmp
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
rm awscliv2.zip
sudo ./aws/install



curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt install -y postgresql-client-13 libpq-dev

cd $THEIA_WORKSPACE_ROOT
mkdir -rf tmp

# echo $pwd
# cd /workspaces/aws-bootcamp-cruddur-2023/frontend-react-js

# npm ci

# cd /workspaces/aws-bootcamp-cruddur-2023/

export GITPOD_IP=$(curl ifconfig.me)
gp env GITPOD_IP=$(curl ifconfig.me)
source  "$THEIA_WORKSPACE_ROOT/bin/rds/update-sg-rule"


curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb"
sudo dpkg -i session-manager-plugin.deb
rm session-manager-plugin.deb

npm instal -g aws-cdk
npm install -g npm@9.6.4
#rm package-lock.json

./bin/ecr/login

./bin/backend/generate-env

./bin/backend/generate-env-local

# ./bin/backend/generate-env-local-cs


./bin/frontend/generate-env

./bin/frontend/generate-env-local

# ./bin/frontend/generate-env-local-cs




