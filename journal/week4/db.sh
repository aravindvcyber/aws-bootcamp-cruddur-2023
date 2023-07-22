aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t4g.micro \
  --engine postgres \
  --engine-version  15.2 \
  --master-username root \
  --master-user-password ******** \
  --allocated-storage 20 \
  --availability-zone ap-south-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection

aws rds modify-db-instance --db-instance-identifier cruddur-db-instance --master-user-password ********


postgresql://[user[:password]]@[netloc][:port][/dbname][?param1=value1&]

createdb cruddur -h localhost -U postgres

export CONNECTION_URL=postgresql://postgres:password@db:5432/cruddur
gp env CONNECTION_URL=postgresql://postgres:password@db:5432/cruddur



psql $CONNECTION_URL


psql cruddur < db/schema.sql -h localhost -U postgres




GITPOD_IP=$(curl ifconfig.me)
CODESPACE_IP=$(curl ifconfig.me)

export DB_SG_ID="sg-02d094a5bdec82a18"
gp env DB_SG_ID="sg-02d094a5bdec82a18"
export DB_SG_RULE_ID="sgr-0a8b5d15d6c931e79"
gp env DB_SG_RULE_ID="sgr-0a8b5d15d6c931e79"

export RDS_SG_ID="sg-03f726db1626779ac"
gp env RDS_SG_ID="sg-03f726db1626779ac"
export RDS_SG_RULE_ID="sgr-0914d04e4ab6df4da"
gp env RDS_SG_RULE_ID="sgr-0914d04e4ab6df4da"


aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"


aws ec2 modify-security-group-rules \
    --group-id $RDS_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$RDS_SG_RULE_ID,SecurityGroupRule={IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"

export PROD_INSTANCE_ENDPOINT=cruddur-db-instance.cgrz56dxptjn.ap-south-1.rds.amazonaws.com
gp env PROD_INSTANCE_ENDPOINT=cruddur-db-instance.cgrz56dxptjn.ap-south-1.rds.amazonaws.com
export PROD_INSTANCE_PASSWORD=**********
gp env PROD_INSTANCE_PASSWORD=**********
export PROD_CONNECTION_URL="postgresql://root:${PROD_INSTANCE_PASSWORD}@${PROD_INSTANCE_ENDPOINT}:5432/cruddur"
gp env PROD_CONNECTION_URL="postgresql://root:${PROD_INSTANCE_PASSWORD}@${PROD_INSTANCE_ENDPOINT}:5432/cruddur"



