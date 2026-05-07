import { useState } from 'react'
import EventForm from './components/EventForm'
import Dashboard from './components/Dashboard'
import './App.css'

function App() {
  const [planData, setPlanData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleGeneratePlan = async (formData) => {
    setLoading(true);
    setError(null);
    try {
      const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      const response = await fetch(`${API_URL}/api/plan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          event_type: formData.eventType,
          budget: parseFloat(formData.budget),
          city: formData.city,
          preferences: formData.preferences
        })
      });

      if (!response.ok) {
        throw new Error('Failed to generate plan');
      }

      const data = await response.json();
      setPlanData(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="header animate-fade-in">
        <h1>Festiva Planner <span className="text-gradient">AI</span></h1>
        <p className="subtitle">Intelligent event planning powered by Agents & Machine Learning</p>
      </header>

      <main className="main-content">
        {!planData ? (
          <EventForm onSubmit={handleGeneratePlan} loading={loading} error={error} />
        ) : (
          <Dashboard data={planData} onReset={() => setPlanData(null)} />
        )}
      </main>
    </div>
  )
}

export default App
