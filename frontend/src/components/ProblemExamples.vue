<template>
  <section class="section-3">
    <div class="problem-examples">
      <div class="side-width">
        <div class="problem-examples__header">
          <div class="title-section">Решаю проблемы клиентов</div>
          <div class="problem-examples__info">Примеры того, как решаются проблемы моих клиентов. У каждого уникальная
            задача, для решения которой требуются уникальные решения.
          </div>
        </div>
      </div>
      <VueSlickCarousel class="problem-examples__content" v-bind="settings">
        <div class="problem-examples__item">
          <span class="problem-examples__title">Кажется что сайт не нравится пользователям?</span>
          <div class="problem-examples__text">Может и не кажется. Проведу юзабилити аудит с помощью Яндекс Метрики и
            асессоров. Докажу аналитически, в чем проблемы сайта, дам готовые рекомендации для внедрения.
          </div>
        </div>
        <div class="problem-examples__item">
          <span class="problem-examples__title">Нужны новые источники лидов?</span>
          <div class="problem-examples__text">Не проблема. Креативно подойду к решению задачи.
            Найду новые источники трафика.
          </div>
        </div>
        <div class="problem-examples__item">
          <span class="problem-examples__title">Думаешь стоит ли сделать мобильное приложение?</span>
          <div class="problem-examples__text">Возможно стоит. Приходи - обсудим, посчитаем затраты и эффективность.
            А затем я найду подходящую для реализации команду.
          </div>
        </div>
        <div class="problem-examples__item">
          <span class="problem-examples__title">Сомневаешься стоит ли вкладывать деньги в блог?</span>
          <div class="problem-examples__text">Сомневаться нормально. Блог редко напрямую побуждает к покупке.
            Стоит проанализировать его эффективность и оценить возможные затраты и “выхлоп”.
          </div>
        </div>
        <div class="problem-examples__item">
          <span class="problem-examples__title">Раздумываешь создать ли блог?</span>
          <div class="problem-examples__text">Приходи за рекомендациями. Проанализирую конкурентов. Составим список
            тем, найдем редактора и подготовим SEO требования для блога.
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
  name: 'ProblemExamples',
  components: { VueSlickCarousel },
  data () {
    return {
      'settings': {
        'arrows': true,
        'dots': false,
        'infinite': false,
        'slidesToShow': 4,
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
@import "../assets/sass/slick"

.problem-examples
  max-width: 1920px
  margin: 0 auto

  &__header
    display: flex
    justify-content: space-between
    margin-bottom: 45px

    .title-section
      margin: 0

  &__info
    width: 50%
    font-size: 15px
    font-weight: 400
    line-height: 20px

  &__content
    margin-left: calc((100% - 1160px) / 2)
    padding-right: 65px
    display: flex
    justify-content: space-between

  .slick-slide
    width: 260px !important
    padding: 5px 20px
    margin: 0 20px
    box-sizing: border-box

  .slick-list
    margin: 0 -40px

  &__item
    display: flex
    flex-direction: column
    padding: 30px
    border-radius: 30px
    box-shadow: rgba(0, 0, 0, 0.07) 0 1px 4px

  &__title
    color: rgba(230, 87, 101, 1)
    font-size: 15px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 20px

  &__text
    margin-top: 20px
    font-size: 15px
    line-height: 20px

  .slick-arrow
    top: 60%
    width: 30px
    height: 24px

    &:before
      content: none

  .slick-prev
    left: 0
    background: url('../assets/images/prev-arrow.svg') no-repeat center center

  .slick-next
    left: 30px
    right: initial
    background: url('../assets/images/next-arrow.svg') no-repeat center center

@media (max-width: 480px)
  .problem-examples
    &__header
      flex-direction: column

    &__info
      width: 100%
      margin-top: 20px

    &__content
      margin-left: 0

</style>
