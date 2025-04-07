import React, { useState } from 'react';
import { Upload, Users, FileText, Calendar, Brain } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('upload');

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
          <h1 className="text-2xl font-bold text-gray-900">AI Recruitment Assistant</h1>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow">
          {/* Navigation Tabs */}
          <nav className="flex space-x-4 p-4 border-b">
            <button
              onClick={() => setActiveTab('upload')}
              className={`flex items-center px-3 py-2 rounded-md text-sm font-medium ${
                activeTab === 'upload'
                  ? 'bg-blue-100 text-blue-700'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              <Upload className="w-4 h-4 mr-2" />
              Upload Documents
            </button>
            <button
              onClick={() => setActiveTab('jd')}
              className={`flex items-center px-3 py-2 rounded-md text-sm font-medium ${
                activeTab === 'jd'
                  ? 'bg-blue-100 text-blue-700'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              <FileText className="w-4 h-4 mr-2" />
              Job Descriptions
            </button>
            <button
              onClick={() => setActiveTab('candidates')}
              className={`flex items-center px-3 py-2 rounded-md text-sm font-medium ${
                activeTab === 'candidates'
                  ? 'bg-blue-100 text-blue-700'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              <Users className="w-4 h-4 mr-2" />
              Candidates
            </button>
            <button
              onClick={() => setActiveTab('interviews')}
              className={`flex items-center px-3 py-2 rounded-md text-sm font-medium ${
                activeTab === 'interviews'
                  ? 'bg-blue-100 text-blue-700'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              <Calendar className="w-4 h-4 mr-2" />
              Interviews
            </button>
          </nav>

          {/* Content Area */}
          <div className="p-6">
            {activeTab === 'upload' && (
              <div className="space-y-6">
                <div className="border-2 border-dashed border-gray-300 rounded-lg p-12 text-center">
                  <Upload className="mx-auto h-12 w-12 text-gray-400" />
                  <div className="mt-4">
                    <label
                      htmlFor="file-upload"
                      className="cursor-pointer rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-500"
                    >
                      Upload Files
                      <input id="file-upload" type="file" className="hidden" multiple />
                    </label>
                  </div>
                  <p className="mt-2 text-sm text-gray-500">
                    Drop your JDs and CVs here or click to browse
                  </p>
                </div>
              </div>
            )}

            {activeTab === 'jd' && (
              <div className="space-y-4">
                <h2 className="text-lg font-semibold text-gray-900">Active Job Descriptions</h2>
                <div className="border rounded-lg divide-y">
                  {/* Sample JD Item */}
                  <div className="p-4 flex items-center justify-between">
                    <div>
                      <h3 className="font-medium">Senior Software Engineer</h3>
                      <p className="text-sm text-gray-500">Posted 2 days ago</p>
                    </div>
                    <button className="text-blue-600 hover:text-blue-800">View Details</button>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'candidates' && (
              <div className="space-y-4">
                <h2 className="text-lg font-semibold text-gray-900">Shortlisted Candidates</h2>
                <div className="border rounded-lg divide-y">
                  {/* Sample Candidate Item */}
                  <div className="p-4 flex items-center justify-between">
                    <div>
                      <h3 className="font-medium">John Doe</h3>
                      <p className="text-sm text-gray-500">Match Score: 95%</p>
                    </div>
                    <div className="flex space-x-2">
                      <button className="text-green-600 hover:text-green-800">Schedule Interview</button>
                      <button className="text-blue-600 hover:text-blue-800">View Profile</button>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'interviews' && (
              <div className="space-y-4">
                <h2 className="text-lg font-semibold text-gray-900">Scheduled Interviews</h2>
                <div className="border rounded-lg divide-y">
                  {/* Sample Interview Item */}
                  <div className="p-4 flex items-center justify-between">
                    <div>
                      <h3 className="font-medium">Interview with Jane Smith</h3>
                      <p className="text-sm text-gray-500">Tomorrow at 2:00 PM</p>
                    </div>
                    <button className="text-blue-600 hover:text-blue-800">View Details</button>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;