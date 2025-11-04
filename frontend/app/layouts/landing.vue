<template>
  <div>
    <!-- Floating header that appears on scroll -->
    <header
      :class="[
        'fixed top-0 left-0 right-0 z-50 transition-all duration-300 ease-in-out',
        showHeader
          ? 'translate-y-0 opacity-100 bg-white/95 backdrop-blur-md shadow-lg'
          : '-translate-y-full opacity-0',
      ]"
    >
      <AppHeader />
    </header>

    <main>
      <slot />
    </main>

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import AppHeader from "~/components/common/AppHeader.vue";
import AppFooter from "~/components/common/AppFooter.vue";

const showHeader = ref(false);

const handleScroll = () => {
  // Show header when scrolled down more than 100px
  showHeader.value = window.scrollY > 100;
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
