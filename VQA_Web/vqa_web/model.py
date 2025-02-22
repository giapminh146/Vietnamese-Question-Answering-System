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

def clean_answer(question, answer):
    if answer.startswith(question):
        return answer[len(question):].strip()
    return answer

def get_answer(context: str, question: str, selected_model: str = ""):
    if not selected_model:
        for model_checkpoint in model_checkpoint_list:
            tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
            model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
            
            inputs = tokenizer(question, context, return_tensors="pt", truncation=True, padding=True)
            inputs.pop("token_type_ids", None)

            with torch.no_grad():
                outputs = model(**inputs)

            start_logits = outputs.start_logits
            end_logits = outputs.end_logits

            start_idx = torch.argmax(start_logits)
            end_idx = torch.argmax(end_logits)

            #answer = tokenizer.decode(inputs["input_ids"][0][start_idx:end_idx + 1], skip_special_tokens=True)
            answer = clean_answer(question, tokenizer.decode(inputs["input_ids"][0][start_idx:end_idx + 1], skip_special_tokens=True))
            if answer != "":

                return {
                    "answer": answer,
                    "model": model_checkpoint.split('/')[-1]
                }
    else:
        model_checkpoint = f"lizz4rd/{selected_model}"
        tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
        model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
        
        inputs = tokenizer(question, context, return_tensors="pt", truncation=True, padding=True)
        inputs.pop("token_type_ids", None)

        with torch.no_grad():
            outputs = model(**inputs)

        start_logits = outputs.start_logits
        end_logits = outputs.end_logits

        start_idx = torch.argmax(start_logits)
        end_idx = torch.argmax(end_logits)

        #answer = tokenizer.decode(inputs["input_ids"][0][start_idx:end_idx + 1], skip_special_tokens=True)
        answer = clean_answer(question, tokenizer.decode(inputs["input_ids"][0][start_idx:end_idx + 1], skip_special_tokens=True))
        return {
            "answer": answer if answer else "Tôi không thể tìm thấy câu trả lời với model này.",
            "model": selected_model
        }
    
    return {
        "answer": "Xin lỗi, tôi không thể tìm thấy câu trả lời cho câu hỏi này.",
        "model": "none"
    }