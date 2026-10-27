import { computed } from 'vue'

export function useLoginUrl() {
  const loginUrl = computed(() => {
    const origin =
      typeof window !== 'undefined' ? window.location.origin : ''
    return `${origin}/login`
  })

  return { loginUrl }
}
