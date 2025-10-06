import React, { useState, useEffect } from 'react';
import { departmentAPI } from '../services/api';
import './DepartmentTable.css';

const DepartmentTable = () => {
  const [departments, setDepartments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    fetchDepartments();
  }, []);

  const fetchDepartments = async () => {
    try {
      setLoading(true);
      const response = await departmentAPI.getAll();
      const departmentData = response.data.results || response.data;
      setDepartments(Array.isArray(departmentData) ? departmentData : []);
      setError(null);
    } catch (err) {
      console.error('Error fetching departments:', err);
      setError('Failed to fetch departments. Please check if the backend is running.');
      setDepartments([]);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (departmentId) => {
    if (window.confirm('Are you sure you want to delete this department?')) {
      try {
        await departmentAPI.delete(departmentId);
        await fetchDepartments(); // Refresh the list
      } catch (err) {
        console.error('Error deleting department:', err);
        alert('Failed to delete department');
      }
    }
  };

  const filteredDepartments = departments.filter(department =>
    department.name?.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading departments...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <div className="error-message">
          <h3>⚠️ Error</h3>
          <p>{error}</p>
          <button onClick={fetchDepartments} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="department-table-container">
      <div className="table-header">
        <h2>Departments</h2>
        <div className="table-controls">
          <input
            type="text"
            placeholder="Search departments..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
          <button onClick={fetchDepartments} className="refresh-button">
            🔄 Refresh
          </button>
        </div>
      </div>

      {filteredDepartments.length === 0 ? (
        <div className="no-data">
          <p>No departments found. {searchTerm ? 'Try adjusting your search.' : ''}</p>
        </div>
      ) : (
        <div className="table-wrapper">
          <table className="department-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredDepartments.map((department) => (
                <tr key={department.id}>
                  <td className="department-id">
                    <code>{department.id}</code>
                  </td>
                  <td className="department-name">
                    <strong>{department.name || 'Unnamed Department'}</strong>
                  </td>
                  <td className="actions">
                    <button
                      onClick={() => console.log('Edit department:', department.id)}
                      className="edit-button"
                      title="Edit Department"
                    >
                      ✏️
                    </button>
                    <button
                      onClick={() => handleDelete(department.id)}
                      className="delete-button"
                      title="Delete Department"
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
        <p>Total departments: {filteredDepartments.length}</p>
      </div>
    </div>
  );
};

export default DepartmentTable;