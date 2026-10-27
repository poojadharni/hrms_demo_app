export function useSectionScroll() {
  function prefersReducedMotion() {
    return (
      typeof window !== 'undefined' &&
      window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches
    )
  }

  function scrollToSection(id) {
    const element = document.getElementById(id)
    if (!element) return
    element.scrollIntoView({
      behavior: prefersReducedMotion() ? 'auto' : 'smooth',
      block: 'start',
    })
  }

  return { scrollToSection }
}
