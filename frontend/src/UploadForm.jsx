// src/UploadForm.jsx
function UploadForm({ files, handleFileChange, handleUpload, uploadStatus, styles }) {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Image Uploader</h1>

      <input
        type="file"
        accept="image/*"
        multiple
        onChange={handleFileChange}
        style={styles.fileInput}
      />

      <button onClick={handleUpload} style={styles.uploadButton}>
        Upload Files
      </button>

      <p
        style={{
          ...styles.status,
          color: uploadStatus.type === "error" ? "red" : "green",
        }}
      >
        {uploadStatus.message}
      </p>
    </div>
  );
}

export default UploadForm;
