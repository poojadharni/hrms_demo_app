<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <article
    class="group h-full rounded-2xl border border-hrms-border bg-white p-6 shadow-card transition-all duration-300 hover:-translate-y-1 hover:border-hrms-purple/30 hover:shadow-card-hover focus-within:shadow-card-hover"
  >
    <span
      class="inline-flex h-12 w-12 items-center justify-center rounded-xl bg-brand-gradient-soft text-hrms-purple transition-colors duration-300 group-hover:bg-brand-gradient group-hover:text-white"
    >
      <slot name="icon">
        <svg
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="h-6 w-6"
          aria-hidden="true"
        >
          <circle cx="12" cy="12" r="9" />
        </svg>
      </slot>
    </span>
    <h3 class="mt-5 text-[17px] font-bold text-hrms-deep">
      {{ title }}
    </h3>
    <p class="mt-2 text-body-md text-hrms-muted">
      {{ description }}
    </p>
  </article>
</template>
