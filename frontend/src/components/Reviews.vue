<template>
  <section class="section-6">
    <div class="reviews">
      <div class="reviews__wrap">
        <div class="title-section">Отзывы</div>
        <div>Некоторые отзывы обо мне и моей работе</div>
        <VueSlickCarousel class="reviews__content" v-bind="settings">
          <div class="reviews__item">
            <span class="reviews__company">1212»</span>
            <span class="reviews__author">Мария Стародубова</span>
            <div class="reviews__text">Зона ответственности клиента в договоре выше специализации клиента. Обслуживание
              нормальное,
              в принципе свои задачи выполнили и все работает. В договоре много зон ответственности клиента,
              что нашей компетенции не соответствовало и мы не могли контролировать сам процесс.
            </div>
            <a href="#" class="reviews__download">Смотреть pdf отзыва</a>
          </div>
          <div class="reviews__item">
            <span class="reviews__company">О323232»</span>
            <span class="reviews__author">Мария Стародубова</span>
            <div class="reviews__text">Зона ответственности клиента в договоре выше специализации клиента. Обслуживание
              нормальное,
              в принципе свои задачи выполнили и все работает. В договоре много зон ответственности клиента,
              что нашей компетенции не соответствовало и мы не могли контролировать сам процесс.
            </div>
            <a href="#" class="reviews__download">Смотреть pdf отзыва</a>
          </div>
          <div class="reviews__item">
            <span class="reviews__company">ООО 434354оз»</span>
            <span class="reviews__author">Мария Стародубова</span>
            <div class="reviews__text">Зона ответственности клиента в договоре выше специализации клиента. Обслуживание
              нормальное,
              в принципе свои задачи выполнили и все работает. В договоре много зон ответственности клиента,
              что нашей компетенции не соответствовало и мы не могли контролировать сам процесс.
            </div>
            <a href="#" class="reviews__download">Смотреть pdf отзыва</a>
          </div>
          <div class="reviews__item">
            <span class="reviews__company">ООО43455454хоз»</span>
            <span class="reviews__author">Мария Стародубова</span>
            <div class="reviews__text">Зона ответственности клиента в договоре выше специализации клиента. Обслуживание
              нормальное,
              в принципе свои задачи выполнили и все работает. В договоре много зон ответственности клиента,
              что нашей компетенции не соответствовало и мы не могли контролировать сам процесс.
            </div>
            <a href="#" class="reviews__download">Смотреть pdf отзыва</a>
          </div>
        </VueSlickCarousel>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'Reviews',
  components: { VueSlickCarousel },
  data () {
    return {
      'settings': {
        'arrows': true,
        'dots': false,
        'infinite': true,
        'slidesToShow': 3,
        'slidesToScroll': 1,
        'variableWidth': true,
        'responsive': [
          {
            'breakpoint': 480,
            'settings': {
              'arrows': false,
              'dots': true,
              'slidesToShow': 1,
              'slidesToScroll': 1,
              'adaptiveHeight': true
            }
          }
        ]
      }
    }
  }
}
</script>

<style lang="sass">
.reviews
  padding: 55px 0 0
  background: url('../assets/images/bg-section-7.png') no-repeat, linear-gradient(to bottom, rgba(247, 245, 249, 1) 95%, rgba(255, 255, 255, 1) 5%)

  &__wrap
    max-width: 1920px
    margin: 0 0 0 30%

    .title-section
      margin: 0 0 16px
      color: rgba(26, 5, 29, 1)

  &__content
    display: flex
    justify-content: space-between
    margin-top: 50px

    .slick-slide
      width: 450px !important
      padding: 5px 20px
      margin: 0 40px
      box-sizing: border-box

    .slick-list
      margin: 0 -20px

    .slick-arrow
      width: 30px
      height: 24px
      bottom: 0
      right: 0

      &:before
        content: none

      &.slick-prev
        right: 70px !important
        background: url('../assets/images/prev-arrow.png') no-repeat center center

      &.slick-next
        right: 0 !important
        background: url('../assets/images/next-arrow.png') no-repeat center center

  &__item
    width: 28%
    display: flex !important
    flex-direction: column
    padding: 40px
    background: #fff
    border-radius: 30px
    box-shadow: rgba(0, 0, 0, 0.07) 0 1px 4px

  &__company
    font-size: 12px
    font-weight: 500

  &__author
    margin: 2px 0 30px
    font-size: 18px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 24px

  &__text
    margin-bottom: 22px
    font-size: 15px
    line-height: 20px

  &__download
    display: flex
    align-items: center
    color: rgba(230, 87, 101, 1)
    font-size: 12px
    font-weight: 500
    line-height: 16px
    text-decoration: none
    text-transform: uppercase

    &:before
      content: ''
      display: block
      width: 24px
      height: 24px
      margin-right: 18px
      background: url('../assets/images/download-red.png') no-repeat

@media (max-width: 480px)
  .reviews
    padding: 30px 13px 0
    background: linear-gradient(to bottom, rgba(247, 245, 249, 1) 80%, rgba(255, 255, 255, 1) 5%)

    &__wrap
      margin: 0
      text-align: center

    &__author
      margin: 4px 0 10px

    &__content
      margin-top: 12px
      padding: 0
      text-align: left

      .slick-list
        margin: 0

        .slick-track
          width: 100% !important

          .slick-slide
            width: 90% !important
            padding: 10px 0
            margin: 0
            box-sizing: border-box

    &__item
      width: 100%
      padding: 20px

    .slick-arrow
      &.slick-prev
        left: calc(50% - 30px) !important

      &.slick-next
        left: calc(50% + 30px) !important

</style>
