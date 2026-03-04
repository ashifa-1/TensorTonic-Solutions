import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        special_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
    
        for token in special_tokens:
            self.word_to_id[token] = self.vocab_size
            self.id_to_word[self.vocab_size] = token
            self.vocab_size += 1
    
        # collect unique words
        unique_words = set()
    
        for text in texts:
            words = text.split()
            unique_words.update(words)
    
        # add words to vocab
        for word in unique_words:
            self.word_to_id[word] = self.vocab_size
            self.id_to_word[self.vocab_size] = word
            self.vocab_size += 1
        pass
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        words = text.split()
        ids = []
    
        for word in words:
            token_id = self.word_to_id.get(word, self.word_to_id[self.unk_token])
            ids.append(token_id)
    
        return ids
        pass
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words = []
    
        for token_id in ids:
            word = self.id_to_word.get(token_id, self.unk_token)
            words.append(word)
    
        return " ".join(words)
        pass
