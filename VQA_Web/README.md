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
poetry run uvicorn vqa_web.main:app --reload
```

And for the request, it should look like this:

```bash
fetch("http://127.0.0.1:8000/vqa/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        context: "The context",
        question: "The question"
    }),
})
    .then((response) => response.json())
    .then((data) => console.log(data));
```
then open live server index.html to use the interface
