<script setup>
import { computed } from 'vue'
import BrandLogo from '@/components/BrandLogo.vue'
import { useLoginUrl } from '@/composables/useLoginUrl'
import { useSectionScroll } from '@/composables/useSectionScroll'

const { loginUrl } = useLoginUrl()
const { scrollToSection } = useSectionScroll()

const year = computed(() => new Date().getFullYear())

const platformLinks = [
  { label: 'Home', target: 'home' },
  { label: 'Features', target: 'features' },
  { label: 'Benefits', target: 'benefits' },
  { label: 'About', target: 'about' },
]

function onNavClick(event, target) {
  event.preventDefault()
  scrollToSection(target)
}
</script>

<template>
  <footer class="bg-hrms-deep text-white">
    <div class="mx-auto max-w-7xl px-4 py-14 sm:px-6 lg:px-8">
      <div class="grid gap-10 lg:grid-cols-[1.4fr_1fr_1fr]">
        <div>
          <BrandLogo variant="dark" />
          <p class="mt-4 max-w-md text-body-md text-white/70">
            An HRMS workspace for employee records, hiring, leave, attendance
            and the everyday work of managing people.
          </p>
        </div>

        <nav aria-label="Footer">
          <h3 class="text-body-sm font-bold uppercase tracking-[0.16em] text-white/50">
            Platform
          </h3>
          <ul class="mt-4 space-y-2.5">
            <li v-for="link in platformLinks" :key="link.target">
              <a :href="`#${link.target}`"
                class="text-body-md text-white/75 transition-colors hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/60 focus-visible:ring-offset-2 focus-visible:ring-offset-hrms-deep rounded"
                @click="onNavClick($event, link.target)">
                {{ link.label }}
              </a>
            </li>
          </ul>
        </nav>

        <nav aria-label="Resources">
          <h3 class="text-body-sm font-bold uppercase tracking-[0.16em] text-white/50">
            Resources
          </h3>
          <ul class="mt-4 space-y-2.5">
            <li>
              <a :href="loginUrl"
                class="text-body-md text-white/75 transition-colors hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white/60 focus-visible:ring-offset-2 focus-visible:ring-offset-hrms-deep rounded">
                Open Demo App
              </a>
            </li>
          </ul>
        </nav>
      </div>

      <div class="mt-12 flex flex-col items-center justify-between gap-3 border-t border-white/10 pt-6 sm:flex-row">
        <p class="text-body-sm text-white/55">
          &copy; {{ year }} Quantumberg Tech Pvt Ltd &middot; HRMS Portal.
          All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>
