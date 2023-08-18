<template>
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
          <button class="btn feedback">ОСТАВИТЬ ЗАЯВКУ</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Prices'
}
</script>

<style lang="sass">
.prices
  display: flex
  flex-direction: column
  padding: 60px 50px
  background: rgba(247, 245, 249, 1)
  border-radius: 100px

  &__wrap
    display: flex
    justify-content: space-between

  .title-section
    text-align: center

  &__item
    width: 25%
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

  .btn
    &.feedback
      width: 100%
      margin-top: 25px
      padding: 11px 0
      font-size: 14px

  &__left-column
    width: 45%

  &__title
    font-size: 18px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

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
      font-weight: 600
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
      background-image: url('../assets/images/check.png')
      background-repeat: no-repeat

</style>
