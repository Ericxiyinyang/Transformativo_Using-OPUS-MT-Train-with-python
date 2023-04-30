import art
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm
from time import sleep
import warnings
from translator import Translator
from interaction_processor import inputProcessor
from interaction import UserInteractor

if __name__ == "__main__":
    warnings.simplefilter('ignore')
    InputProcessor = inputProcessor()
    print("Choose a language to translate from: ")
    source = InputProcessor.stdlanginput()
    print("Choose a language to translate to: ")
    target = InputProcessor.stdlanginput()
    for i in tqdm(range(100), desc="Loading Language Translation Model(MIGHT TAKE A WHILE)"):
        sleep(0.005)
    Translator = Translator(source, target)
    Usercoms = UserInteractor(Translator, InputProcessor)
    Usercoms.greet()
    Usercoms.interactionloop()
