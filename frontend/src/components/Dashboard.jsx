import { useRef } from 'react';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import { Download, RefreshCw, Calendar, PieChart, MapPin, Sparkles } from 'lucide-react';
import './Dashboard.css';

export default function Dashboard({ data, onReset }) {
  const { event_plan, budget_breakdown, knowledge_insights } = data;
  const reportRef = useRef();

  const downloadPDF = async () => {
    const element = reportRef.current;
    
    // 1. Enter Capture Mode
    element.classList.add('pdf-capture-mode');
    
    try {
      const canvas = await html2canvas(element, {
        scale: 2,
        useCORS: true,
        backgroundColor: '#030712',
        logging: false,
        // This ensures we don't capture extra empty space
        scrollY: -window.scrollY 
      });

      const imgData = canvas.toDataURL('image/png');
      
      // 2. Create a PDF that is exactly the size of the content
      // 'px' unit ensures a 1:1 match with the canvas
      const pdf = new jsPDF({
        orientation: canvas.width > canvas.height ? 'l' : 'p',
        unit: 'px',
        format: [canvas.width, canvas.height]
      });

      pdf.addImage(imgData, 'PNG', 0, 0, canvas.width, canvas.height);
      pdf.save('Festiva_Event_Plan.pdf');
      
    } catch (err) {
      console.error("PDF Export Error:", err);
    } finally {
      // 3. Clean up UI
      element.classList.remove('pdf-capture-mode');
    }
  };

  return (
    <div className="dashboard-wrapper animate-fade-in">
      <div className="action-bar">
        <button className="icon-btn" onClick={onReset}><RefreshCw size={18} /> New Plan</button>
        <button className="btn-primary" onClick={downloadPDF}><Download size={18} /> Download PDF</button>
      </div>

      <div ref={reportRef} className="dashboard-content">
        <header className="plan-header glass-panel">
          <Sparkles className="accent-icon" style={{color: 'var(--primary)'}} />
          <p className="label">OFFICIAL EVENT STRATEGY</p>
          <h2 className="theme-title">{event_plan.overall_theme_suggestion}</h2>
        </header>

        <div className="dashboard-grid">
          <section className="glass-panel card-stats">
            <div className="card-title"><PieChart size={20} /> <h3>Budget Allocation</h3></div>
            <div className="b-list">
              {budget_breakdown.map((item, i) => (
                <div key={i} className="b-item">
                  <div className="b-row"><span>{item.category}</span> <span>{item.percentage.toFixed(0)}%</span></div>
                  <div className="b-bar"><div className="b-fill" style={{width: `${item.percentage}%`}}></div></div>
                  <p className="b-price">₹{item.allocated_amount.toLocaleString()}</p>
                </div>
              ))}
            </div>
          </section>

          <section className="glass-panel card-stats">
            <div className="card-title"><Calendar size={20} /> <h3>Operations Timeline</h3></div>
            <div className="timeline-v-list">
              {event_plan.timeline.map((item, i) => (
                <div key={i} className="t-item">
                  <span className="t-dot"></span>
                  <div className="t-info"><strong>{item.timeline}</strong><p>{item.task}</p></div>
                </div>
              ))}
            </div>
          </section>

          <section className="glass-panel full-width">
            <div className="card-title"><MapPin size={20} /> <h3>Expert Insights</h3></div>
            <p className="insights-para">{knowledge_insights}</p>
          </section>
        </div>
      </div>
    </div>
  );
}