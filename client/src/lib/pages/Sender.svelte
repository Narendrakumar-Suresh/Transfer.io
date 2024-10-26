<script>
  import { onMount } from "svelte";
  import Alert from "../../components/Alert.svelte";

  let file;
  let code = "";
  let alertVisible = false;
  let alertMessage = "";
  let alertType = "info";

  async function sendFile() {
    if (!file) {
      alertMessage = "Please select a file to send.";
      alertType = "error";
      alertVisible = true;
      return;
    }

    if (!code) {
      alertMessage = "Failed to generate a code. Please try again.";
      alertType = "error";
      alertVisible = true;
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("code", code);

    try {
      const response = await fetch("https://transfer-io.onrender.com/send", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        alertMessage = "File sent successfully!";
        alertType = "success";
        alertVisible = true;
        file = null; // Clear the file input
        document.querySelector('input[type="file"]').value = ""; // Reset input field
        code = generateRandomCode(); // Generate a new random code
      } else {
        const error = await response.json();
        alertMessage = "Error: " + error.message;
        alertType = "error";
        alertVisible = true;
      }
    } catch (error) {
      alertMessage = "Error: " + error.message;
      alertType = "error";
      alertVisible = true;
      console.log("Error: " + error.message);
    }

    console.log("Using code:", code);
  }

  function handleFileChange(event) {
    file = event.target.files[0];
    console.log("Selected file:", file);
  }

  onMount(() => {
    code = generateRandomCode();
  });

  function generateRandomCode() {
    const characters =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let code = "";
    for (let i = 0; i < 6; i++) {
      code += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return code;
  }
</script>

<div class="sender-container">
  <h2>Upload a File</h2>
  <input type="file" on:change={handleFileChange} />
  <p>{code}</p>
  <button on:click={sendFile}>Send</button>

  <Alert message={alertMessage} type={alertType} visible={alertVisible} />
</div>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  * {
    background-color: black;
    color: white;
  }

  .sender-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: black;
    color: white;
  }

  h2 {
    margin-bottom: 20px;
  }

  input[type="file"] {
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
