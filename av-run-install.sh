cd /workspace/aws-bootcamp-cruddur-2023/frontend-react-js
npm install
cd /workspaces/aws-bootcamp-cruddur-2023/


cd /workspace
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
cd /workspaces/aws-bootcamp-cruddur-2023/

cd /workspaces/aws-bootcamp-cruddur-2023/


curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt install -y postgresql-client-13 libpq-dev

cd /workspaces/aws-bootcamp-cruddur-2023/

cd frontend-react-js
npm ci

cd /workspaces/aws-bootcamp-cruddur-2023/