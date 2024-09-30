<script>
  import Navbar from "./components/Navbar.svelte";
  import Card from "./components/Card.svelte";
  import { Router, Link, Route } from "svelte-routing";
  import Sender from "./lib/pages/Sender.svelte";
  import Receiver from "./lib/pages/Receiver.svelte";
</script>

<Navbar />
<div class="w-screen">
  <Router>
    <!-- Routes -->
    <Route path="/sender" component={Sender} />
    <Route path="/receiver" component={Receiver} />

    <div class="container">
      <Card title="Send" links="/sender">
        <svg
          slot="icon"
          xmlns="http://www.w3.org/2000/svg"
          width="48"
          height="48"
          viewBox="0 0 24 24"
          fill="none"
          stroke="white"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
          <polyline points="17 8 12 3 7 8"></polyline>
          <line x1="12" y1="3" x2="12" y2="15"></line>
        </svg>
      </Card>

      <Card title="Receive" links="/receiver">
        <svg
          slot="icon"
          xmlns="http://www.w3.org/2000/svg"
          width="48"
          height="48"
          viewBox="0 0 24 24"
          fill="none"
          stroke="white"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
          <polyline points="7 10 12 15 17 10"></polyline>
          <line x1="12" y1="15" x2="12" y2="3"></line>
        </svg>
      </Card>
    </div>
  </Router>
</div>

<style>
  * {
    margin: 0;
    padding: 0;

    box-sizing: border-box;
    overflow: hidden; /* This makes the page non-scrollable */
  }

  .container {
    display: flex; /* Makes the cards align horizontally */
    justify-content: center; /* Centers the cards horizontally */
    align-items: center; /* Centers the cards vertically */
    height: 100vh;
    /* Full viewport height */
    background-color: black;
    padding: 3.5rem;
  }

  .container > * {
    margin: 0 1rem; /* Adds space between the cards */
  }
</style>
