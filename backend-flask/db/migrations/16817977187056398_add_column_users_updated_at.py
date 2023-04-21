from lib.db import db
class AddColumnUsersUpdatedAtMigration:
  def migrate_sql():
    data = """
    ALTER TABLE public.users ADD COLUMN updated_at TIMESTAMP;
    """
    return data
  def rollback_sql():
    data = """
    ALTER TABLE public.users DROP COLUMN updated_at;
    """
    return data
  def migrate():
    db.query_commit(AddColumnUsersUpdatedAtMigration.migrate_sql(),{
    })
  def rollback():
    db.query_commit(AddColumnUsersUpdatedAtMigration.rollback_sql(),{
    })
migration = AddColumnUsersUpdatedAtMigration