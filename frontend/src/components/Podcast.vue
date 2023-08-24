<template>
  <section class="section-3 podcast">
    <div class="side-width">
      <div class="podcast">
        <div><img src="../assets/images/play.png" alt=""></div>
        <div class="podcast__info">
          <div class="podcast__title">Рассказываю о SEO на подкасте «Профориентация» в Yandex Music</div>
          <span class="podcast__text">Был приглашен на подкаст о маркетинге как эксперт в области SEO. Послушайте) мы старались,
        чтобы было интересно)</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Podcast'
}
</script>

<style lang="sass">
.section-3
  &.podcast
    max-width: 1920px
    margin: 0 auto
    background: url('../assets/images/soundtrack.png') no-repeat left center, url('../assets/images/soundtrack-2.png') no-repeat right center

.podcast
  display: flex
  align-items: center

  &__info
    display: flex
    flex-direction: column
    margin-left: 70px

  &__title
    margin-bottom: 40px
    color: rgba(26, 5, 29, 1)
    font-size: 37px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 42px

  &__text
    font-size: 15px
    line-height: 20px

</style>
