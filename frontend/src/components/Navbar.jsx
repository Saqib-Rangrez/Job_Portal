import React from 'react';

const Navbar = () => {
  return (
    <div className="bg-primary text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">Remote Job Portal</h1>
        <button className="bg-secondary px-4 py-2 rounded-lg">Sign In</button>
      </div>
    </div>
  );
};

export default Navbar;
