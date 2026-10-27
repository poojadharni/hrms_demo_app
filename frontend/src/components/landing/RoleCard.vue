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
  bullets: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <article
    class="flex h-full flex-col rounded-2xl border border-hrms-border bg-white p-7 shadow-card transition-all duration-300 hover:-translate-y-1 hover:shadow-card-hover"
  >
    <span class="inline-flex h-12 w-12 items-center justify-center rounded-xl bg-brand-gradient text-white shadow-cta">
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
          <circle cx="12" cy="8" r="4" />
          <path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1" />
        </svg>
      </slot>
    </span>

    <h3 class="mt-5 text-[18px] font-bold text-hrms-deep">
      {{ title }}
    </h3>
    <p class="mt-2 text-body-md text-hrms-muted">
      {{ description }}
    </p>

    <ul class="mt-5 space-y-2.5">
      <li
        v-for="bullet in bullets"
        :key="bullet"
        class="flex items-start gap-2.5 text-body-md text-hrms-ink"
      >
        <svg
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2.5"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="mt-1 h-3.5 w-3.5 shrink-0 text-hrms-pink"
          aria-hidden="true"
        >
          <path d="M20 6 9 17l-5-5" />
        </svg>
        {{ bullet }}
      </li>
    </ul>
  </article>
</template>
