import os
from pathlib import Path

package_name = "DiamondPricePrediction"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/Data_ingestion.py",
    f"src/{package_name}/components/Data_transformation.py",
    f"src/{package_name}/components/Model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/Training_pipeline.py",
    f"src/{package_name}/pipelines/Prediction_Pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "Notebook_Experiments/Research.ipynb",
    "Notebook_Experiments/Data/.gitkeep",
    "templates/index.html",
    "static/style.css",
    "app.py",
    "requirements.txt",
    "setup.py",
    "README.md",
    "Dockerfile"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
