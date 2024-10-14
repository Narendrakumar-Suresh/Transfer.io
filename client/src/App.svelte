<script>
  import Navbar from "./components/Navbar.svelte";
  import { Router, Route, Link } from "svelte-routing";
  import Sender from "./lib/pages/Sender.svelte";
  import Receiver from "./lib/pages/Receiver.svelte";
</script>

<Navbar />
<Router>
  <div class="w-full h-screen flex justify-center items-center bg-black p-14">
    <Route path="/sender" component={Sender} />
    <Route path="/receiver" component={Receiver} />
    <Route path="/" exact>
      <div class="flex space-x-8">
        <Link to="/sender">
          <div
            class="cursor-pointer p-6 bg-gray-700 rounded-lg text-white flex flex-col items-center"
          >
            <svg
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
            <span class="mt-2">Send</span>
          </div>
        </Link>

        <Link to="/receiver">
          <div
            class="cursor-pointer p-6 bg-gray-700 rounded-lg text-white flex flex-col items-center"
          >
            <svg
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
            <span class="mt-2">Receive</span>
          </div>
        </Link>
      </div>
    </Route>
  </div>
</Router>
