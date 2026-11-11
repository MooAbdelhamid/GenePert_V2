"""
To be written
"""

from pathlib import Path

import scanpy as sc


class LoadTarget:
    def __init__(self):
        self.adata = None
        self.filePath = None
        self.mode = None

    def load_data(self, path, mode="path"):
        """
        Modes: Path, Object Through API
        """
        self.filePath = Path(path)
        self.mode = mode

        if self.mode == "path":
            if not self.filePath.exists():
                raise FileNotFoundError(f"Dataset not found: {self.filePath}")

            self.adata = sc.read_h5ad(self.filePath)

            print(
                f"Dataset loaded: {self.adata.n_obs} cells, {self.adata.n_vars} genes"
            )

        return self
