from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

model_checkpoint_list = [
    'lizz4rd/bartpho-syllable-question-answering',
    'lizz4rd/bartpho-syllable-base-question-answering',
    'lizz4rd/bartpho-word-question-answering',
    'lizz4rd/bartpho-word-base-question-answering'
]

tokenizer = ""
model = ""

def sort_answer(a):
    return len(a)

def load_model():
    print("Starting to load model.")
    for model_checkpoint in model_checkpoint_list:
        tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
    print("Load model complete.")

def get_answer(context : str, question: str):
    # Load model and tokenizer
    for model_checkpoint in model_checkpoint_list:
        tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
        # Tokenize inputs
        inputs = tokenizer(question,context, return_tensors="pt", truncation=True, padding=True)

        # Remove token_type_ids to avoid errors
        inputs.pop("token_type_ids", None)

        # Run inference
        with torch.no_grad():
            outputs = model(**inputs)

        # Get the start and end logits
        start_logits = outputs.start_logits
        end_logits = outputs.end_logits

        # Get the most probable start and end token positions
        start_idx = torch.argmax(start_logits)
        end_idx = torch.argmax(end_logits)

        # Decode the answer
        answer = tokenizer.decode(inputs["input_ids"][0][start_idx:end_idx + 1], skip_special_tokens=True)
        if answer != "":
            return answer
    return ""