import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

class EconomicLinguistics:
    """
    Utilities for analyzing linguistic structures in economic discourse.
    Combines Yale-rooted linguistics and UMich-based economics.
    """
    def __init__(self):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
            nltk.download('stopwords')
            
        self.stop_words = set(stopwords.words('english'))
        
    def extract_economic_markers(self, text: str):
        """
        Extracts key economic and labor market markers from text.
        """
        markers = [
            "labor market", "inflation", "unemployment", "interest rates",
            "GDP", "recession", "economic growth", "tech sector", "AI automation"
        ]
        
        found = [m for m in markers if re.search(rf"\b{m}\b", text.lower())]
        return found
        
    def analyze_lexical_density(self, text: str):
        """
        Calculates lexical density (content words vs total words).
        """
        words = word_tokenize(text.lower())
        content_words = [w for w in words if w.isalnum() and w not in self.stop_words]
        
        density = len(content_words) / len(words) if words else 0
        return f"{density:.2f}"

if __name__ == "__main__":
    utils = EconomicLinguistics()
    test_text = "Interest rates and the labor market are stabilizing with technological advancements."
    print(f"Economic Markers: {utils.extract_economic_markers(test_text)}")
    print(f"Lexical Density: {utils.analyze_lexical_density(test_text)}")
