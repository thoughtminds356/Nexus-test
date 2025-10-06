import React, { useState, useEffect } from 'react';
import { agentAPI } from '../services/api';
import './AgentTable.css';

const AgentTable = () => {
  const [agents, setAgents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterType, setFilterType] = useState('ALL');

  useEffect(() => {
    fetchAgents();
  }, []);

  const fetchAgents = async () => {
    try {
      setLoading(true);
      const response = await agentAPI.getAll();
      const agentData = response.data.results || response.data;
      setAgents(Array.isArray(agentData) ? agentData : []);
      setError(null);
    } catch (err) {
      console.error('Error fetching agents:', err);
      setError('Failed to fetch agents. Please check if the backend is running.');
      setAgents([]);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (agentId) => {
    if (window.confirm('Are you sure you want to delete this agent?')) {
      try {
        await agentAPI.delete(agentId);
        await fetchAgents(); // Refresh the list
      } catch (err) {
        console.error('Error deleting agent:', err);
        alert('Failed to delete agent');
      }
    }
  };

  const filteredAgents = agents.filter(agent => {
    const matchesSearch = agent.agent_name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         agent.agent_short_desc?.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesType = filterType === 'ALL' || agent.agent_type === filterType;
    return matchesSearch && matchesType;
  });

  const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleDateString();
  };

  const truncateText = (text, maxLength = 50) => {
    if (!text) return 'N/A';
    return text.length > maxLength ? `${text.substring(0, maxLength)}...` : text;
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading agents...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <div className="error-message">
          <h3>⚠️ Error</h3>
          <p>{error}</p>
          <button onClick={fetchAgents} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="agent-table-container">
      <div className="table-header">
        <h1>Agents Management</h1>
        <div className="table-controls">
          <input
            type="text"
            placeholder="Search agents..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
          <select
            value={filterType}
            onChange={(e) => setFilterType(e.target.value)}
            className="filter-select"
          >
            <option value="ALL">All Types</option>
            <option value="BOT">Bot</option>
            <option value="SITE">Site</option>
          </select>
          <button onClick={fetchAgents} className="refresh-button">
            🔄 Refresh
          </button>
        </div>
      </div>

      {filteredAgents.length === 0 ? (
        <div className="no-data">
          <p>No agents found. {searchTerm || filterType !== 'ALL' ? 'Try adjusting your filters.' : ''}</p>
        </div>
      ) : (
        <div className="table-wrapper">
          <table className="agent-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Short Description</th>
                <th>Problem</th>
                <th>Solution</th>
                <th>Video</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredAgents.map((agent) => (
                <tr key={agent.id}>
                  <td className="agent-name">
                    <strong>{agent.agent_name || 'Unnamed Agent'}</strong>
                  </td>
                  <td>
                    <span className={`type-badge ${agent.agent_type?.toLowerCase()}`}>
                      {agent.agent_type || 'N/A'}
                    </span>
                  </td>
                  <td className="description">
                    {truncateText(agent.agent_short_desc)}
                  </td>
                  <td className="problem">
                    {truncateText(agent.problem)}
                  </td>
                  <td className="solution">
                    {truncateText(agent.solution)}
                  </td>
                  <td className="video">
                    {agent.video_file ? (
                      <a 
                        href={agent.video_file} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="video-link"
                      >
                        📹 View Video
                      </a>
                    ) : (
                      <span className="no-video">No video</span>
                    )}
                  </td>
                  <td className="actions">
                    <button
                      onClick={() => console.log('Edit agent:', agent.id)}
                      className="edit-button"
                      title="Edit Agent"
                    >
                      ✏️
                    </button>
                    <button
                      onClick={() => handleDelete(agent.id)}
                      className="delete-button"
                      title="Delete Agent"
                    >
                      🗑️
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <div className="table-footer">
        <p>Total agents: {filteredAgents.length}</p>
      </div>
    </div>
  );
};

export default AgentTable;