from lib.db import db
class AddColumnUsersUpdatedAtMigration:
  def migrate_sql():
    data = """
    ALTER TABLE users ADD COLUMN updated_at TIMESTAMP;
    CREATE TRIGGER trig_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW EXECUTE PROCEDURE func_updated_at();
    """
    return data
  def rollback_sql():
    data = """
    DROP TRIGGER IF EXISTS trig_users_updated_at ON users;
    ALTER TABLE users DROP COLUMN updated_at;
    """
    return data
  def migrate():
    db.query_commit(AddColumnUsersUpdatedAtMigration.migrate_sql(),{
    })
  def rollback():
    db.query_commit(AddColumnUsersUpdatedAtMigration.rollback_sql(),{
    })
migration = AddColumnUsersUpdatedAtMigration