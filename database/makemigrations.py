from datetime import datetime
from alembic import command
from alembic.config import Config

def make_migrations(message):
   try:
       timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
       alembic_cfg = Config("alembic.ini")
       revision_id = f"{timestamp}__{message.replace(' ', '_')}"
       command.revision(alembic_cfg, 
                       message=message,
                       autogenerate=True,
                       rev_id=revision_id)
       print("Migration file created successfully")
   except Exception as e:
       print(f"Failed to create migration: {e}")

if __name__ == "__main__":
   import sys
   if len(sys.argv) > 1:
       make_migrations(sys.argv[1])
   else:
       print("Please provide a migration message")