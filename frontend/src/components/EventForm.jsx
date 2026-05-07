import { useState } from 'react';
import './EventForm.css';

export default function EventForm({ onSubmit, loading, error }) {
  const [formData, setFormData] = useState({
    eventType: 'Wedding',
    budget: '',
    city: '',
    preferences: ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const eventsList = [
    "Wedding", "Reception", "Engagement", "Sangeet", "Mehendi", "Haldi", 
    "Corporate Conference", "Product Launch", "Team Building Offsite", 
    "Award Ceremony", "Networking Event", "Trade Show",
    "Birthday (Kids)", "Birthday (Adults)", "Anniversary", 
    "Baby Shower / Godhbharai", "Housewarming / Griha Pravesh", 
    "Retirement Party", "Alumni Meet", "Charity Gala", "Musical Concert"
  ];

  return (
    <div className="form-wrapper glass-panel animate-fade-in">
      <h2>Plan Your Event</h2>
      {error && <div className="error-message">{error}</div>}
      
      <form onSubmit={handleSubmit} className="event-form">
        <div className="input-group">
          <label>Event Type</label>
          <select name="eventType" value={formData.eventType} onChange={handleChange}>
            {eventsList.map(evt => <option key={evt} value={evt}>{evt}</option>)}
          </select>
        </div>

        <div className="input-group">
          <label>Budget (₹)</label>
          <input 
            type="number" 
            name="budget" 
            placeholder="e.g. 1000000" 
            value={formData.budget} 
            onChange={handleChange}
            required
            min="1000"
          />
        </div>

        <div className="input-group">
          <label>City (India)</label>
          <input 
            type="text" 
            name="city" 
            list="cities"
            placeholder="e.g. Mumbai, Bangalore, Delhi..." 
            value={formData.city} 
            onChange={handleChange}
            required
          />
          <datalist id="cities">
            <option value="Mumbai" />
            <option value="Delhi" />
            <option value="Bangalore" />
            <option value="Hyderabad" />
            <option value="Ahmedabad" />
            <option value="Chennai" />
            <option value="Kolkata" />
            <option value="Surat" />
            <option value="Pune" />
            <option value="Jaipur" />
            <option value="Lucknow" />
            <option value="Kanpur" />
            <option value="Nagpur" />
            <option value="Indore" />
            <option value="Thane" />
            <option value="Bhopal" />
            <option value="Visakhapatnam" />
            <option value="Pimpri-Chinchwad" />
            <option value="Patna" />
            <option value="Vadodara" />
            <option value="Ghaziabad" />
            <option value="Ludhiana" />
            <option value="Agra" />
            <option value="Nashik" />
            <option value="Faridabad" />
            <option value="Meerut" />
            <option value="Rajkot" />
            <option value="Kalyan-Dombivli" />
            <option value="Vasai-Virar" />
            <option value="Varanasi" />
            <option value="Srinagar" />
            <option value="Aurangabad" />
            <option value="Dhanbad" />
            <option value="Amritsar" />
            <option value="Navi Mumbai" />
            <option value="Allahabad" />
            <option value="Ranchi" />
            <option value="Howrah" />
            <option value="Coimbatore" />
            <option value="Jabalpur" />
            <option value="Gwalior" />
            <option value="Vijayawada" />
            <option value="Jodhpur" />
            <option value="Madurai" />
            <option value="Raipur" />
            <option value="Kota" />
            <option value="Guwahati" />
            <option value="Chandigarh" />
            <option value="Solapur" />
            <option value="Hubballi-Dharwad" />
            <option value="Mysore" />
            <option value="Tiruchirappalli" />
            <option value="Bareilly" />
            <option value="Aligarh" />
            <option value="Tiruppur" />
            <option value="Gurgaon" />
            <option value="Moradabad" />
            <option value="Jalandhar" />
            <option value="Bhubaneswar" />
            <option value="Salem" />
            <option value="Warangal" />
            <option value="Guntur" />
            <option value="Bhiwandi" />
            <option value="Saharanpur" />
            <option value="Gorakhpur" />
            <option value="Bikaner" />
            <option value="Amravati" />
            <option value="Noida" />
            <option value="Jamshedpur" />
            <option value="Bhilai" />
            <option value="Cuttack" />
            <option value="Firozabad" />
            <option value="Kochi" />
            <option value="Nellore" />
            <option value="Bhavnagar" />
            <option value="Dehradun" />
            <option value="Durgapur" />
            <option value="Asansol" />
            <option value="Rourkela" />
            <option value="Nanded" />
            <option value="Kolhapur" />
            <option value="Ajmer" />
            <option value="Akola" />
            <option value="Gulbarga" />
            <option value="Jamnagar" />
            <option value="Ujjain" />
            <option value="Loni" />
            <option value="Siliguri" />
            <option value="Jhansi" />
            <option value="Ulhasnagar" />
            <option value="Jammu" />
            <option value="Sangli-Miraj & Kupwad" />
            <option value="Mangalore" />
            <option value="Erode" />
            <option value="Belgaum" />
            <option value="Kurnool" />
            <option value="Ambattur" />
            <option value="Rajahmundry" />
            <option value="Tirunelveli" />
            <option value="Malegaon" />
            <option value="Gaya" />
            <option value="Udaipur" />
            <option value="Kakinada" />
            <option value="Davanagere" />
            <option value="Kozhikode" />
            <option value="Maheshtala" />
            <option value="Rajpur Sonarpur" />
            <option value="Bokaro" />
            <option value="South Dumdum" />
            <option value="Bellary" />
            <option value="Patiala" />
            <option value="Gopalpur" />
            <option value="Agartala" />
            <option value="Bhagalpur" />
            <option value="Muzaffarnagar" />
            <option value="Bhatpara" />
            <option value="Panihati" />
            <option value="Latur" />
            <option value="Dhule" />
            <option value="Rohtak" />
            <option value="Korba" />
            <option value="Bhilwara" />
            <option value="Berhampur" />
            <option value="Muzaffarpur" />
            <option value="Ahmednagar" />
            <option value="Mathura" />
            <option value="Kollam" />
            <option value="Avadi" />
            <option value="Kadapa" />
            <option value="Kamarhati" />
            <option value="Sambalpur" />
            <option value="Bilaspur" />
            <option value="Shahjahanpur" />
            <option value="Satara" />
            <option value="Bijapur" />
            <option value="Kampur" />
            <option value="Shimla" />
            <option value="Panaji" />
          </datalist>
        </div>

        <div className="input-group">
          <label>Preferences</label>
          <textarea 
            name="preferences" 
            placeholder="e.g. Traditional setup, 500 guests, mostly vegetarian food" 
            value={formData.preferences} 
            onChange={handleChange}
            rows="4"
            required
          />
        </div>

        <button type="submit" className="btn submit-btn" disabled={loading}>
          {loading ? <span className="loader"></span> : 'Generate Plan'}
        </button>
      </form>
    </div>
  );
}
