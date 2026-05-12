import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGKnowledgeBase:
    def __init__(self):
        self.data_dir = "knowledge_data"
        self.documents = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self._load_local_data()

    def _load_local_data(self):
        # Instantly loads your .txt guides from the folder
        if os.path.exists(self.data_dir):
            for filename in os.listdir(self.data_dir):
                if filename.endswith(".txt"):
                    filepath = os.path.join(self.data_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        self.documents.append(f.read())
            
            if self.documents:
                self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
                print(f"✅ Local Knowledge Engine Ready ({len(self.documents)} guides loaded)")

    def query(self, question: str, k: int = 1) -> str:
        # Uses local math to find the right guide in 0ms
        if not self.documents or self.tfidf_matrix is None:
            return "Standard Indian Event Guidelines."
            
        query_vec = self.vectorizer.transform([question])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        best_index = np.argmax(scores)
        
        if scores[best_index] > 0.1:
            return self.documents[best_index][:1000]
        return "Standard Indian Event Guidelines."