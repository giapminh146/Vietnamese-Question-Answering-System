# Instruction

## Installation

### Prerequisites

Install [Poetry](https://python-poetry.org/docs/#installation).

### Clone the Repository

```bash
git clone <repository_url>
cd VQA_Web
poetry install
```
And for running backend
```bash
 poetry run uvicorn vqa_web_backend.main:app --reload
```