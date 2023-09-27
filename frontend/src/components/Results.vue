<template>
  <section class="section-3 results-wrap">
    <div class="results">
      <div class="title-section">Результаты моей работы</div>
      <VueSlickCarousel class="results__wrap" v-bind="settings">
        <div class="results__item">
          <img src="../assets/images/graph.png" alt="">
          <div class="results__description">
            <span class="results__title">ПРОДВИЖЕНИЕ САЙТА АГЕНТСТВА НЕДВИЖИМОСТИ</span>
            <span class="results__info">Заявки (в месяц): было 142 - стало 257 | Срок работ - 6 месяцев</span>
          </div>
        </div>
        <div class="results__item">
          <img src="../assets/images/graph.png" alt="">
          <div class="results__description">
            <span class="results__title">ПРОДВИЖЕНИЕ САЙТА АГЕНТСТВА НЕДВИЖИМОСТИ</span>
            <span class="results__info">Заявки (в месяц): было 142 - стало 257 | Срок работ - 6 месяцев</span>
          </div>
        </div>
        <div class="results__item">
          <img src="../assets/images/graph.png" alt="">
          <div class="results__description">
            <span class="results__title">ПРОДВИЖЕНИЕ САЙТА АГЕНТСТВА НЕДВИЖИМОСТИ</span>
            <span class="results__info">Заявки (в месяц): было 142 - стало 257 | Срок работ - 6 месяцев</span>
          </div>
        </div>
        <div class="results__item">
          <img src="../assets/images/graph.png" alt="">
          <div class="results__description">
            <span class="results__title">ПРОДВИЖЕНИЕ САЙТА АГЕНТСТВА НЕДВИЖИМОСТИ</span>
            <span class="results__info">Заявки (в месяц): было 142 - стало 257 | Срок работ - 6 месяцев</span>
          </div>
        </div>
        <div class="results__item">
          <img src="../assets/images/graph.png" alt="">
          <div class="results__description">
            <span class="results__title">ПРОДВИЖЕНИЕ САЙТА АГЕНТСТВА НЕДВИЖИМОСТИ</span>
            <span class="results__info">Заявки (в месяц): было 142 - стало 257 | Срок работ - 6 месяцев</span>
          </div>
        </div>
      </VueSlickCarousel>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name: 'Results',
  components: { VueSlickCarousel },
  data () {
    return {
      'settings': {
        'arrows': false,
        'dots': true,
        'infinite': true,
        'slidesToShow': 4,
        'slidesToScroll': 2,
        'responsive': [
          {
            'breakpoint': 480,
            'settings': {
              'arrows': false,
              'dots': true,
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
@import "../assets/sass/slick"

.results
  max-width: 1920px
  margin: 0 auto
  display: flex
  flex-direction: column
  padding: 60px 0
  background: linear-gradient(rgba(247, 245, 249, 1) 55%, #fff 45%)

  .title-section
    margin: 0 auto

  &__item
    width: 25%
    display: flex
    text-align: center
    justify-content: center

    img
      width: 100%
      height: auto
      margin: 0 auto
      object-fit: cover

  &__description
    padding: 0 40px
    display: flex
    flex-direction: column

  &__title
    margin-bottom: 10px
    font-size: 15px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 20px

  &__info
    font-size: 12px
    font-weight: 500

@media (max-width: 480px)
  .section-3
    &.results-wrap
      padding: 0

  .results
    padding: 30px 0 70px !important
    background: rgba(247, 245, 249, 1)

    .title-section
      text-align: center

    .slick-dots
      bottom: -50px

      li
        margin: 0 4px

        button
          width: 4px

      .slick-active
        button
          width: 20px

    &__title
      color: #000

    &__info
      font-size: 11px
</style>
