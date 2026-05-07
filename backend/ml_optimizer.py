import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import os
import pickle

class BudgetOptimizer:
    def __init__(self):
        self.model_path = "budget_model.pkl"
        self.categories = ["Venue", "Food & Catering", "Decor & Setup", "Photography", "Misc/Entertainment"]
        self.model = None
        self.event_map = {
            "Wedding": 0, "Reception": 0, "Engagement": 0, "Sangeet": 0, "Mehendi": 0, "Haldi": 0, 
            "Corporate Conference": 1, "Product Launch": 1, "Team Building Offsite": 1, 
            "Award Ceremony": 1, "Networking Event": 1, "Trade Show": 1,
            "Birthday (Kids)": 2, "Birthday (Adults)": 2, "Anniversary": 2, 
            "Baby Shower / Godhbharai": 2, "Housewarming / Griha Pravesh": 2, 
            "Retirement Party": 2, "Alumni Meet": 2, "Charity Gala": 1, "Musical Concert": 1
        }
        self._load_or_train_model()

    def _generate_dummy_data(self):
        # Generate dummy data for training
        np.random.seed(42)
        n_samples = 50
        data = {
            "budget": np.random.uniform(50000, 10000000, n_samples),
            "event_type_encoded": np.random.choice([0, 1, 2], n_samples), # 0: Wedding/Traditional, 1: Corporate/Formal, 2: Casual/Party
        }
        df = pd.DataFrame(data)
        
        # Target: percentage allocations based on event type
        # 0 (Wedding): Venue 30%, Food 35%, Decor 20%, Photography 10%, Misc 5%
        # 1 (Corporate): Venue 40%, Food 30%, Decor 10%, Photography 10%, Misc 10%
        # 2 (Casual): Venue 20%, Food 40%, Decor 20%, Photography 10%, Misc 10%
        
        y_data = []
        for _, row in df.iterrows():
            if row["event_type_encoded"] == 0:
                y = [0.30, 0.35, 0.20, 0.10, 0.05]
            elif row["event_type_encoded"] == 1:
                y = [0.40, 0.30, 0.10, 0.10, 0.10]
            else:
                y = [0.20, 0.40, 0.20, 0.10, 0.10]
            
            # add some noise
            noise = np.random.normal(0, 0.03, 5)
            y = np.clip(y + noise, 0, 1)
            y = y / y.sum() # normalize
            y_data.append(y)
            
        y_df = pd.DataFrame(y_data, columns=self.categories)
        return df, y_df

    def _load_or_train_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            X, y = self._generate_dummy_data()
            self.model = RandomForestRegressor(n_estimators=50, random_state=42)
            self.model.fit(X, y)
            with open(self.model_path, "wb") as f:
                pickle.dump(self.model, f)

    def predict_allocation(self, budget: float, event_type: str) -> dict:
        event_type_encoded = self.event_map.get(event_type, 0)
        
        X_pred = pd.DataFrame({"budget": [budget], "event_type_encoded": [event_type_encoded]})
        pred_percentages = self.model.predict(X_pred)[0]
        
        pred_percentages = pred_percentages / pred_percentages.sum()
        
        breakdown = []
        for cat, perc in zip(self.categories, pred_percentages):
            breakdown.append({
                "category": cat,
                "percentage": float(perc * 100),
                "allocated_amount": float(budget * perc)
            })
            
        return breakdown
