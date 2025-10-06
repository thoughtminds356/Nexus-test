import React, { useState } from 'react';
import AgentTable from './components/AgentTable';
import DepartmentTable from './components/DepartmentTable';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('agents');

  return (
    <div className="App">
      <nav className="app-nav">
        <div className="nav-container">
          <h1 className="app-title">Nexus Dashboard</h1>
          <div className="nav-tabs">
            <button
              className={`nav-tab ${activeTab === 'agents' ? 'active' : ''}`}
              onClick={() => setActiveTab('agents')}
            >
              👤 Agents
            </button>
            <button
              className={`nav-tab ${activeTab === 'departments' ? 'active' : ''}`}
              onClick={() => setActiveTab('departments')}
            >
              🏢 Departments
            </button>
          </div>
        </div>
      </nav>
      
      <main className="app-main">
        {activeTab === 'agents' && <AgentTable />}
        {activeTab === 'departments' && <DepartmentTable />}
      </main>
    </div>
  );
}

export default App
