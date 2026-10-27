<script setup>
import RoleCard from '@/components/landing/RoleCard.vue'

const roles = [
  {
    key: 'employees',
    title: 'Employees',
    description:
      'A straightforward place to manage personal information and everyday HR needs.',
    bullets: [
      'Review personal and employment information',
      'Submit and follow leave requests',
      'Stay informed about attendance and workplace updates',
    ],
    icon: 'employee',
  },
  {
    key: 'managers',
    title: 'People Managers',
    description:
      'Useful workforce context to support teams and day-to-day decisions.',
    bullets: [
      'Review team information and availability',
      'Respond to leave and attendance requests',
      'Support employee goals and performance reviews',
    ],
    icon: 'manager',
  },
  {
    key: 'hr-teams',
    title: 'HR Teams',
    description:
      'A central workspace for the people processes that keep an organization moving.',
    bullets: [
      'Maintain employee and organizational records',
      'Coordinate hiring, leave and payroll processes',
      'Review workforce reports and HR operations',
    ],
    icon: 'admin',
  },
]
</script>

<template>
  <section id="roles" class="scroll-mt-24 bg-white py-20 lg:py-[40px]">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-body-sm font-bold uppercase tracking-[0.18em] text-hrms-purple">
          Built for every role
        </p>
        <h2 class="mt-3 text-display-sm font-extrabold text-hrms-deep sm:text-display-md">
          A workspace for every role
        </h2>
        <p class="mt-4 text-body-lg text-hrms-muted">
          Employees, managers and HR teams can focus on the information and
          processes relevant to their work.
        </p>
      </div>

      <div class="mt-14 grid gap-6 md:grid-cols-3">
        <RoleCard
          v-for="role in roles"
          :key="role.key"
          :title="role.title"
          :description="role.description"
          :bullets="role.bullets"
        >
          <template #icon>
            <svg
              v-if="role.icon === 'employee'"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="h-6 w-6"
              aria-hidden="true"
            >
              <path d="M22 10 12 5 2 10l10 5 10-5z" />
              <path d="M6 12.5V17c0 1 2.7 2.5 6 2.5s6-1.5 6-2.5v-4.5" />
            </svg>
            <svg
              v-else-if="role.icon === 'manager'"
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
        </RoleCard>
      </div>
    </div>
  </section>
</template>
