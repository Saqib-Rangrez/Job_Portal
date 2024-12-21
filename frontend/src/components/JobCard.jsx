import React from 'react';
import { FiGlobe, FiClock, FiDollarSign, FiMapPin, FiBriefcase } from 'react-icons/fi';
import { FaBuilding } from 'react-icons/fa';

const JobCard = ({ job }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg p-6 mb-6 hover:shadow-xl transition-all ease-in-out duration-300">
      <div className="flex items-center mb-6">
        <div className="h-16 w-16 mr-6 rounded-full flex justify-center items-center bg-gray-200 shadow-lg">
          {job.company_logo_url ? (
            <img
              src={job.company_logo_url}
              alt="Company Logo"
              className="h-full w-full object-cover rounded-full"
            />
          ) : (
            <FaBuilding className="text-gray-600 text-4xl" />
          )}
        </div>

        <div>
          <h3 className="text-2xl font-semibold text-gray-800 mb-1">{job.title || 'Job Title Not Provided'}</h3>
          <p className="text-md text-gray-500 mb-2">{job.company_name || 'Company Name Not Provided'}</p>
          <a
            href={job.company_page_url || '#'}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-500 hover:text-blue-700 text-sm"
          >
            {job.company_page_url ? 'View Company Profile' : 'Company Profile Not Available'}
          </a>
        </div>
      </div>

      <div className="space-y-3 mb-6">
        <div className="flex items-center text-gray-600">
          <FiBriefcase className="mr-2" />
          <span>{job.employer_type || 'Employer Type Not Provided'}</span>
        </div>
        <div className="flex items-center text-gray-600">
          <FiClock className="mr-2" />
          <span>{job.employment_type || 'Employment Type Not Provided'}</span>
        </div>
        <div className="flex items-center text-gray-600">
          <FiMapPin className="mr-2" />
          <span>{job.location || 'Location Not Provided'}</span>
        </div>
        {job.work_from_home && (
          <div className="flex items-center text-gray-600">
            <FiGlobe className="mr-2" />
            <span>Work from Home Available</span>
          </div>
        )}
      </div>

      <div className="mb-6">
        <h4 className="font-semibold text-gray-800">Job Description</h4>
        <p className="text-gray-600 text-sm line-clamp-3">
          {job.summary || 'Job summary not provided. Please visit the job link for more details.'}
        </p>
        <a
          href={job.details_page_url || '#'}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-500 hover:text-blue-700 text-sm mt-2 block"
        >
          {job.details_page_url ? 'Read Full Job Description' : 'No Job Description Available'}
        </a>
      </div>

      <div className="flex justify-between items-center mt-6">
        <span className="text-lg font-semibold text-gray-800">
          {job.salary || 'Salary Not Disclosed'}
        </span>
        <span className="text-md text-gray-600">
          {job.willing_to_sponsor ? 'Visa Sponsorship Available' : 'No Visa Sponsorship'}
        </span>
      </div>
    </div>
  );
};

export default JobCard;
