<template>
  <div class="section-1">
    <div class="side-width">
      <div class="title-section">Почему стоит обратиться ко мне</div>
      <VueSlickCarousel class="description mobile" v-bind="settings">
        <div class="description__item">
          <img class="description__image" src="../assets/images/1_item.png" alt="1">
          <span class="description__title">С ГОЛОВОЙ В ПРОЕКТЕ</span>
          <div class="description__text">
            Гарантирую полное погружение в проект. Моя работа не в том, чтобы брать деньги 1 раз в месяц и тянуть время,
            а в том, чтобы бизнес процветал.<br><br>
            Беру деньги только за фактическую работу.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/2_item.png" alt="2">
          <span class="description__title">НЕ ДАЮ ПУСТЫХ ОБЕЩАНИЙ</span>
          <div class="description__text">
            Не знаю никаких секретов и волшебных таблеток, не даю пустых гарантий - могу обещать только то, что буду
            честно трудиться над вашим проектом.<br><br>
            Есть только ответственная методичная работа.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/3_item.png" alt="3">
          <span class="description__title">ТОЛЬКО ПРАВДА</span>
          <div class="description__text">
            Не морочу голову клиентам, которым не нужен сайт и не пытаюсь что то впарить. Если маркетинг
            вам не нужен - прямо об этом скажу.<br><br>
            У меня прозрачный договор без скрытых крючков, <a href="#" class="description__link">пример</a>.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/4_item.png" alt="4">
          <span class="description__title">БОЛЬШОЙ ОПЫТ</span>
          <div class="description__text">
            Занимаюсь маркетингом более 9 лет и за это время накопил опыт работы в крупных федеральных компаниях с
            оборотами более миллиарда рублей<br><br>
            Работал в лучших компаниях России
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/5_item.png" alt="5">
          <span class="description__title">ВСЕГДА НА СВЯЗИ</span>
          <div class="description__text">
            Стараюсь моментально отвечать на любые запросы со стороны клиентов.
            Большую часть работы делаю в выходные.<br><br>
            Есть сертификат Яндекса по интернет-маркетингу.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/6_item.png" alt="6">
          <span class="description__title">УПОР НА КАЧЕСТВО</span>
          <div class="description__text">
            Часто компании просто тянут резину, им не важно продвинуть сайт, им важно получить как можно больше
            денег за больший период.<br><br>
            Я мотивирован в получении крутого кейса.
          </div>
        </div>
      </VueSlickCarousel>
      <div class="description default">
        <div class="description__item">
          <img class="description__image" src="../assets/images/1_item.png" alt="1">
          <span class="description__title">С ГОЛОВОЙ В ПРОЕКТЕ</span>
          <div class="description__text">
            Гарантирую полное погружение в проект. Моя работа не в том, чтобы брать деньги 1 раз в месяц и тянуть время,
            а в том, чтобы бизнес процветал.<br><br>
            Беру деньги только за фактическую работу.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/2_item.png" alt="2">
          <span class="description__title">НЕ ДАЮ ПУСТЫХ ОБЕЩАНИЙ</span>
          <div class="description__text">
            Не знаю никаких секретов и волшебных таблеток, не даю пустых гарантий - могу обещать только то, что буду
            честно трудиться над вашим проектом.<br><br>
            Есть только ответственная методичная работа.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/3_item.png" alt="3">
          <span class="description__title">ТОЛЬКО ПРАВДА</span>
          <div class="description__text">
            Не морочу голову клиентам, которым не нужен сайт и не пытаюсь что то впарить. Если маркетинг
            вам не нужен - прямо об этом скажу.<br><br>
            У меня прозрачный договор без скрытых крючков, <a href="#" class="description__link">пример</a>.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/4_item.png" alt="4">
          <span class="description__title">БОЛЬШОЙ ОПЫТ</span>
          <div class="description__text">
            Занимаюсь маркетингом более 9 лет и за это время накопил опыт работы в крупных федеральных компаниях с
            оборотами более миллиарда рублей<br><br>
            Работал в лучших компаниях России
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/5_item.png" alt="5">
          <span class="description__title">ВСЕГДА НА СВЯЗИ</span>
          <div class="description__text">
            Стараюсь моментально отвечать на любые запросы со стороны клиентов.
            Большую часть работы делаю в выходные.<br><br>
            Есть сертификат Яндекса по интернет-маркетингу.
          </div>
        </div>
        <div class="description__item">
          <img class="description__image" src="../assets/images/6_item.png" alt="6">
          <span class="description__title">УПОР НА КАЧЕСТВО</span>
          <div class="description__text">
            Часто компании просто тянут резину, им не важно продвинуть сайт, им важно получить как можно больше
            денег за больший период.<br><br>
            Я мотивирован в получении крутого кейса.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'Description',
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
.description
  display: flex
  flex-wrap: wrap
  justify-content: space-between

  &.mobile
    display: none !important

  &__item
    display: flex
    flex-direction: column
    width: 30%

    &:not(:nth-child(4))
      margin-right: 30px

    &:nth-child(n+4)
      margin-top: 30px

  &__image
    width: 180px
    height: auto
    margin-bottom: 20px

  &__title
    margin-bottom: 20px
    font-size: 18px
    font-weight: 700
    line-height: 24px
    font-family: 'Unbounded', 'sans-serif'

  &__text
    font-size: 15px
    font-weight: 400
    font-family: 'Golos', 'sans-serif'
    line-height: 20px

  &__link
    color: rgba(230, 87, 101, 1)

@media (max-width: 480px)
  .description
    &.default
      display: none

    &__text
      margin-top: 10px

    &.mobile
      display: flex !important
      flex-direction: row
      flex-wrap: nowrap
      padding: 0 13px

      .slick-dots
        bottom: -40px
        text-align: left

        .slick-active
            button
              width: 20px

        li
          margin: 0 4px

          button
            width: 4px

    &__item
      width: 100%

</style>
