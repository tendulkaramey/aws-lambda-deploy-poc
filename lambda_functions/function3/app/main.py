import json
from alembic import command
from alembic.config import Config

def run_migrations():
    alembic_cfg = Config("database/alembic.ini")
    alembic_cfg.set_main_option('script_location', 'database/alembic')
    command.upgrade(alembic_cfg, "head")
    print("Migrations completed successfully")

def lambda_handler(event, context):

    run_migrations()

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'MIGRATIONS RUN'
        })
    }
