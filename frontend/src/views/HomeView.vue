<script setup>
import Navbar from '@/components/layout/Navbar.vue'
import Footer from '@/components/layout/Footer.vue'
import HeroSection from '@/components/landing/HeroSection.vue'
import TrustedBySection from '@/components/landing/TrustedBySection.vue'
import FeaturesSection from '@/components/landing/FeaturesSection.vue'
import BenefitsSection from '@/components/landing/BenefitsSection.vue'
import RolesSection from '@/components/landing/RolesSection.vue'
import CallToAction from '@/components/landing/CallToAction.vue'
</script>

<template>
  <div class="min-h-screen bg-white">
    <Navbar />
    <main>
      <HeroSection />
      <TrustedBySection />
      <FeaturesSection />
      <BenefitsSection />
      <RolesSection />
      <CallToAction />
    </main>
    <Footer />
  </div>
</template>
