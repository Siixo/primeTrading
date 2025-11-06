<script setup></script>

<template>
  <div>
    <div class="relative h-screen w-full">
      <img
        src="/imgs/dennis-kummer-52gEprMkp7M-unsplash.jpg"
        alt="Stock trading hero"
        class="h-full w-full object-cover object-center"
      />
      <div
        class="absolute inset-0 flex flex-col items-center justify-center bg-black/50 text-center"
      >
        <h1 class="text-white text-6xl font-bold mb-6 leading-tight">
          Welcome to <br />PrimeTrading
        </h1>
        <button
          class="px-6 py-3 bg-white text-black font-semibold rounded-full hover:bg-neutral-200 transition mb-4"
        >
          Get Started
        </button>
        <a href="">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
          >
            <!-- Icon from IconaMoon by Dariush Habibpour - https://creativecommons.org/licenses/by/4.0/ -->
            <path
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2.5"
              d="m7 10l5 5m0 0l5-5"
            />
          </svg>
        </a>
      </div>
    </div>
    <section
      class="discover p-8 max-w-4xl mx-auto flex flex-col items-center text-center gap-4"
    >
      <h2 class="text-2xl font-bold mb-4">Discover</h2>
      <p class="text-gray-600">
        Explore the features and benefits of PrimeTrading.
      </p>
      <ul class="list-disc list-inside">
        <li>Real-time market data</li>
        <li>Advanced trading tools</li>
        <li>Secure portfolio management</li>
        <li>Comprehensive market analysis</li>
      </ul>
    </section>
  </div>
</template>
