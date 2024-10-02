<script>
  export let message = ""; // Message to display in the alert
  export let type = "info"; // Type of alert (info, success, warning, error)
  export let visible = false; // Visibility of the alert

  function closeAlert() {
    visible = false; // Function to close the alert
  }
</script>

{#if visible}
  <div class="alert {type}">
    <span>{message}</span>
    <button on:click={closeAlert} class="close-button">x</button>
  </div>
{/if}

<style>
  .alert {
    padding: 10px 20px;
    margin: 10px 0;
    border-radius: 5px;
    position: relative;
  }

  .alert.info {
    background-color: #2196f3;
    color: white;
  }

  .alert.success {
    background-color: #4caf50;
    color: white;
  }

  .alert.warning {
    background-color: #ff9800;
    color: white;
  }

  .alert.error {
    background-color: #f44336;
    color: white;
  }

  .close-button {
    position: absolute;
    top: 5px;
    right: 10px;
    border: none;
    background: transparent;
    color: white;
    font-size: 16px;
    cursor: pointer;
  }
</style>
