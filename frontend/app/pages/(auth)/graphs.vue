<template>
  <div>
    <div
      ref="chartContainer"
      class="w-[600px] h-[300px] mx-auto border border-gray-300"
    />
  </div>
</template>

<script lang="js" setup>
const router = useRouter();

async function checkAuth() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/accounts/me/', {
      method: 'GET',
      credentials: 'include', // sends cookies
    });
    if (response.ok) {
      const user = await response.json();
      // User is authenticated, proceed to show page
    } else {
      // Not authenticated, redirect to login
      router.push('/login');
    }
  } catch (error) {
    router.push('/login');
  }
}

onMounted(() => {
  checkAuth();
});
</script>
