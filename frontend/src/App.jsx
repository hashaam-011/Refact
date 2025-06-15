import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:8000/api/analyze/upload", {
      method: "POST",
      body: formData,
    });

    const json = await res.json();
    alert("Upload success: " + JSON.stringify(json));
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl mb-6">RefactAI Frontend</h1>

      <input
        type="file"
        accept=".zip"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Upload Codebase
      </button>
    </div>
  );
}

export default App;
