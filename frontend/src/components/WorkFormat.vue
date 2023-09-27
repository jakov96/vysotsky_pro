<template>
  <section class="section-3">
    <div class="side-width">
      <div class="bounded">
        <div class="work-format">
          <div class="work-format__header">
            <div class="title-section">Формат работы</div>
            <div class="work-format__info">Придерживаюсь порядка и прозрачности во всем. План работ и статусы по задачам
              доступны 24/7. По любой задаче можно написать вопрос или уточнить даже с мобильного телефона.
              <a class="link" href="#">Вот пример</a>.
            </div>
          </div>
          <div class="work-format__content">
            <div class="work-format__item">
              <img src="../assets/images/calendar.png" alt="">
              <span class="work-format__title">Составляю план работ и согласую с заказчиком</span>
            </div>
            <div class="work-format__item">
              <img src="../assets/images/status.png" alt="">
              <span class="work-format__title">Заказчик видит все статусы по задачам</span>
            </div>
            <div class="work-format__item">
              <img src="../assets/images/clock.png" alt="">
              <span class="work-format__title">Отчет в конце каждого месяца</span>
            </div>
          </div>
          <div class="work-format__description">Сроки рассчитываются индивидуально в зависимости от масштаба и сложности
            проекта. Срок от начала работ до первых результатов около 1 месяца.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'WorkFormat'
}
</script>

<style lang="sass">
.work-format
  &__header
    display: flex
    justify-content: space-between
    margin-bottom: 50px

  &__info
    width: 50%
    font-size: 15px
    font-weight: 400
    line-height: 20px

  &__content
    display: flex
    justify-content: space-between
    border: 1px solid rgba(208, 201, 214, 1)
    border-radius: 30px

  &__item
    width: 17%
    display: flex
    flex-direction: column
    align-items: center
    padding: 34px 36px
    background: rgba(247, 245, 249, 1)
    border-radius: 30px

  &__title
    margin-top: 30px
    font-size: 15px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 20px
    text-align: center

  &__description
    margin-top: 30px
    color: rgba(240, 132, 143, 1)
    font-size: 17px
    font-weight: 500
    line-height: 22px
    text-transform: uppercase

@media (max-width: 480px)
  .work-format
    padding: 0 13px

    &__header
      flex-direction: column
      margin-bottom: 30px

    &__info
      width: 100%
      font-size: 14px

    &__content
      flex-direction: column
      border: none

    &__description
      margin-top: 20px
      font-size: 15px

    &__item
      width: 100%
      margin-bottom: 10px
      padding: 20px
      background: #F7F5F9 url('../assets/images/bg-section-mobile-2.png') no-repeat left bottom
      background-size: cover
      border-radius: 45px
      box-sizing: border-box

      &:last-child
        margin-bottom: 0

    &__title
      order: 0
      margin: 0

    img
      order: 1

</style>
