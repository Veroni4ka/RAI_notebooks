# RAI Notebooks & Content Safety Samples

This repository contains examples for Responsible AI (RAI) evaluation, Red Teaming using Azure AI Foundry, and Azure Content Safety text analysis.

## High-Level Structure

*   **[dotnet/](dotnet/)**: Contains a C# Console Application demonstrating Azure Content Safety.
    *   [`Program.cs`](dotnet/Program.cs): Main logic for analyzing text for Hate, SelfHarm, Sexual, and Violence categories.
    *   [`AnalyzeText.csproj`](dotnet/AnalyzeText.csproj): Project file.
*   **[python/](python/)**: Contains Jupyter Notebooks for AI evaluation and Red Teaming.
    *   **Data**: [`data/`](python/data/) contains JSONL datasets (Circus, Hiking, Software Engineering) used for evaluation.
    *   **Notebooks**:
        *   [`RedTeaming.ipynb`](python/RedTeaming.ipynb): AI Red Teaming Agent for adversarial testing.
        *   [`DatasetEval-newFoundry.ipynb`](python/DatasetEval-newFoundry.ipynb): Evaluates datasets using Azure AI Foundry evaluators.
        *   [`ModelResponseEval-newFoundry.ipynb`](python/ModelResponseEval-newFoundry.ipynb): Generates and evaluates model responses against ground truth.
        *   [`MultiModelEval.ipynb`](python/MultiModelEval.ipynb): Compares multiple models (Grok, GPT-5, Claude).
    *   **Utilities**: [`model_endpoints.py`](python/model_endpoints.py) handles API calls to various model deployments.

---

## Python Notebooks

The Python folder contains notebooks that interact with Azure AI Foundry and Azure OpenAI.

### Prerequisites
*   Python 3.10+
*   Azure CLI (`az login`)
*   An Azure AI Foundry Project

### Setup

1.  **Navigate to the python directory:**
    ```bash
    cd python
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    Based on the imports in [`RedTeaming.ipynb`](python/RedTeaming.ipynb), install the required packages:
    ```bash
    pip install azure-ai-evaluation[redteam] azure-identity openai azure-ai-projects python-dotenv requests
    ```

4.  **Configuration (.env):**
    Create a `.env` file in the `python/` folder with the following variables (referenced in [`ModelResponseEval-newFoundry.ipynb`](python/ModelResponseEval-newFoundry.ipynb)):
    ```env
    AZURE_PROJECT_ENDPOINT="your-foundry-project-endpoint"
    AZURE_OPENAI_DEPLOYMENT="your-deployment-name"
    AZURE_OPENAI_ENDPOINT="your-openai-endpoint"
    AZURE_OPENAI_API_KEY="your-api-key"
    AZURE_OPENAI_API_VERSION="2024-12-01-preview"
    ```

### Running the Notebooks
1.  Open a notebook file (e.g., [`RedTeaming.ipynb`](python/RedTeaming.ipynb)) in VS Code.
2.  Select the `.venv` kernel you created in the top right corner.
3.  Run the cells sequentially. Note that you may need to authenticate via the browser when `!az login` is executed.

---

## .NET Project

The .NET folder contains a console application that uses the Azure Content Safety SDK.

### Prerequisites
*   .NET SDK 6.0 or later.
*   An Azure Content Safety resource.

### Setup

1.  **Navigate to the dotnet directory:**
    ```bash
    cd dotnet
    ```

2.  **Configuration:**
    Open [`appsettings.json`](dotnet/appsettings.json) and update the `AzureContentSafety` section with your resource details:
    ```json
    {
      "AzureContentSafety": {
        "Endpoint": "https://your-resource-name.cognitiveservices.azure.com/",
        "Key": "your-api-key"
      }
    }
    ```

### Running the Application

1.  **Build the project:**
    ```bash
    dotnet build
    ```

2.  **Run the application:**
    ```bash
    dotnet run
    ```

3.  Follow the prompt to enter text. The application will output severity scores for Hate, SelfHarm, Sexual, and Violence categories.