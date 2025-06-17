import { useState } from 'react';

const CodeAnalysis = () => {
  const [code, setCode] = useState('');
  const [instructions, setInstructions] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [mode, setMode] = useState('analyze'); // 'analyze' or 'refactor'

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8000/api/code/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code }),
      });
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleRefactor = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8000/api/code/refactor', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code, instructions }),
      });
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto mt-10 p-6 bg-white rounded-lg shadow-lg">
      <h2 className="text-2xl font-bold mb-4">Code Analysis & Refactoring</h2>

      <div className="mb-4">
        <div className="flex space-x-4 mb-4">
          <button
            onClick={() => setMode('analyze')}
            className={`px-4 py-2 rounded ${
              mode === 'analyze' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
          >
            Analyze Code
          </button>
          <button
            onClick={() => setMode('refactor')}
            className={`px-4 py-2 rounded ${
              mode === 'refactor' ? 'bg-blue-500 text-white' : 'bg-gray-200'
            }`}
          >
            Refactor Code
          </button>
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Code
          </label>
          <textarea
            value={code}
            onChange={(e) => setCode(e.target.value)}
            className="w-full h-48 p-2 border rounded"
            placeholder="Paste your code here..."
          />
        </div>

        {mode === 'refactor' && (
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Refactoring Instructions
            </label>
            <textarea
              value={instructions}
              onChange={(e) => setInstructions(e.target.value)}
              className="w-full h-24 p-2 border rounded"
              placeholder="Enter refactoring instructions..."
            />
          </div>
        )}

        <button
          onClick={mode === 'analyze' ? handleAnalyze : handleRefactor}
          disabled={loading}
          className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors disabled:bg-blue-300"
        >
          {loading ? 'Processing...' : mode === 'analyze' ? 'Analyze Code' : 'Refactor Code'}
        </button>
      </div>

      {error && (
        <div className="mt-4 p-3 bg-red-100 text-red-700 rounded">
          {error}
        </div>
      )}

      {result && (
        <div className="mt-4">
          <h3 className="text-xl font-semibold mb-2">Result:</h3>
          <div className="p-4 bg-gray-50 rounded">
            {mode === 'analyze' ? (
              <pre className="whitespace-pre-wrap">{result.analysis}</pre>
            ) : (
              <>
                <h4 className="font-medium mb-2">Refactored Code:</h4>
                <pre className="whitespace-pre-wrap bg-gray-100 p-4 rounded mb-4">
                  {result.refactored_code}
                </pre>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default CodeAnalysis;