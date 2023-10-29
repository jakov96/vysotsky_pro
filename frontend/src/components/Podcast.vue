<template>
  <section class="section-3 podcast">
    <div class="side-width">
      <div class="podcast">
        <a href="https://music.yandex.ru/album/23305928/track/107558099" target="_blank"><img src="../assets/images/play.png" alt="Play"></a>
        <div class="podcast__info">
          <div class="podcast__title">Рассказываю о SEO на подкасте «Профориентация» в Yandex Music</div>
          <span class="podcast__text">Был приглашен на подкаст о маркетинге как эксперт в области SEO.
            Послушайте) мы старались, чтобы было интересно)</span>
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
    margin: 100px auto 0
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

@media (max-width: 480px)
  .section-3
    &.podcast
      flex-direction: column
      padding: 0
      background: url('../assets/images/soundtrack-mobile.png') no-repeat left top, url('../assets/images/soundtrack-mobile-2.png') no-repeat right top

  .podcast
    flex-direction: column

    img
      width: 160px
      height: 160px

    &__title
      margin: 40px 0 20px
      font-size: 22px
      line-height: 29px

    &__info
      width: 100%
      margin: 0

    &__title
      padding: 0 13px

    &__text
      padding: 0 13px
</style>
