from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset Path
DATA_PATH = BASE_DIR / "data" / "HR-Employee-Attrition.csv"

# Model Folder
MODEL_DIR = BASE_DIR / "models"

# Reports Folder
REPORT_DIR = BASE_DIR / "reports"