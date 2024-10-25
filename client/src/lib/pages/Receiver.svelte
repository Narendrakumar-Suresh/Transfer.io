<script>
  let enteredCode = "";
  let isDownloading = false; // Track download state

  async function receiveFile() {
    const formData = new FormData();
    formData.append("code", enteredCode); // Include entered code

    console.log("Entered code:", enteredCode); // Debugging log

    try {
      const response = await fetch("https://transfer-io.onrender.com/receive", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        isDownloading = true; // Set downloading state for UI feedback

        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.style.display = "none";
        a.href = url;
        a.download = "received_file_name"; // Set a default filename
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);

        console.log("File downloaded successfully");
        isDownloading = false; // Reset downloading state
      } else {
        const error = await response.json();
        console.error("Error:", error);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<div class="receiver-container">
  <h2>Enter Code</h2>
  <input type="text" bind:value={enteredCode} placeholder="Enter code" />
  <button on:click={receiveFile} disabled={isDownloading}>
    {isDownloading ? "Downloading..." : "Receive"}
  </button>
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

  button:hover {
    background-color: #ddd;
  }
</style>
