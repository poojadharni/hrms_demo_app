<script setup>
import { ref } from 'vue'

defineProps({
  variant: {
    type: String,
    default: 'light',
    validator: (value) => ['light', 'dark'].includes(value),
  },
})

// Same live logo the Frappe login page reads from Website Settings.
const logoSrc = '/files/quantumberg-logo.png'
const failed = ref(false)
</script>

<template>
  <span class="inline-flex items-center gap-3">
    <span
      v-if="!failed"
      class="inline-flex items-center rounded-xl"
      :class="
        variant === 'dark'
          ? 'bg-white p-1.5 shadow-sm'
          : 'bg-white p-1'
      "
    >
      <img
        :src="logoSrc"
        alt="Quantumberg Technologies logo"
        class="h-8 w-auto object-contain lg:h-9"
        @error="failed = true"
      />
    </span>

    <span
      v-else
      class="inline-flex items-center gap-2.5"
    >
      <span
        class="inline-flex h-9 w-9 items-center justify-center rounded-xl bg-brand-gradient"
        aria-hidden="true"
      >
        <svg
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="h-5 w-5 text-white"
        >
          <path d="M16 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
          <circle cx="10" cy="7" r="4" />
          <path d="M20 21v-2a4 4 0 0 0-3-3.87" />
          <path d="M16 3.13a4 4 0 0 1 0 7.75" />
        </svg>
      </span>
      <span
        class="text-body-md font-bold tracking-tight"
        :class="variant === 'dark' ? 'text-white' : 'text-hrms-deep'"
      >
        HRMS
      </span>
    </span>

    <span
      class="hidden border-l pl-3 sm:inline-block"
      :class="
        variant === 'dark'
          ? 'border-white/20 text-white/70'
          : 'border-hrms-border text-hrms-muted'
      "
    >
      <span class="block text-[11px] font-semibold uppercase tracking-[0.14em]">
        HRMS Portal
      </span>
    </span>
  </span>
</template>
