import React, { useState } from 'react';

const FilterBar = ({ jobs, setFilteredJobs }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedFilter, setSelectedFilter] = useState('All');

  // Filter logic
  const filterJobs = () => {
    let filtered = [...jobs];

    // Search Filter
    if (searchTerm) {
      filtered = filtered.filter(job =>
        job.title.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    // Dropdown Filters
    if (selectedFilter === 'Most Recent') {
      filtered = filtered.sort((a, b) => new Date(b.posted_date) - new Date(a.posted_date));
    } else if (selectedFilter === 'High Pay') {
      filtered = filtered.sort((a, b) => parseInt(b.salary.replace(/[^0-9]/g, '')) - parseInt(a.salary.replace(/[^0-9]/g, '')));
    } else if (selectedFilter === 'Low Pay') {
      filtered = filtered.sort((a, b) => parseInt(a.salary.replace(/[^0-9]/g, '')) - parseInt(b.salary.replace(/[^0-9]/g, '')));
    } else if (selectedFilter === 'Remote') {
      filtered = filtered.filter(job => job.work_from_home);
    }

    setFilteredJobs(filtered);
  };

  // Handle search change
  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
    filterJobs();
  };

  // Reset filters
  const handleResetFilters = () => {
    setSearchTerm('');
    setSelectedFilter('All');
    setFilteredJobs(jobs);
  };

  return (
    <div className="bg-white shadow-lg rounded-lg p-4 mb-6 flex justify-between items-center">
      <div className="relative w-[90%]">
        <input
          type="text"
          placeholder="Search by Job Title"
          className="border rounded-md p-2 w-full"
          value={searchTerm}
          onChange={handleSearch}
        />
      </div>
      {/* <div className="relative inline-block text-left">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-lg focus:outline-none"
          onClick={() => document.getElementById('filter-dropdown').classList.toggle('hidden')}
        >
          Filters ▼
        </button>
        <div
          id="filter-dropdown"
          className="absolute right-0 mt-2 w-48 bg-white shadow-lg rounded-lg hidden"
        >
          <div className="p-2">
            <select
              className="border p-2 rounded-lg w-full"
              value={selectedFilter}
              onChange={(e) => setSelectedFilter(e.target.value)}
            >
              <option value="All">All Jobs</option>
              <option value="Most Recent">Most Recent</option>
              <option value="High Pay">High Pay</option>
              <option value="Low Pay">Low Pay</option>
              <option value="Remote">Remote Only</option>
            </select>
          </div>
        </div>
      </div> */}
      <button
        className="ml-4 bg-gray-500 text-white px-4 py-2 rounded-lg"
        onClick={handleSearch}
      >
        Search
      </button>
    </div>
  );
};

export default FilterBar;
