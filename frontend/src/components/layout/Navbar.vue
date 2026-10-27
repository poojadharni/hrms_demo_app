<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import BrandLogo from '@/components/BrandLogo.vue'
import { useLoginUrl } from '@/composables/useLoginUrl'
import { useSectionScroll } from '@/composables/useSectionScroll'

const { loginUrl } = useLoginUrl()
const { scrollToSection } = useSectionScroll()

const mobileOpen = ref(false)

const navLinks = [
  { label: 'Home', target: 'home' },
  { label: 'About', target: 'about' },
  { label: 'Features', target: 'features' },
  { label: 'Benefits', target: 'benefits' },
]

function onNavClick(event, target) {
  event.preventDefault()
  mobileOpen.value = false
  scrollToSection(target)
}

function onMobileToggle() {
  mobileOpen.value = !mobileOpen.value
}

function onEscape(event) {
  if (event.key === 'Escape') {
    mobileOpen.value = false
  }
}

function onResize() {
  if (window.innerWidth >= 1024) {
    mobileOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('keydown', onEscape)
  window.addEventListener('resize', onResize)
})

onBeforeUnmount(() => {
  document.removeEventListener('keydown', onEscape)
  window.removeEventListener('resize', onResize)
})
</script>

<template>
  <header class="fixed inset-x-0 top-0 z-50 border-b border-hrms-border bg-white/90 backdrop-blur-md">
    <nav class="mx-auto flex h-16 max-w-7xl items-center justify-between gap-4 px-4 sm:px-6 lg:h-[72px] lg:px-8"
      aria-label="Main">
      <a href="#home"
        class="rounded-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-pink focus-visible:ring-offset-2"
        @click="onNavClick($event, 'home')">
        <BrandLogo />
      </a>

      <div class="hidden items-center gap-1 lg:flex">
        <a v-for="link in navLinks" :key="link.target" :href="`#${link.target}`"
          class="rounded-lg px-3.5 py-2 text-body-md font-medium text-hrms-muted transition-colors hover:text-hrms-purple focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-pink focus-visible:ring-offset-1"
          @click="onNavClick($event, link.target)">
          {{ link.label }}
        </a>
        <a :href="loginUrl"
          class="ml-2 inline-flex items-center justify-center rounded-xl bg-brand-gradient px-5 py-2.5 text-body-md font-semibold text-white shadow-cta transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-purple focus-visible:ring-offset-2">
          Open Demo App
        </a>
      </div>

      <button type="button"
        class="inline-flex h-11 w-11 items-center justify-center rounded-xl border border-hrms-border bg-white text-hrms-purple transition-colors hover:bg-hrms-bg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-pink focus-visible:ring-offset-2 lg:hidden"
        :aria-expanded="mobileOpen ? 'true' : 'false'" aria-controls="mobile-menu"
        :aria-label="mobileOpen ? 'Close menu' : 'Open menu'" @click="onMobileToggle">
        <svg v-if="!mobileOpen" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
          stroke-linecap="round" class="h-5 w-5" aria-hidden="true">
          <path d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
          class="h-5 w-5" aria-hidden="true">
          <path d="M6 6l12 12M18 6L6 18" />
        </svg>
      </button>
    </nav>

    <div v-show="mobileOpen" id="mobile-menu" class="border-t border-hrms-border bg-white lg:hidden">
      <div class="space-y-1 px-4 py-4 sm:px-6">
        <a v-for="link in navLinks" :key="`mobile-${link.target}`" :href="`#${link.target}`"
          class="block rounded-xl px-4 py-3 text-body-lg font-medium text-hrms-ink transition-colors hover:bg-hrms-bg hover:text-hrms-purple focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-pink"
          @click="onNavClick($event, link.target)">
          {{ link.label }}
        </a>
        <a :href="loginUrl"
          class="mt-2 block rounded-xl bg-brand-gradient px-4 py-3 text-center text-body-lg font-semibold text-white shadow-cta focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-hrms-purple focus-visible:ring-offset-2"
          @click="mobileOpen = false">
          Sign in
        </a>
      </div>
    </div>
  </header>
</template>
