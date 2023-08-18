<template>
  <div class="section-1">
    <div class="side-width">
      <div class="title-section">Какие услуги предоставляю</div>
      <div class="items">
        <div class="item">
          <span class="icon promotion"></span>
          <span class="title">SEO - продвижение</span>
          <span>что входит в услугу:</span>
          <div class="description">
            <ul>
              <li>анализ ниши и конкурентов</li>
              <li>сбор семантического ядра</li>
              <li>seo аудиты</li>
              <li>оптимизация сайта</li>
              <li>доработки конверсии сайта</li>
              <li>настройка аналитики</li>
            </ul>
          </div>
          <button class="btn">ЗАКАЗАТЬ</button>
        </div>
        <div class="item">
          <span class="icon develop"></span>
          <span class="title">Разработка сайтов</span>
          <span>что входит в услугу:</span>
          <div class="description">
            <ul>
              <li>подготовка структуры сайта</li>
              <li>формирование прототипов сайта</li>
              <li>разработка дизайна</li>
              <li>программирование сайта</li>
              <li>наполнение контентом</li>
              <li>настройка аналитики</li>
            </ul>
          </div>
          <button class="btn">ЗАКАЗАТЬ</button>
        </div>
        <div class="item advertising">
          <span class="icon advertising"></span>
          <span class="title">Настройка рекламы</span>
          <span>что входит в услугу:</span>
          <div class="description">
            <ul>
              <li>анализ ниши и конкурентов</li>
              <li>подбор ключевых слов</li>
              <li>запуск рекламной кампаний</li>
              <li>корректировка кампании</li>
              <li>доработки конверсии сайта</li>
              <li>настройка аналитики</li>
            </ul>
          </div>
          <button class="btn">ЗАКАЗАТЬ</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Services'
}
</script>

<style lang="sass">
@import '../assets/sass/base'

.items
  width: 100%
  display: flex

  .item
    width: 32%
    display: flex
    flex-direction: column
    justify-content: space-between
    padding: 42px
    border-radius: 30px
    box-sizing: border-box
    box-shadow: 0 24px 94px 0 #00000012

    &:not(:last-child)
      margin-right: 40px

    .icon
      display: block
      width: 80px
      height: 60px

      border-radius: 40px

      &.promotion
        background: #ECE9F1 url("../assets/images/promotion.png") no-repeat center

      &.develop
        background: #ECE9F1 url("../assets/images/develop.png") no-repeat center

      &.advertising
        background: #ECE9F1 url("../assets/images/advertising.png") no-repeat center

    .title
      margin: 30px 0 15px 0
      font-size: 18px
      font-weight: 700
      font-family: 'Unbounded', 'sans-serif'
      line-height: 24px
      color: #000

    .description
      margin-top: 30px
      font-size: 15px
      font-weight: 400
      font-family: Golos, 'sans-serif'

      ul
        padding-left: 25px

    .btn
      margin-top: 40px
      padding: 20px 95px
      background: #3F3356
      border-radius: 30px

</style>
