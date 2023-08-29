<template>
  <section class="section-3">
    <div class="side-width">
      <div class="prices-detail">
        <div class="prices-detail__description">
          <div class="prices-detail__title">Из чего складывается стоимость?</div>
          <div class="prices-detail__text">Стоимость формируется для каждого проекта индивидуально, потому что список
            работ и их объем могут сильно различаться от проекта к проекту.
          </div>
        </div>
        <div class="prices-detail__checklist">
          <div class="prices-detail__left">
            <ul>
              <li>Оценка приоритетов бизнеса клиента + анализ источников трафика и лидов клиента</li>
              <li>Анализ конкурентов - источники трафика, объемы трафика, объем продаж - сильные и слабые стороны</li>
              <li>Формирование плана работ</li>
              <li>Текстовые факторы - работы по текстовой оптимизации</li>
            </ul>
          </div>
          <div class="prices-detail__right">
            <ul>
              <li>Поведенческие факторы - работы с юзабилити сайта и улучшение поведения пользователей на сайте</li>
              <li>Технические факторы - устранение проблем с индексацией ресурса</li>
              <li>Ссылочные факторы - улучшение упоминаемости в интернете и др.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'PricesDetail'
}
</script>

<style lang="sass">
.prices-detail
  display: flex
  justify-content: space-between

  &__description
    width: 40%
    display: flex
    flex-direction: column

  &__title
    color: #000
    font-size: 42px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 48px

  &__text
    margin-top: 40px
    font-size: 15px
    line-height: 20px

  &__checklist
    width: 50%
    display: flex

    ul
      margin: 0
      padding-left: 30px
      list-style: none

    ul > li
      position: relative
      display: flex
      align-items: center
      padding-left: 40px
      color: #000
      font-size: 12px
      font-weight: 500
      line-height: 16px
      text-transform: uppercase

    ul > li:not(:first-child)
        margin: 24px 0 0 0

    ul > li:before
      content: ''
      display: block
      width: 25px
      height: 25px
      position: absolute
      left: 0
      background-image: url('../assets/images/check-red.png')
      background-repeat: no-repeat

@media (max-width: 480px)
  .prices-detail
    flex-direction: column

    &__description
      width: 100%

    &__title
      font-size: 28px
      line-height: 34px

    &__text
      margin: 20px 0 30px
      font-size: 14px

    &__checklist
      width: 100%
      flex-direction: column

      ul
        padding: 0

      ul > li:not(:first-child)
        margin: 10px 0 0 0

    &__right
      margin-top: 10px
</style>
