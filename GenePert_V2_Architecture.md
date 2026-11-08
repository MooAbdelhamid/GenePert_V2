# GenePert V2

## 1. System Architecture

### Objective

Build a modular and configurable machine learning pipeline that predicts gene expression responses to genetic perturbations using gene description embeddings.

The system should support different sources of gene embeddings:
- Precomputed embeddings (e.g. GenePT).
- Embeddings generated dynamically from biological text descriptions using a pretrained language model.

The pipeline should allow different embedding sources, preprocessing strategies, and ML models to be used without requiring changes to the entire system.

### System Diagram



## 2. System Components

### 2.1 Data Ingestion

**Responsibility:**

Load the raw input data required by the pipeline and perform initial structural validation.

The ingestion layer handles two main data inputs:

**1. Target data (Y source)**
- Load the single-cell gene expression dataset (AnnData).
- Validate that the expected metadata and expression matrix are available.
- Check the basic structure and data types.

**2. Training data (X source)**

Support two ingestion modes:

- **Precomputed embeddings:** Load an existing gene embedding file, such as GenePT embeddings.
- **Text descriptions:** Load gene identifiers and their corresponding biological descriptions, which will subsequently be used to generate embeddings.

The selected mode determines the type of raw input provided to Data Preparation.

**Expected outputs:**
- Loaded AnnData object.
- Either precomputed gene embeddings or gene-description data.
- TBD

### 2.2 Data Preparation

**Responsibility:**

Transform the ingested data into machine-learning-ready input features (X) and target values (Y).

This layer contains two independent preparation workflows.

**1. X preparation – Gene embeddings**

The preparation process depends on the input type selected during ingestion.

- **Embedding input:** Validate and standardize the loaded precomputed embeddings.
- **Text input:** Load the selected pretrained embedding model and generate embeddings from the biological descriptions.

Additional responsibilities:
- Match gene identifiers between perturbation labels and embedding keys.
- Handle missing gene embeddings.
- Validate embedding dimensions and numerical values.
- Store the resulting gene-to-embedding mapping.

The embedding-generation process should be model-configurable, allowing different pretrained models to be used.

**2. Y preparation – Expression targets**

Prepare the gene expression dataset to construct the target matrix.

Responsibilities:
- Filter invalid or unassigned perturbation labels.
- Standardize control labels.
- Perform gene and cell quality control.
- Normalize expression values.
- Apply log transformation when required.
- Group cells by perturbation.
- Calculate the mean expression profile for each perturbation.

Each perturbation produces one target expression vector containing the mean expression of all measured genes.

**3. Dataset construction**

- Align X and Y using perturbation identifiers.
- Validate compatible dimensions and identifiers.
- Produce the final training dataset.

**Expected outputs:**
- X: Gene embedding matrix.
- Y: Mean expression profile matrix.
- Perturbation identifiers linking X and Y.

### 2.3 Training

**Responsibility:**

Train machine learning models using the prepared X and Y datasets.

The training layer should be modular and model-independent at the pipeline level.

Responsibilities:
- Provide a model-selection mechanism.
- Support different model architectures.
- Configure model-specific hyperparameters.
- Train the selected model using X and Y.
- Support cross-validation and experiment configurations.
- Save trained models and relevant experiment metadata.

**Initial candidate models:**
- Baseline models (mean/median).
- Ridge Regression.
- K-Nearest Neighbors (KNN).
- Multi-Layer Perceptron (MLP).

The architecture should allow additional models to be introduced without changing the overall training workflow.

### 2.4 Evaluation

**Responsibility:**

Evaluate model performance and compare predictions against the observed expression targets.

Responsibilities:
- TBD

**Initial evaluation metrics:**
- RMSE.
- MAE.
- Pearson correlation.

### 2.5 Reports

**Responsibility:**

Translate evaluation outputs into interpretable results and visualizations.

Responsibilities:
- TBD

### 2.6 Orchestration

**Responsibility:**

Coordinate and execute the complete pipeline using configurable inputs and parameters.

Responsibilities:
- TBD

### 2.7 User Interface

**Responsibility:**


## 3. Configuration and Modularity

The pipeline should be configurable through a central configuration mechanism.

Important configuration parameters include:

| Component | Configuration |
|---|---|
| Data ingestion | Dataset paths, X input mode |
| X preparation | Input type, embedding model, model name |
| Y preparation | QC thresholds, normalization, log transformation |
| Training | Model selection, hyperparameters |
| Evaluation | Metrics, cross-validation settings |
| Reports | Output formats and visualization settings |

**Important design principle:**

Each component should operate through defined inputs and outputs. Changing the embedding source or ML model should not require modifying unrelated components.

## 4. MVP – Minimum Viable Product

The first implementation should focus on establishing a complete, working end-to-end pipeline.

### Phase 1 – Data Ingestion
- Load the AnnData target dataset.
- Load precomputed gene embeddings.
- Load gene descriptions as an alternative X input.
- Perform initial structural validation.

### Phase 2 – Data Preparation
- Implement target preprocessing and mean expression calculation.
- Implement precomputed embedding loading and validation.
- Implement embedding generation using one pretrained model.
- Match perturbation identifiers to embeddings.
- Build and align X and Y.

### Phase 3 – Training
- Implement a common training interface.
- Implement Baseline and Ridge Regression initially.
- Support configurable model selection and parameters.

### Phase 4 – Evaluation
- Implement RMSE, MAE, and Pearson correlation.
- Evaluate predictions relative to control expression.
- Implement initial cross-validation.

### Phase 5 – Reports
- Generate basic performance tables.
- Visualize predicted versus observed expression.
- Compare model performance.

### Phase 6 – Orchestration
- Connect all modules into one executable pipeline.
- Introduce a central experiment configuration.
- Save experiment outputs and configurations.
