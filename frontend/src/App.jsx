import { useState } from "react";
import UploadForm from "./UploadForm";
import styles from "./AppStyles"; // if using separate styles file

function App() {
  const [files, setFiles] = useState([]);
  const [uploadStatus, setUploadStatus] = useState({ message: "", type: "" });
  const [inputKey, setInputKey] = useState(Date.now());

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    setFiles(selectedFiles);
  };

  const handleUpload = () => {
    if (files.length == 0) {
      alert("Please select atleast one image!");
      return;
    }

    console.log("Files to upload:", files);
    files.forEach(f => console.log(f.name, f.type, f.size));

    const formData = new FormData();
    files.forEach((file) => formData.append("images", file));


    setUploadStatus({ message: "Uploading...", type: "" });
    setInputKey(Date.now());

    fetch("/upload", {
      method: "POST",
      body: formData,
      credentials: "include"
    })
      .then(async (res) => {
        const data = await res.text();
        if (res.ok) {
          setUploadStatus({ message: "Upload successful: " + data, type: "success" });
          setFiles([]); // clear selected files
        } else {
          setUploadStatus({ message: "Upload failed: " + data, type: "error" });
        }
      })
      .catch((err) => setUploadStatus({ message: "Upload failed: " + err, type: "error" }));
  };

  return (
    <UploadForm
      files={files}
      handleFileChange={handleFileChange}
      handleUpload={handleUpload}
      uploadStatus={uploadStatus}
      styles={styles}
    />
  );
}

export default App;
