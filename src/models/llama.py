import os
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

load_dotenv()

class LlamaModel:
    def __init__(self):
        model_name = "meta-llama/Llama-3.2-3B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=os.getenv("HF_ACCESS_TOKEN"))
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            use_auth_token=os.getenv("HF_ACCESS_TOKEN"),
            device_map="auto"
        )

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=256, temperature=0.7)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
