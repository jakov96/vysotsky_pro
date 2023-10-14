<template>
  <section class="section-2">
    <div class="wrapper">
      <div class="side-width">
        <div class="prices">
          <div class="title-section">Цены на SEO продвижение</div>
          <div class="prices__wrap">
            <div class="prices__item">
              <span class="prices__title">SEO-аудит</span>
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
            </div>
            <div class="prices__item">
              <span class="prices__title">SEO-продвижение сайта</span>
              <div class="prices__description">Продвину сайт за 2-3 месяца и увеличу трафик и количество заявок.</div>
              <div class="prices__price">100,000</div>
              <span class="prices__currency">рублей в месяц</span>
              <div class="prices__info">
                <ul>
                  <li>ГАРАНТИЯ УВЕЛИЧЕНИЯ ТРАФИКА</li>
                  <li>ПОДРОБНАЯ ОТЧЕТНОСТЬ</li>
                  <li>УВЕЛИЧЕНИЕ КОНВЕРСИИ САЙТА</li>
                </ul>
              </div>
            </div>
            <div class="prices__item">
              <span class="prices__title">Персональная консультация</span>
              <div class="prices__description">Полезная консультация на любую тему связанную с проектом.</div>
              <div class="prices__price">5,000</div>
              <span class="prices__currency">рублей</span>
              <div class="prices__info">
                <ul>
                  <li>ЛЮБЫМ УДОБНЫМ СПОСОБОМ</li>
                  <li>ГАРАНТИРУЮ ПОЛЕЗНОСТЬ</li>
                  <li>ЗАПИСЬ КОНСУЛЬТАЦИИ</li>
                </ul>
              </div>
            </div>
          </div>
          <VueSlickCarousel class="prices__wrap mobile" v-bind="settings">
            <div class="prices__item">
              <span class="prices__title">SEO-аудит</span>
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
            <div class="prices__item">
              <span class="prices__title">SEO-продвижение сайта</span>
              <div class="prices__description">Продвину сайт за 2-3 месяца и увеличу трафик и количество заявок.</div>
              <div class="prices__price">100,000</div>
              <span class="prices__currency">рублей в месяц</span>
              <div class="prices__info">
                <ul>
                  <li>ГАРАНТИЯ УВЕЛИЧЕНИЯ ТРАФИКА</li>
                  <li>ПОДРОБНАЯ ОТЧЕТНОСТЬ</li>
                  <li>МОНИТОРИНГ КОНКУРЕНТОВ</li>
                  <li>УВЕЛИЧЕНИЕ КОНВЕРСИИ САЙТА</li>
                </ul>
              </div>
              <button class="btn order">ЗАКАЗАТЬ</button>
            </div>
            <div class="prices__item">
              <span class="prices__title">Персональная консультация</span>
              <div class="prices__description">Полезная консультация на любую тему связанную с проектом.</div>
              <div class="prices__price">5,000</div>
              <span class="prices__currency">рублей</span>
              <div class="prices__info">
                <ul>
                  <li>ЛЮБЫМ УДОБНЫМ СПОСОБОМ</li>
                  <li>ГАРАНТИРУЮ ПОЛЕЗНОСТЬ</li>
                  <li>ЗАПИСЬ КОНСУЛЬТАЦИИ</li>
                </ul>
              </div>
              <button class="btn feedback">ОСТАВИТЬ ЗАЯВКУ</button>
            </div>
          </VueSlickCarousel>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'Prices',
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
.section-2
  .wrapper
    background: url('../assets/images/bg-section-2-revert.png') no-repeat left center, url('../assets/images/bg-section-2.png') no-repeat right center

.prices
  display: flex
  flex-direction: column
  padding: 60px 50px
  border-radius: 100px
  background: rgba(247, 245, 249, 1) url('../assets/images/bg-section.png') no-repeat bottom

  &__wrap
    display: flex
    justify-content: space-between
    align-items: center

    &.mobile
      display: none !important

  .title-section
    text-align: center

  &__item
    width: 24%
    display: flex
    flex-direction: column
    align-items: center
    padding: 40px
    background: #fff
    border-radius: 30px

  &__description
    margin: 50px 0 20px
    color: rgba(63, 51, 86, 1)
    font-size: 15px
    text-align: center

  &__price
    margin-bottom: 10px
    color: rgba(26, 5, 29, 1)
    font-size: 44px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 60px

  &__currency
    font-size: 14px
    font-weight: 600
    font-family: 'Golos', 'sans-serif'
    line-height: 10px

  &__info
    margin-top: 40px

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

  .btn
    width: 100%
    margin-top: 25px

    &.feedback
      padding: 11px 0
      border-radius: 20px
      font-size: 14px

    &.order
      padding: 20px 0
      border-radius: 30px
      font-size: 18px

  &__title
    font-size: 18px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

@media (max-width: 480px)
  .section-2
    .wrapper
      padding: 0 13px
      background: none
      box-sizing: border-box

  .prices
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
