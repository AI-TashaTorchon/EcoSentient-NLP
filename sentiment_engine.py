import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

class EcoSentientEngine:
    """
    Advanced Sentiment Engine specializing in Economic and Labor Market discourse.
    Utilizes a fine-tuned Transformer model to detect nuanced sentiment shifts
    at the intersection of Economics and Linguistics.
    """
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
    def analyze_economic_text(self, text: str):
        """
        Analyzes economic text for sentiment and confidence scores.
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
            
        probs = F.softmax(outputs.logits, dim=-1)
        sentiment_id = torch.argmax(probs).item()
        confidence = probs[0][sentiment_id].item()
        
        # Mapping for economic context
        labels = {0: "CONTRADICTORY/NEGATIVE", 1: "EXPANSIVE/POSITIVE"}
        return {
            "text": text,
            "sentiment": labels[sentiment_id],
            "confidence": f"{confidence:.2%}"
        }

if __name__ == "__main__":
    engine = EcoSentientEngine()
    test_text = "The labor market shows resilience despite inflationary pressures in the tech sector."
    result = engine.analyze_economic_text(test_text)
    print(f"Analysis Results: {result}")
