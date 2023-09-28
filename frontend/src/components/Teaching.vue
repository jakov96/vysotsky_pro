<template>
  <div class="section-2">
    <div class="teaching">
      <div class="side-width">
        <div class="title-section">Преподавание в GeekBrains</div>
      </div>
      <div class="teaching__content">
        <div class="teaching__info">
          <p>Преподаю SEO в университете GeekBrains на факультете маркетинга.</p>
          <p>Часто выступаю как эксперт по SEO.</p>
          <p>Разработал и внедрил собственную программу по SEO по которой студенты учатся по сей день.</p>
        </div>
        <VueSlickCarousel class="teaching__photos" v-bind="settings">
          <img src="../assets/images/card-1.png" alt="">
          <img src="../assets/images/card-2.png" alt="">
          <img src="../assets/images/card-3.png" alt="">
          <img src="../assets/images/card-4.png" alt="">
        </VueSlickCarousel>
      </div>
    </div>
  </div>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'Teaching',
  components: { VueSlickCarousel },
  data () {
    return {
      'settings': {
        'arrows': true,
        'dots': false,
        'infinite': true,
        'slidesToShow': 3,
        'slidesToScroll': 2,
        'variableWidth': true,
        'responsive': [
          {
            'breakpoint': 480,
            'settings': {
              'arrows': true,
              'dots': false,
              'slidesToShow': 1,
              'slidesToScroll': 1
            }
          }
        ]
      }
    }
  }
}
</script>

<style lang="sass">
.teaching
  max-width: 1920px
  margin: 0 auto

  &__content
    position: relative
    height: 300px
    margin-left: calc((100% - 1160px) / 2)
    padding-right: 65px
    display: flex

  &__info
    width: 25%
    margin-right: 40px
    font-size: 15px

  &__photos
    width: 65%
    position: initial !important

    .slick-slide
      margin: 0 20px

    .slick-arrow
      width: 30px
      height: 24px

      &:before
        content: none

      &.slick-prev
        top: 100% !important
        left: 0
        background: url('../assets/images/prev-arrow.png') no-repeat center center

      &.slick-next
        top: 100% !important
        left: 30px
        right: initial
        background: url('../assets/images/next-arrow.png') no-repeat center center

@media (max-width: 480px)
  .teaching
    padding: 0 13px

    .title-section
      font-size: 22px

    &__content
      height: auto
      flex-direction: column
      margin-left: 0

    &__info
      width: 100%
      font-size: 14px

    &__photos
      width: 100%
      margin-top: 20px

      img
        width: auto
        height: 185px

      .slick-arrow
        &.slick-prev,
        &.slick-next
          top: calc(100% + 40px) !important
</style>
