# migrate.py
from alembic import command
from alembic.config import Config

def run_migrations():
   try:
       alembic_cfg = Config("alembic.ini")
       command.upgrade(alembic_cfg, "head")
       print("Migrations completed successfully")
   except Exception as e:
       print(f"Migration failed: {e}")

if __name__ == "__main__":
   run_migrations()