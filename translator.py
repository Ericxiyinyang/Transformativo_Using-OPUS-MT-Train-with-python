from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    def __init__(self, source_language, target_language):
        self.source = source_language
        self.target = target_language
        self.model_name = f"Helsinki-NLP/opus-mt-{self.source}-{self.target}"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.version = "0.0.1 Alpha Build"
        self.isStable = False
        self.author = "NeedingSleep"

    def translate(self, input_txt):
        texttotranslate = input_txt
        batch = self.tokenizer([texttotranslate], return_tensors="pt")
        generated_ids = self.model.generate(**batch)
        return self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]