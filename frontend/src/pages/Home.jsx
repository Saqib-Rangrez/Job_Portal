import React, { useState, useEffect } from 'react';
import Navbar from '../components/Navbar';
import FilterBar from '../components/FilterBar';
import JobList from '../components/JobList';
import axios from 'axios';
import JobCard from '../components/JobCard';

const Home = () => {
  const [jobs, setJobs] = useState([]);
  const [filteredJobs, setFilteredJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/jobs/')
      .then((response) => {
        setJobs(response.data);
        setFilteredJobs(response.data);  // Initialize filteredJobs with all jobs
        setLoading(false);
      })
      .catch((err) => {
        setError('Failed to fetch jobs.');
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="bg-gray-100">
      <Navbar />
      <div className="container mx-auto px-4 py-8 max-w-7xl">
        <FilterBar jobs={jobs} setFilteredJobs={setFilteredJobs} />
        <JobList jobs={filteredJobs} />
      </div>
    </div>
  );
};

export default Home;