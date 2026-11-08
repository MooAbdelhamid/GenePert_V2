"""
To be written
"""

from pathlib import Path

import pandas as pd
import scanpy as sc


class LoadX:
    def __init__(self):
        self.adata = None
        self.filePath = None

    def load_data(self, path):
        self.filePath = Path(path)

        if not self.filePath.exists():
            raise FileNotFoundError(f"Dataset not found: {self.filePath}")

        self.adata = sc.read_h5ad(self.filePath)

        print(f"Dataset loaded: {self.adata.n_obs} cells, {self.adata.n_vars} genes")

        return self


class Loady:
    def __init__(self):
        self.data = None
        self.filePath = None

    def load_data(self, path):
        self.filePath = Path(path)

        if not self.filePath.exists():
            raise FileNotFoundError(f"Dataset not found: {self.filePath}")

        # check for file extention
        extension = self.filePath.name.split(".")[1]

        if extension == "csv":
            self.data = pd.read_csv(self.filePath)
            print("Dataset loaded")

        elif extension in ["xls", "xlsx"]:
            self.data = pd.read_excel(self.filePath)
            print("Dataset loaded")
        else:
            raise ValueError(
                f"Invalid file type: {self.filePath.suffix}. "
                "Expected an Excel file (csv or xlsx or xls)."
            )
