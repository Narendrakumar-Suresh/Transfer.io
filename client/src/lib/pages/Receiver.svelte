<script>
  let enteredCode = "";
  let isDownloading = false; // Track download state
  let alertMessage = "";
  let showAlert = false;

  async function receiveFile() {
    if (!enteredCode) {
      alertMessage = "Please enter a code.";
      showAlert = true;
      return;
    }

    const formData = new FormData();
    formData.append("code", enteredCode);

    console.log("Entered code:", enteredCode);

    isDownloading = true; // Disable button while downloading
    showAlert = false; // Hide any previous alerts

    try {
      const response = await fetch("https://transfer-io.onrender.com/receive", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);

        // Set filename from response if available, otherwise use a default
        const contentDisposition = response.headers.get("Content-Disposition");
        let filename = "received_file_name";
        if (contentDisposition && contentDisposition.includes("filename=")) {
          filename = contentDisposition
            .split("filename=")[1]
            .replace(/['"]/g, "")
            .trim();
        }

        const a = document.createElement("a");
        a.style.display = "none";
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        enteredCode = "";
        console.log("File downloaded successfully");
      } else {
        const error = await response.json();
        alertMessage =
          error.error || "Failed to receive the file. Please try again.";
        showAlert = true;
        console.error("Error:", error);
      }
    } catch (error) {
      alertMessage = "An error occurred while downloading the file.";
      showAlert = true;
      console.error("Error:", error);
    } finally {
      isDownloading = false; // Re-enable the button
    }
  }
</script>

<div class="receiver-container">
  <h2>Enter Code</h2>
  <input type="text" bind:value={enteredCode} placeholder="Enter code" />
  <button on:click={receiveFile} disabled={isDownloading}>
    {isDownloading ? "Downloading..." : "Receive"}
  </button>

  {#if showAlert}
    <p class="alert">{alertMessage}</p>
  {/if}
</div>

<style>
  * {
    background-color: black;
    color: white;
  }

  .receiver-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: black;
    color: white;
  }

  input[type="text"] {
    padding: 10px;
    border: 1px solid white;
    border-radius: 5px;
    background-color: #333;
    color: white;
    width: 200px;
    margin-bottom: 10px;
  }

  button {
    margin-top: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: white;
    color: black;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:disabled {
    background-color: grey;
    cursor: not-allowed;
  }

  button:hover {
    background-color: #ddd;
  }

  .alert {
    margin-top: 15px;
    color: red;
  }
</style>
