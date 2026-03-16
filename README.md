# EcoSentient-NLP ðŸŒðŸ“ˆ
**Multi-Dimensional Economic Sentiment & Labor Market Analysis Engine**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/)
[![EconomicAI](https://img.shields.io/badge/Economic-AI-green.svg)](https://github.com/AI-TashaTorchon)

## **Project Overview**
**EcoSentient-NLP** is a specialized analytical engine designed to bridge the gap between **Linguistic Syntax**, **Applied Economics**, and **Transformer-based Deep Learning**. 

As an AI/ML Engineer with a background in both Linguistics (Yale) and Economics (UMich), I developed this tool to analyze how labor market trends and economic sentiments are reflected in complex textual data. Unlike standard sentiment analysis, EcoSentient-NLP accounts for linguistic markers and lexical density to provide high-precision economic insights.

---

## **Key Architecture**
The engine is built on two primary modules:
1.  **`EcoSentientEngine`**: A fine-tuned DistilBERT-based model optimized for detecting expansive vs. contradictory economic sentiments.
2.  **`EconomicLinguistics`**: A utility suite that leverages NLTK to perform lexical density analysis and keyword marker extraction, specifically for labor market discourse.

---

## **Features**
-   ðŸš€ **Economic Sentiment Analysis**: Detect shifts in market confidence through textual analysis.
-   ðŸ”¡ **Linguistic Contextualization**: Extract specific economic markers and analyze lexical complexity.
-   ðŸ§  **Transformer-Powered**: Utilizes state-of-the-art NLP via the HuggingFace `transformers` library.
-   âš™ï¸ **Highly Modular**: Designed for easy integration into larger socioeconomic research pipelines.

---

## **Installation**

Clone the repository and install dependencies:

```bash
git clone https://github.com/AI-TashaTorchon/EcoSentient-NLP.git
cd EcoSentient-NLP
pip install -r requirements.txt
```

---

## **Example Usage**

```python
from sentiment_engine import EcoSentientEngine
from linguistic_utils import EconomicLinguistics

# Initialize the engine and utils
engine = EcoSentientEngine()
utils = EconomicLinguistics()

text = "The job market is experiencing significant growth in AI-driven sectors despite cautious hiring in traditional industries."

# 1. Sentiment Analysis
sentiment = engine.analyze_economic_text(text)
print(f"Economic Sentiment: {sentiment['sentiment']} (Confidence: {sentiment['confidence']})")

# 2. Linguistic Extraction
markers = utils.extract_economic_markers(text)
density = utils.analyze_lexical_density(text)

print(f"Economic Markers Found: {markers}")
print(f"Lexical Density: {density}")
```

---

## **Why This Project?**
This project serves as a showcase of my ability to apply **Interdisciplinary AI**. By combining the structural rigor of Linguistics with the predictive goals of Economics, EcoSentient-NLP represents a holistic approach to understanding data that goes beyond mere pattern matching.

---

## **Connect & Contribute**
I am always open to discussing AI ethics, labor market research, and NLP innovations.

-   **LinkedIn:** [Tasha Torchon](https://www.linkedin.com/in/tasha-torchon/)
-   **Portfolio:** [AI-TashaTorchon](https://github.com/AI-TashaTorchon)

---

> "At the intersection of language and data lies the truth of human impact."

---
*Disclaimer: This tool is for research purposes and should not be used as the sole basis for financial or policy decisions.*
