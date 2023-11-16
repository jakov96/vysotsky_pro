<template>
  <section class="section-3 results-wrap">
    <div class="results">
      <div class="title-section">Результаты моей работы</div>
      <VueSlickCarousel class="results__wrap" v-bind="settings">
        <div v-for="(result, index) in results" :key="index" class="results__item">
          <img :src="result.img" :alt="result.title">
          <div class="results__description">
            <span class="results__title">{{ result.title }}</span>
            <span class="results__info">{{ result.result }}</span>
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
  components: {VueSlickCarousel},
  data () {
    return {
      'results': [
        {
          'img': require('../assets/images/graph.png'),
          'title': 'Агентство недвижимости (риелторские услуги)',
          'result': 'Заявки (в месяц): было 142 - стало 257; Срок работ - 6 месяцев'
        },
        {
          'img': require('../assets/images/graph-1.png'),
          'title': 'Ремонт холодильников (услуги)',
          'result': 'Заявки (в месяц): было 3 - стало 32; Срок работ - 2 месяца'
        },
        {
          'img': require('../assets/images/graph-2.png'),
          'title': 'Продажа подшипников (интернет-магазин)',
          'result': 'Заявки (в месяц): было 142 - стало 257; Срок работ - 4 месяца'
        },
        {
          'img': require('../assets/images/graph-3.png'),
          'title': 'Хочешь чтобы это был график твоего сайта?',
          'result': 'Просто оставь заявку и я перезвоню через 10 минут, чтобы обсудить детали'
        },
        {
          'img': require('../assets/images/graph-4.png'),
          'title': 'Продажа алкогольной продукции (интернет-магазин)',
          'result': 'Трафик (в месяц): было 17,160 - стало 300,000; Срок работ - 7 месяцев'
        },
        {
          'img': require('../assets/images/graph-5.png'),
          'title': 'Продажа автозапчастей (интернет-магазин)',
          'result': 'Заявки (в месяц): было 43,371 - стало 97,713; Срок работ - 6 месяцев'
        },
        {
          'img': require('../assets/images/graph-6.jpg'),
          'title': 'Блог о маркетинге (инфо-сайт)',
          'result': 'Трафик (в месяц): было 24,392 - стало 70,368; Срок работ - 10 месяцев'
        },
        {
          'img': require('../assets/images/graph-7.png'),
          'title': 'Грузоперевозки (услуги)',
          'result': 'Трафик: было 1975 - стало 11,297; Срок работ - 5 месяцев'
        },
        {
          'img': require('../assets/images/graph-8.png'),
          'title': 'Сайт страховой компании',
          'result': 'Рост позиций и трафика по очень конкурентной нише "КАСКО" в Москве'
        }
      ],
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

  &__wrap
    margin-top: 50px
    height: 350px

    .slick-list
      .slick-slide
        margin: 0 20px

    .slick-dots
      bottom: -100px

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
    margin-top: 30px
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

    &__wrap
      .slick-list
        .slick-slide
          margin: 0

      .slick-dots
        bottom: -60px

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
