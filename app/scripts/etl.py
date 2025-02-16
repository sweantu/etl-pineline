from app.scripts.create_tables import create_tables
from app.scripts.load import load_data


def run_etl():
    print("🚀 Starting ETL Pipeline...")
    create_tables()
    load_data()
    print("✅ ETL Pipeline Completed!")


if __name__ == "__main__":
    run_etl()
