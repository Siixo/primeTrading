<template>
  <div
    class="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-sm w-full space-y-8">
      <!-- Header -->

      <!-- Login Form -->
      <UCard class="shadow-xl">
        <div class="text-center m-8">
          <UIcon
            name="i-heroicons-arrow-right-on-rectangle"
            class="mx-auto h-12 w-12 text-primary-600"
          />
          <h2
            class="mt-6 text-3xl font-extrabold text-gray-900 dark:text-white"
          >
            Welcome back
          </h2>
          <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
            Sign in to your PrimeTrading account
          </p>
        </div>

        <form class="space-y-6 flex flex-col justify-center">
          <!-- Email/Username Field -->
          <UFormGroup
            label="Email or Username"
            name="identifier"
            help="Enter your email address or username"
            class="text-center"
          >
            <UInput
              placeholder="Enter your email or username"
              icon="i-heroicons-user"
              size="xl"
              class="text-center"
              required
            />
          </UFormGroup>

          <!-- Password Field -->
          <UFormGroup label="Password" name="password" class="text-center">
            <UInput
              type="password"
              placeholder="Enter your password"
              icon="i-heroicons-lock-closed"
              size="xl"
              class="text-center"
              required
            />
          </UFormGroup>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between">
            <UCheckbox label="Remember me" />
            <UButton
              variant="link"
              size="sm"
              to="/forgot-password"
              class="p-0 text-sm"
            >
              Forgot password?
            </UButton>
          </div>

          <!-- Submit Button -->
          <UButton
            type="submit"
            block
            size="lg"
            class="justify-center mx-auto w-full"
          >
            <template #leading>
              <UIcon name="i-heroicons-arrow-right-on-rectangle" />
            </template>
            Sign In
          </UButton>
        </form>

        <!-- Register Link -->
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600 dark:text-gray-400">
            Don't have an account?
            <UButton variant="link" size="sm" to="/register" class="p-0">
              Create one here
            </UButton>
          </p>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
useHead({
  title: "Login - PrimeTrading",
  meta: [
    {
      name: "description",
      content:
        "Sign in to your PrimeTrading account and continue your trading journey.",
    },
  ],
});
</script>

<style scoped>
/* Center form labels and help text */
:deep(.form-group) {
  text-align: center;
}

:deep(.form-group label) {
  display: block;
  text-align: center;
  margin-bottom: 0.5rem;
}

:deep(.form-group .help-text) {
  text-align: center;
}

/* Ensure input fields are properly aligned */
:deep(.ui-input-wrapper) {
  margin: 0 auto;
  text-align: center;
}

:deep(.ui-input) {
  text-align: center;
}

/* Center the checkbox container */
:deep(.ui-checkbox-wrapper) {
  justify-content: center;
  text-align: center;
}
</style>
