<template>
  <div
    class="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <div class="max-w-md w-full space-y-8">
      <!-- Header -->

      <!-- Registration Form -->
      <UCard class="shadow-xl">
        <div class="text-center m-8">
          <UIcon
            name="i-heroicons-user-plus"
            class="mx-auto h-12 w-12 text-primary-600"
          />
          <h2
            class="mt-6 text-3xl font-extrabold text-gray-900 dark:text-white"
          >
            Create your account
          </h2>
          <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
            Join PrimeTrading and start your trading journey
          </p>
        </div>

        <form
          class="space-y-4 flex flex-col justify-center"
          @submit.prevent="onSubmit"
        >
          <!-- Username Field -->
          <UFormGroup
            label="Username"
            name="username"
            help="Choose a unique username for your account"
            class="text-center"
          >
            <UInput
              v-model="state.username"
              placeholder="Enter your username"
              icon="i-heroicons-user"
              size="lg"
              :disabled="loading"
              class="text-center"
              required
            />
          </UFormGroup>

          <!-- Email Field -->
          <UFormGroup
            label="Email"
            name="email"
            help="We'll use this email for account verification"
            class="text-center"
          >
            <UInput
              v-model="state.email"
              type="email"
              placeholder="Enter your email address"
              icon="i-heroicons-envelope"
              size="lg"
              :disabled="loading"
              class="text-center"
              required
            />
          </UFormGroup>

          <!-- Password Field -->
          <UFormGroup
            label="Password"
            name="password"
            help="Must be at least 8 characters long"
            class="text-center"
          >
            <UInput
              v-model="state.password"
              type="password"
              placeholder="Create a strong password"
              icon="i-heroicons-lock-closed"
              size="lg"
              :disabled="loading"
              class="text-center"
              required
            />
          </UFormGroup>

          <!-- Confirm Password Field -->
          <UFormGroup
            label="Confirm Password"
            name="confirmPassword"
            class="text-center"
          >
            <UInput
              v-model="state.confirmPassword"
              type="password"
              placeholder="Confirm your password"
              icon="i-heroicons-lock-closed"
              size="lg"
              :disabled="loading"
              class="text-center"
              required
            />
          </UFormGroup>

          <!-- Terms and Conditions -->
          <UFormGroup name="acceptTerms" class="flex justify-center">
            <UCheckbox
              v-model="state.acceptTerms"
              label="I agree to the Terms of Service and Privacy Policy"
              :disabled="loading"
              class="text-justify"
              required
            />
          </UFormGroup>
          <UFormGroup name="acceptAge" class="flex justify-center">
            <UCheckbox
              v-model="state.acceptAge"
              label="I certify that I am at least 18 years old"
              :disabled="loading"
              class="text-justify"
              required
            />
          </UFormGroup>

          <!-- Submit Button -->
          <UButton
            type="submit"
            block
            size="lg"
            :loading="loading"
            :disabled="!state.acceptTerms"
            class="justify-center mx-auto w-full"
          >
            <template #leading>
              <UIcon name="i-heroicons-user-plus" />
            </template>
            Create Account
          </UButton>
        </form>

        <!-- Login Link -->
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600 dark:text-gray-400">
            Already have an account?
            <UButton variant="link" size="sm" to="/login" class="p-0">
              Sign in here
            </UButton>
          </p>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
// Reactive state for form data
const state = reactive({
  username: "",
  email: "",
  password: "",
  confirmPassword: "",
  acceptTerms: false,
  acceptAge: false,
});

// Loading state
const loading = ref(false);

// Toast notification
const toast = useToast();

// Form submission handler
async function onSubmit() {
  // Basic client-side checks
  if (!state.acceptTerms) {
    toast.add({
      title: "Terms Required",
      description: "You must accept the terms and conditions.",
      icon: "i-heroicons-exclamation-triangle",
      color: "warning",
    });
    return;
  }

  if (state.password !== state.confirmPassword) {
    toast.add({
      title: "Password Mismatch",
      description: "Passwords don't match.",
      icon: "i-heroicons-exclamation-triangle",
      color: "warning",
    });
    return;
  }

  loading.value = true;

  try {
    // Replace with actual API call to your Django backend
    // const response = await $fetch('/api/auth/register', {
    //   method: 'POST',
    //   body: {
    //     username: state.username,
    //     email: state.email,
    //     password: state.password,
    //   }
    // })

    // Simulate API call for now
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Show success message
    toast.add({
      title: "Account Created Successfully!",
      description:
        "Welcome to PrimeTrading. Please check your email to verify your account.",
      icon: "i-heroicons-check-circle",
      color: "success",
    });

    // Redirect to login or dashboard
    await navigateTo("/login");
  } catch {
    // Handle backend validation errors here
    toast.add({
      title: "Registration Failed",
      description: "Something went wrong. Please try again.",
      icon: "i-heroicons-exclamation-triangle",
      color: "error",
    });
  } finally {
    loading.value = false;
  }
}

// Set page meta
useHead({
  title: "Register - PrimeTrading",
  meta: [
    {
      name: "description",
      content:
        "Create your PrimeTrading account and start your trading journey today.",
    },
  ],
});
</script>
