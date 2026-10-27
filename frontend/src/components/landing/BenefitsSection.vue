<script setup>
import DashboardPreview from '@/components/landing/DashboardPreview.vue'

const benefits = [
  {
    title: 'A reliable employee record',
    description:
      'Keep employee information organized and easy for authorized teams to find.',
  },
  {
    title: 'Clearer HR workflows',
    description:
      'Give HR teams, managers and employees a shared view of requests and next steps.',
  },
  {
    title: 'More consistent processes',
    description:
      'Bring hiring, leave, attendance and payroll processes into a more organized routine.',
  },
  {
    title: 'Information for each role',
    description:
      'Make relevant workforce information easier to access for employees, managers and HR.',
  },
  {
    title: 'Better workforce visibility',
    description:
      'Review people data and operational reports to support informed planning.',
  },
]
</script>

<template>
  <section id="benefits" class="scroll-mt-24 bg-hrms-bg py-20 lg:py-[40px]">
    <div class="mx-auto grid max-w-7xl items-center gap-14 px-4 sm:px-6 lg:grid-cols-2 lg:gap-20 lg:px-8">
      <div class="relative order-2 lg:order-1">
        <div class="rounded-[26px] bg-brand-gradient p-1.5 shadow-panel">
          <DashboardPreview />
        </div>
      </div>

      <div class="order-1 lg:order-2">
        <p class="text-body-sm font-bold uppercase tracking-[0.18em] text-hrms-purple">
          Benefits
        </p>
        <h2 class="mt-3 text-display-sm font-extrabold text-hrms-deep sm:text-display-md">
          Run HR operations with
          <span class="bg-brand-gradient bg-clip-text text-transparent">
            less friction
          </span>
        </h2>
        <p class="mt-4 text-body-lg text-hrms-muted">
          Organize the core HR processes your team handles every day, from
          employee information to workforce reporting.
        </p>

        <ul class="mt-8 space-y-5">
          <li
            v-for="benefit in benefits"
            :key="benefit.title"
            class="flex gap-4"
          >
            <span
              class="mt-0.5 inline-flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-brand-gradient text-white"
            >
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="3"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="h-3.5 w-3.5"
                aria-hidden="true"
              >
                <path d="M20 6 9 17l-5-5" />
              </svg>
            </span>
            <div>
              <h3 class="text-[16px] font-bold text-hrms-deep">
                {{ benefit.title }}
              </h3>
              <p class="mt-1 text-body-md text-hrms-muted">
                {{ benefit.description }}
              </p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>
