<script setup>
const modules = [
  'Employee records',
  'Recruitment',
  'Leave management',
  'Attendance',
  'Payroll',
  'Performance',
  'Workforce reports',
  'Employee self-service',
]
</script>

<template>
  <section
    id="about"
    class="border-y border-hrms-border bg-hrms-bg py-16 lg:py-[50px]"
  >
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-body-sm font-bold uppercase tracking-[0.18em] text-hrms-purple">
          About the platform
        </p>
        <h2 class="mt-3 text-display-sm font-extrabold text-hrms-deep sm:text-display-md">
          One connected workspace for the employee lifecycle
        </h2>
        <p class="mt-4 text-body-lg text-hrms-muted">
          Bring employee information and essential people processes into one
          organized workspace, with relevant access for employees, managers
          and HR teams.
        </p>
      </div>

      <ul class="mx-auto mt-10 flex max-w-4xl flex-wrap items-center justify-center gap-3">
        <li
          v-for="module in modules"
          :key="module"
          class="inline-flex items-center gap-2 rounded-full border border-hrms-border bg-white px-4 py-2 text-body-sm font-semibold text-hrms-ink shadow-sm"
        >
          <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2.5"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="h-3.5 w-3.5 text-hrms-pink"
            aria-hidden="true"
          >
            <path d="M20 6 9 17l-5-5" />
          </svg>
          {{ module }}
        </li>
      </ul>
    </div>
  </section>
</template>
