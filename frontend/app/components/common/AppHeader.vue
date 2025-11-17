<script setup lang="ts">
import type { NavigationMenuItem } from "@nuxt/ui";

const route = useRoute();

const items = computed<NavigationMenuItem[]>(() => [
  {
    label: "Home",
    to: "/",
    icon: "i-lucide-home",
    active: route.path === "/",
  },
  {
    label: "Graphs",
    to: "/graphs",
    icon: "i-material-symbols:ssid-chart",
    active: route.path.startsWith("/graphs"),
  },
  {
    label: "Predictions",
    to: "/predictions",
    icon: "i-tabler:math-max-min",
    active: route.path.startsWith("/predictions"),
  },
  {
    label: "Profile",
    to: "/profile",
    icon: "i-heroicons-user-circle-20-solid",
    active: route.path.startsWith("/profile"),
  },
  {
    label: "About",
    to: "/about",
    icon: "i-ic:outline-info",
    active: route.path.startsWith("/about"),
  },
]);
</script>

<template>
  <UHeader
    :toggle="{
      color: 'neutral',
      variant: 'ghost',
      class: 'rounded-full',
    }"
  >
    <template #title>
      <Logo class="h-6 w-auto" />
    </template>

    <UNavigationMenu :items="items" />

    <template #right>
      <UButton color="primary" variant="solid" to="/login" label="Login" />
      <UButton
        color="neutral"
        variant="outline"
        to="/register"
        label="Register"
        class="ml-2"
      />

      <UColorModeButton class="ml-2" />

      <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
        <UButton
          color="neutral"
          variant="ghost"
          to="https://github.com/nuxt/ui"
          target="_blank"
          icon="i-simple-icons-github"
          aria-label="GitHub"
        />
      </UTooltip>
    </template>

    <template #body>
      <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
    </template>
  </UHeader>
</template>
