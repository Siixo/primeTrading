<script setup>
definePageMeta({
  layout: "landing",
});
</script>

<template>
  <div class="relative h-screen w-full">
    <img
      src="/imgs/andreas-brucker-C2Dyr5FhGPQ-unsplash.jpg"
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
        class="px-6 py-3 bg-white text-black font-semibold rounded-full hover:bg-neutral-200 transition"
      >
        Get Started
      </button>
    </div>
  </div>
</template>
