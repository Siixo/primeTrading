<template>
  <UHeader>
    <template #title>
      <Logo class="h-6 w-auto" />
    </template>

    <UNavigationMenu :items="items" />

    <template #right>
      <UColorModeButton />

      <UButton
        color="primary"
        variant="solid"
        to="/login"
        label="Login"
        class="ml-2"
      />
      <UButton
        color="neutral"
        variant="outline"
        to="/register"
        label="Register"
        class="ml-2"
      />

      <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
        <UButton
          color="neutral"
          variant="ghost"
          to="https://github.com/Siixo/primeTrading"
          target="_blank"
          icon="i-simple-icons-github"
          aria-label="GitHub"
        />
      </UTooltip>
    </template>
  </UHeader>
</template>

<script setup lang="ts">
const items = [
  {
    label: "Home",
    to: "/",
  },
  {
    label: "Trading",
    to: "/trading",
  },
  {
    label: "Portfolio",
    to: "/portfolio",
  },
  {
    label: "Markets",
    to: "/markets",
  },
  {
    label: "About",
    to: "/about",
  },
];
</script>
