<template>
  <section class="section-2">
    <div class="side-width related-prices-wrapper">
      <div class="related-prices">
        <div class="title-section">Цены на сопутствующие услуги</div>
        <div class="related-prices__wrap">
          <div class="related-prices__item">
            <div class="related-prices__top">
              <div class="related-prices__left-column">
                <span class="related-prices__title">Разработка сайтов</span>
                <div class="related-prices__description">Если нужно быстро понять почему сайт не привлекает трафик.
                </div>
              </div>
              <div class="related-prices__right-column">
                <ul>
                  <li>РЕЗУЛЬТАТ ЧЕРЕЗ 1-3 ДНЯ</li>
                  <li>ТЕХНИЧЕСКИЙ И КОММЕРЧЕСКИЙ АУДИТ</li>
                  <li>СРАВНЕНИЕ С КОНКУРЕНТАМИ</li>
                </ul>
              </div>
            </div>
            <hr>
            <div class="related-prices__bottom">
              <div class="related-prices__price-block">
                <span class="related-prices__price">500,000</span>
                <span class="related-prices__currency">рублей</span>
              </div>
              <button class="btn feedback">ОСТАВИТЬ ЗАЯВКУ</button>
            </div>
          </div>
          <div class="related-prices__item">
            <div class="related-prices__top">
              <div class="related-prices__left-column">
                <span class="related-prices__title">Разработка сайтов</span>
                <div class="related-prices__description">Если нужно быстро понять почему сайт не привлекает трафик.
                </div>
              </div>
              <div class="related-prices__right-column">
                <ul>
                  <li>РЕЗУЛЬТАТ ЧЕРЕЗ 1-3 ДНЯ</li>
                  <li>ТЕХНИЧЕСКИЙ И КОММЕРЧЕСКИЙ АУДИТ</li>
                  <li>СРАВНЕНИЕ С КОНКУРЕНТАМИ</li>
                </ul>
              </div>
            </div>
            <hr>
            <div class="related-prices__bottom">
              <div class="related-prices__price-block">
                <span class="related-prices__price">500,000</span>
                <span class="related-prices__currency">рублей</span>
              </div>
              <button class="btn feedback">ОСТАВИТЬ ЗАЯВКУ</button>
            </div>
          </div>
        </div>
        <VueSlickCarousel class="related-prices__wrap mobile" v-bind="settings">
          <div class="related-prices__item">
            <span class="prices__title">Разработка сайтов</span>
            <div class="prices__description">Если нужно быстро понять почему сайт не привлекает трафик.</div>
            <div class="prices__price">500,000</div>
            <span class="prices__currency">рублей</span>
            <div class="prices__info">
              <ul>
                <li>РЕЗУЛЬТАТ ЧЕРЕЗ 1-3 ДНЯ</li>
                <li>ТЕХНИЧЕСКИЙ И КОММЕРЧЕСКИЙ АУДИТ</li>
                <li>СРАВНЕНИЕ С КОНКУРЕНТАМИ</li>
              </ul>
            </div>
            <button class="btn feedback">ОСТАВИТЬ ЗАЯВКУ</button>
          </div>
          <div class="related-prices__item">
            <span class="prices__title">Настройка рекламы</span>
            <div class="prices__description">Если нужно быстро понять почему сайт не привлекает трафик.</div>
            <div class="prices__price">50,000</div>
            <span class="prices__currency">рублей</span>
            <div class="prices__info">
              <ul>
                <li>РЕЗУЛЬТАТ ЧЕРЕЗ 1-3 ДНЯ</li>
                <li>ТЕХНИЧЕСКИЙ И КОММЕРЧЕСКИЙ АУДИТ</li>
                <li>СРАВНЕНИЕ С КОНКУРЕНТАМИ</li>
              </ul>
            </div>
            <button class="btn feedback">ОСТАВИТЬ ЗАЯВКУ</button>
          </div>
        </VueSlickCarousel>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'RelatedPrices',
  components: { VueSlickCarousel },
  data () {
    return {
      'settings': {
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
.related-prices
  display: flex
  flex-direction: column
  padding: 60px 50px
  background: rgba(247, 245, 249, 1)
  border-radius: 100px

  &__wrap
    display: flex
    justify-content: space-between

    &.mobile
      display: none !important

  hr
    display: block
    width: 100%
    margin: 30px 0
    background: rgba(208, 201, 214, 1)

  .title-section
    text-align: center

  &__item
    width: 41%
    display: flex
    flex-direction: column
    padding: 40px
    background: #fff
    border-radius: 30px

  &__top
    display: flex

  &__bottom
    display: flex
    justify-content: space-between
    align-items: center

  &__price-block
    display: flex
    align-items: center

  &__price
    margin-right: 10px
    color: rgba(26, 5, 29, 1)
    font-size: 24px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

  &__currency
    font-size: 14px
    font-weight: 600
    font-family: 'Golos', 'sans-serif'

  .btn
    &.feedback
      padding: 11px 36px
      font-size: 14px

  &__left-column
    width: 45%

  &__title
    font-size: 18px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

  &__description
    margin-top: 16px
    font-size: 15px
    font-weight: 400
    font-family: 'Golos', 'sans-serif'
    line-height: 20px

  &__right-column
    ul
      margin: 0
      padding-left: 30px
      list-style: none

    ul > li
      position: relative
      display: flex
      align-items: center
      padding-left: 40px
      font-size: 12px
      font-weight: 500
      line-height: 16px

    ul > li:not(:first-child)
        margin: 20px 0 0 0

    ul > li:before
      content: ''
      display: block
      width: 25px
      height: 25px
      position: absolute
      left: 0
      background-image: url('../assets/images/check.svg')
      background-repeat: no-repeat

@media (max-width: 480px)
  .side-width
    &.related-prices-wrapper
      padding: 0 13px
      box-sizing: border-box

  .related-prices
    width: 100%
    padding: 30px 0 50px
    background: #f7f5f9
    border-radius: 30px

    &__info
      margin-top: 30px

      ul
        padding: 0

    &__wrap
      display: none

      &.mobile
        display: flex !important
        padding: 0 13px

        .slick-dots
          bottom: -40px

          .slick-active
            button
              width: 20px

          li
            margin: 0 4px

            button
              width: 4px

      .slick-list
        border-radius: 30px

    &__item
      width: 100%
      height: 480px
      display: flex !important
      justify-content: space-between
      padding: 20px
      border-radius: 30px
      box-sizing: border-box
      text-align: center

      .btn
        width: 100%
        margin-top: 35px !important
        padding: 20px 0 !important
        border-radius: 30px !important
        font-size: 15px !important

    &__description
      margin: 15px 0 10px

    &__price
      margin: 0
      font-size: 30px

    &__currency
      font-size: 10px
</style>
