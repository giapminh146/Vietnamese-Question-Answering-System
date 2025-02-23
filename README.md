# Vietnamese Question Answering System
## Members
**Leader**: Giap Do Anh Minh <br/>
Member: Le Anh Quang  <br/>
Member: Ho Thanh Thuy Tien <br/>
Member: Do Minh Quang  <br/>
Member: Vu Ha Vy <br/>
Member: Phan Nguyen Tuan Minh

## About The Project
In this project, we tried to build a Vietnamese Question Answering system that can help us answer **questions** of a given **context**. We fine-tuned the 4 variants of the BARTpho model: *BARTpho-word*, *BARTpho-syllable*, *BARTpho-word-base*, *BARTpho-syllable-base*. Additionally, we built a user-friendly website interface that allows anyone to interact with our QA System.

## Dataset
The dataset that we used in this project is UIT-ViQuAD2.0. It can be accessed through this HuggingFace link: [UIT-ViQuAD2.0](https://huggingface.co/datasets/taidng/UIT-ViQuAD2.0)

## Installation and Run
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
After that, open the live server on **index.html** to use the interface

In the interface, you can select any model or choose "Auto" mode to provide the best answer among the 4 models.

## Fine-tune and Inference
If you want to fine-tune the models, you can run the files:
* **vn-qa-bartpho-syllable-base.ipynb** if you want to fine-tune the BARTpho-syllable-base model
* **vn-qa-bartpho-syllable.ipynb** if you want to fine-tune the BARTpho-syllable model
* **vn-qa-bartpho-word-base.ipynb** if you want to fine-tune the BARTpho-word-base model
* **vn-qa-bartpho-word.ipynb** if you want to fine-tune the BARTpho-word model
  
If you don't have enough resources, you can run them online (e.g. Google Colab or Kaggle)

For inferencing the fine-tuned models, run the **Inference.ipynb** file. You can load your fine-tuned model or load our fine-tuned models, which are available on HuggingFace: [BARTpho-syllable-qa](https://huggingface.co/lizz4rd/bartpho-syllable-question-answering), [BARTpho-syllable-base-qa](https://huggingface.co/lizz4rd/bartpho-syllable-base-question-answering), [BARTpho-word-qa](https://huggingface.co/lizz4rd/bartpho-word-question-answering), [BARTpho-word-base-qa](https://huggingface.co/lizz4rd/bartpho-word-base-question-answering).

## Examples
Here are some examples about our Vietnamese Question Answering System (for more examples, please visit Demo directory):


![](https://github.com/giapminh146/Vietnamese-Question-Answering-System/blob/main/Demo/Demo_bartpho_syllable.jpg)

* Image 1 (BARTpho-syllable-qa)

![](https://github.com/giapminh146/Vietnamese-Question-Answering-System/blob/main/Demo/Demo_bartpho_word.jpg)

* Image 2 (BARTpho-word-qa)
  
![](https://github.com/giapminh146/Vietnamese-Question-Answering-System/blob/main/Demo/Demo_auto.jpg)


* Image 3 (Auto mode)
