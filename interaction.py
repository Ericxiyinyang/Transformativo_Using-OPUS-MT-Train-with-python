import art
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm
from time import sleep
from interaction_processor import inputProcessor

class UserInteractor:
    def __init__(self, translator, inputprocessor):
        self.translator = translator
        self.inputProcessor = inputprocessor

    def greet(self):
        for i in tqdm(range(100), desc="Loading Terminal Interface"):
            sleep(0.005)
        art.tprint("Transformativo AI")
        sleep(0.8)
        print(f"*Version: {self.translator.version}* Made by: {self.translator.author}")
        if self.translator.isStable:
            print("This is a STABLE build, expect no bugs and crashes.")
        else:
            print("This is an UNSTABLE build, expect bugs and crashes.")

    def interactionloop(self):
        while True:
            print()
            print(f"Current Language: {self.translator.source} -> {self.translator.target}")
            print()
            print("Commands: 1. translate, 2. choose a different language, 3. exit")
            userin = input()
            if userin == "1":
                print("Enter text to translate: ")
                txt = input()
                print(self.translator.translate(txt))
                print()
                print("continue? (y/n)")
                continuechoice = input()
                if continuechoice == "y":
                    continue
                else:
                    art.tprint("Thank You!")
                    break
            elif userin == "2":
                print("Choose a language to translate from: ")
                source = self.inputProcessor.stdlanginput()
                print("Choose a language to translate to: ")
                target = self.inputProcessor.stdlanginput()
                self.translator.source = source
                self.translator.target = target
                self.translator.model_name = f"Helsinki-NLP/opus-mt-{self.translator.source}-{self.translator.target}"
                self.translator.tokenizer = AutoTokenizer.from_pretrained(self.translator.model_name)
                self.translator.model = AutoModelForSeq2SeqLM.from_pretrained(self.translator.model_name)
                for i in tqdm(range(100), desc="Loading NEW Language Model"):
                    sleep(0.005)
                art.tprint("Language changed!")
                sleep(0.8)
                continue
            elif userin == "3":
                print("Exiting...")
                art.tprint("Thank You!")
                break