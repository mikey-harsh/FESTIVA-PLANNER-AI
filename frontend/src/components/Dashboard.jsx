import './Dashboard.css';

export default function Dashboard({ data, onReset }) {
  const { event_plan, budget_breakdown, knowledge_insights } = data;

  return (
    <div className="dashboard-container animate-fade-in">
      <div className="dashboard-header">
        <h2>Your Event Plan is Ready!</h2>
        <button className="btn outline-btn" onClick={onReset}>Plan Another Event</button>
      </div>

      <div className="dashboard-grid">
        <div className="glass-panel theme-panel">
          <h3>Theme Suggestion</h3>
          <p className="text-gradient theme-text">{event_plan.overall_theme_suggestion}</p>
        </div>

        <div className="glass-panel budget-panel">
          <h3>Budget Breakdown</h3>
          <div className="budget-list">
            {budget_breakdown.map((item, index) => (
              <div key={index} className="budget-item">
                <div className="budget-info">
                  <span className="budget-cat">{item.category}</span>
                  <span className="budget-perc">{item.percentage.toFixed(1)}%</span>
                </div>
                <div className="progress-bar-container">
                  <div 
                    className="progress-bar" 
                    style={{ width: `${item.percentage}%` }}
                  ></div>
                </div>
                <div className="budget-amount">₹{item.allocated_amount.toLocaleString()}</div>
              </div>
            ))}
          </div>
        </div>

        <div className="glass-panel timeline-panel">
          <h3>Timeline & Tasks</h3>
          <ul className="timeline-list">
            {event_plan.timeline.map((item, index) => (
              <li key={index} className="timeline-item">
                <span className="timeline-time">{item.timeline}</span>
                <span className="timeline-task">{item.task}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="glass-panel vendors-panel">
          <h3>Vendors Needed</h3>
          <ul className="vendor-list">
            {event_plan.vendors_needed.map((item, index) => (
              <li key={index} className="vendor-item">
                <span className="vendor-cat">{item.category}</span>
                <p className="vendor-desc">{item.description}</p>
              </li>
            ))}
          </ul>
        </div>

        <div className="glass-panel insights-panel">
          <h3>Knowledge Agent Insights</h3>
          <p className="insights-text">{knowledge_insights}</p>
        </div>
      </div>
    </div>
  );
}
