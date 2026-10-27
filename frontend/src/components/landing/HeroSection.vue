<script setup>
import DashboardPreview from '@/components/landing/DashboardPreview.vue'
import { useLoginUrl } from '@/composables/useLoginUrl'

const { loginUrl } = useLoginUrl()

const indicators = [
  'Employee self-service',
  'Connected HR workflows',
  'Role-based access',
]
</script>

<template>
  <section id="home" class="relative overflow-hidden bg-white pb-16 pt-28 sm:pb-20 sm:pt-32 lg:pb-24 lg:pt-24">
    <div
      class="hero-orb pointer-events-none absolute -right-32 -top-32 h-[420px] w-[420px] rounded-full bg-brand-gradient-soft blur-3xl"
      aria-hidden="true" />
    <div
      class="hero-orb-alt pointer-events-none absolute -left-40 top-40 h-[320px] w-[320px] rounded-full bg-hrms-purple/5 blur-3xl"
      aria-hidden="true" />

    <div
      class="relative mx-auto grid max-w-7xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-[1.05fr_1fr] lg:gap-16 lg:px-8">
      <div>
        <p
          class="inline-flex items-center gap-2 rounded-full border border-hrms-border bg-white px-4 py-1.5 text-body-sm font-semibold text-hrms-purple shadow-sm">
          <span class="h-2 w-2 rounded-full bg-brand-gradient" aria-hidden="true" />
          Human Resource Management System
        </p>

        <h1 class="mt-6 text-display-md font-extrabold text-hrms-deep sm:text-display-lg xl:text-display-xl">
          Manage Your People
          <span class="bg-brand-gradient bg-clip-text text-transparent">with Confidence</span>
        </h1>

        <p class="mt-6 max-w-2xl text-body-lg text-hrms-muted">
          Bring employee records, hiring, leave, attendance, payroll, and
          performance workflows together in one organized HRMS workspace.
        </p>

        <div class="mt-8 flex flex-col gap-3 sm:flex-row sm:items-center">
          <a :href="loginUrl"
            class="inline-flex items-center justify-center gap-2 rounded-xl bg-brand-gradient px-7 py-3.5 text-body-lg font-semibold text-white shadow-cta transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-purple focus-visible:ring-offset-2">
            Open Demo App
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" class="h-4 w-4" aria-hidden="true">
              <path d="M5 12h14M13 6l6 6-6 6" />
            </svg>
          </a>
          <a href="https://www.quantumberg.com/Contact"
            class="inline-flex items-center justify-center gap-2 rounded-xl border-2 border-hrms-border bg-white px-7 py-3.5 text-body-lg font-semibold text-hrms-ink transition-colors duration-200 hover:border-hrms-purple hover:text-hrms-purple focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-pink focus-visible:ring-offset-2">
            Book a Demo
          </a>
        </div>

        <ul class="mt-8 flex flex-wrap items-center gap-x-5 gap-y-2">
          <li v-for="indicator in indicators" :key="indicator"
            class="inline-flex items-center gap-1.5 text-body-sm font-medium text-hrms-muted">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"
              stroke-linejoin="round" class="h-3.5 w-3.5 text-hrms-pink" aria-hidden="true">
              <path d="M20 6 9 17l-5-5" />
            </svg>
            {{ indicator }}
          </li>
        </ul>
      </div>

      <div class="relative">
        <div class="panel-tilt rounded-[26px] bg-brand-gradient p-1.5 shadow-panel" aria-hidden="false">
          <DashboardPreview />
        </div>
      </div>
    </div>
  </section>
</template>
