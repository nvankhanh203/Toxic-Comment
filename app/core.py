from tensorflow.keras.models import load_model
import json
import re
import numpy as np
import unicodedata
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from torchtext.data.utils import get_tokenizer

# load vocab
VOCAB_PATH = r"F:\khánh toxic comment\vocab.json"
MODEL_PATH = r"F:\khánh toxic comment\model\BiLSTM_e100_h100.keras"

# padding
# train_sents_padded = pad_sequences(train_sents, padding='post', maxlen=max_length)

class ToxicClassification():
    def  __init__(self):
        self.max_length = 120
        self.tokenizer_base = get_tokenizer('basic_english')
        self.model = load_model(MODEL_PATH)
        self.pad_sequences = pad_sequences
        with open(VOCAB_PATH, "r", encoding="utf-8") as file:
            self.vocab_dict = json.load(file)
        
        self.set_tokenizer()
        self.labels = ["Not Toxic", "Toxic"]
    def set_tokenizer(self):
        self.tokenizer_model = Tokenizer(num_words=30000, oov_token='<OOV>', filters="", split=" ")
        # Thiết lập sẵn word_index
        self.tokenizer_model.word_index = self.vocab_dict
        self.tokenizer_model.index_word = {i: w for w, i in self.vocab_dict.items()}

    def text_normalized(self, input_text):
        input_text = re.sub(r"(\")", " ", input_text)
        input_text = re.sub(r" +", " ", input_text)
        return input_text

    def process_input(self, x):
        x = self.text_normalized(unicodedata.normalize("NFKC", " ".join(self.tokenizer_base(x))))
        x = self.tokenizer_model.texts_to_sequences([x])
        x = self.pad_sequences(x, padding='post', maxlen=self.max_length)
        x = self.model(x)
        return self.labels[int(np.round(x[0,0]))]
    
    def __call__(self, x):
        return self.process_input(x)

