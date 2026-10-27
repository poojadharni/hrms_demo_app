<script setup>
import FeatureCard from '@/components/landing/FeatureCard.vue'

const features = [
  {
    title: 'Employee Directory',
    description:
      'Keep employee profiles, roles, departments and contact details organized in one place.',
    icon: 'employees',
  },
  {
    title: 'Recruitment',
    description:
      'Track open positions and candidates as they move through your hiring process.',
    icon: 'recruitment',
  },
  {
    title: 'Leave & Attendance',
    description:
      'Coordinate leave requests, attendance records and team availability.',
    icon: 'attendance',
  },
  {
    title: 'Payroll',
    description:
      'Keep compensation information and payroll processes connected to employee records.',
    icon: 'payroll',
  },
  {
    title: 'Performance Management',
    description:
      'Support goal setting, feedback and performance reviews throughout the employee lifecycle.',
    icon: 'performance',
  },
  {
    title: 'People Analytics',
    description:
      'Use clear workforce reports to understand staffing and day-to-day HR operations.',
    icon: 'analytics',
  },
]
</script>

<template>
  <section id="features" class="scroll-mt-24 bg-white py-20 lg:py-[40px]">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-body-sm font-bold uppercase tracking-[0.18em] text-hrms-purple">
          Features
        </p>
        <h2 class="mt-3 text-display-sm font-extrabold text-hrms-deep sm:text-display-md">
          The essentials for better
          <span class="bg-brand-gradient bg-clip-text text-transparent">
            people operations
          </span>
        </h2>
        <p class="mt-4 text-body-lg text-hrms-muted">
          Organize the everyday work of HR teams, managers and employees
          across the employee lifecycle.
        </p>
      </div>

      <div class="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <FeatureCard
          v-for="feature in features"
          :key="feature.title"
          :title="feature.title"
          :description="feature.description"
        >
          <template #icon>
            <svg
              v-if="feature.icon === 'employees'"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
              <circle cx="9" cy="7" r="4" />
              <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
              <path d="M16 3.13a4 4 0 0 1 0 7.75" />
            </svg>
            <svg
              v-else-if="feature.icon === 'recruitment'"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
              <circle cx="12" cy="7" r="4" />
            </svg>
            <svg
              v-else-if="feature.icon === 'attendance'"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2z" />
              <path d="M22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z" />
            </svg>
            <svg
              v-else-if="feature.icon === 'payroll'"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <path d="M9 11l3 3L22 4" />
              <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11" />
            </svg>
            <svg
              v-else-if="feature.icon === 'performance'"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <path d="M3 3v18h18" />
              <path d="M7 14l4-4 3 3 5-6" />
            </svg>
            <svg
              v-else
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <rect x="3" y="3" width="7" height="9" rx="1.5" />
              <rect x="14" y="3" width="7" height="5" rx="1.5" />
              <rect x="14" y="12" width="7" height="9" rx="1.5" />
              <rect x="3" y="16" width="7" height="5" rx="1.5" />
            </svg>
          </template>
        </FeatureCard>
      </div>
    </div>
  </section>
</template>
