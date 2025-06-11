import React, { useEffect, useState } from 'react';

function App() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/employees")
      .then((res) => res.json())
      .then(setEmployees);
  }, []);

  return (
    <div>
      <h1>Liste des employés</h1>
      <ul>
        {employees.map((emp) => (
          <li key={emp.id}>{emp.name} - {emp.role}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
