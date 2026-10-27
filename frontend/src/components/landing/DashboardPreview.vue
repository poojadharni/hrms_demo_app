<script setup>
import dashboardPreviewImage from '@/assets/dashboard-preview.png'
</script>

<template>
  <figure class="overflow-hidden rounded-2xl border border-hrms-border bg-white shadow-panel">
    <img
      :src="dashboardPreviewImage"
      alt="PeopleOS workforce dashboard showing employee, leave, attendance, and payroll overviews"
      class="block h-auto w-full"
    />
  </figure>
</template>
