from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class RAGKnowledgeBase:
    def __init__(self):
        self.data_dir = "knowledge_data"
        self.index_path = "faiss_index"
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = None
        
        self._ensure_data_exists()
        self._load_or_build_index()

    def _ensure_data_exists(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            
        dummy_guides = {
            "indian_vendor_directory.txt": """
# Indian Vendor Directory
## Mumbai
Venues: The Taj Mahal Palace, Sahara Star, ITC Maratha. Caterers: Mini Punjab Catering, Foodlink. Decor: National Decorators. Photography: The Wedding Story.
## Delhi
Venues: Taj Palace, ITC Maurya, The Leela Ambience. Caterers: Saltt Catering, The Kitchen Art Co. Decor: Ferns N Petals. Photography: Badal Raja Company.
## Bangalore
Venues: The Leela Palace, Taj West End, Bangalore Palace Grounds. Caterers: Sagar Caterers, Sri Udupi Caterers. Decor: Ohana Fine Events. Photography: Lightbucket Productions.
## Hyderabad
Venues: Taj Falaknuma Palace, ITC Kakatiya. Caterers: Fusion Hospitality, Vantillu Caterers. Decor: Minttu Decorators. Photography: RVR Pro.
## Chennai
Venues: ITC Grand Chola, Mayor Ramanathan Chettiar Hall. Caterers: A2B Catering, Saraswathi Caterers. Decor: Marriage Colours. Photography: Studio A.
## General Guidelines for Any Indian City
If a specific city is not listed above, infer realistic local Indian names for that city (e.g., 'Royal Residency Banquet', 'Shree Krishna Caterers', 'Mahalaxmi Decorators', 'Perfect Click Studios').
Pricing: 5-Star Venues (₹3000-₹5000/plate). Banquets (₹1000-₹2000/plate). Kalyana Mandapams (₹500-₹1000/plate). Photography (₹50k-₹3 Lakhs/day). Decor (₹1 Lakh-₹10 Lakhs).
""",
            "wedding_guide.txt": "Indian weddings span 6-12 months of planning. Booking venues (Mandapams/Banquets) requires 8-10 months lead time, especially during Shubh Muhurat dates. Catering and Decor are finalized 4 months prior.",
            "corporate_guide.txt": "Corporate events require rigid scheduling. Timelines are usually 2-6 months. Key focus areas: A/V equipment, premium hotel venues, catering, and guest speakers.",
            "party_guide.txt": "Birthdays, Anniversaries, and Baby Showers can be planned in 1-2 months. Focus heavily on food and entertainment. Book local banquets or hotel halls."
        }
        
        for filename, content in dummy_guides.items():
            filepath = os.path.join(self.data_dir, filename)
            if not os.path.exists(filepath):
                with open(filepath, "w") as f:
                    f.write(content)

    def _load_or_build_index(self):
        if os.path.exists(self.index_path):
            self.vector_store = FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
        else:
            documents = []
            for filename in os.listdir(self.data_dir):
                if filename.endswith(".txt"):
                    loader = TextLoader(os.path.join(self.data_dir, filename))
                    documents.extend(loader.load())
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            texts = text_splitter.split_documents(documents)
            
            if texts:
                self.vector_store = FAISS.from_documents(texts, self.embeddings)
                self.vector_store.save_local(self.index_path)

    def query(self, question: str, k: int = 2) -> str:
        if not self.vector_store:
            return "Knowledge base not initialized."
        docs = self.vector_store.similarity_search(question, k=k)
        if docs:
            return "\n".join([doc.page_content for doc in docs])
        return "No relevant knowledge found."
