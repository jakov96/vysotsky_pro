<template>
  <footer>
    <div class="head">
      <div class="side-width">
        <div class="head__logo">
          <div class="head__logo-wrap">
            <span class="head__title">/ VYSOTSKY /</span>
            <span class="head__info">SEO-оптимизация и создание сайтов</span>
          </div>
          <div class="head__social">
            <a href="#" target="_blank" class="head__icon telegram"></a>
            <a href="#" target="_blank" class="head__icon whatsapp"></a>
            <a href="#" target="_blank" class="head__icon facetime"></a>
          </div>
        </div>
        <button @click="showModal" class="btn">ЗАКАЗАТЬ ЗВОНОК</button>
      </div>
    </div>
    <div class="side-width">
      <div class="bottom">
        <div class="bottom__left">
          <div class="bottom__quote">
            <span class="bottom__quote-text">И в мире нет таких вершин, что взять нельзя.</span>
            <span class="bottom__quote-author">© Владимир Высоцкий</span>
          </div>
          <div class="bottom__quote">
            <span class="bottom__quote-text">В том числе в SEO ;).</span>
            <span class="bottom__quote-author">© Кирилл Высоцкий</span>
          </div>
        </div>
        <div class="bottom__right">
          <div class="bottom__menu">
            <span class="bottom__menu-title">Услуги SEO</span>
            <a href="#" class="bottom__menu-item">SEO аудит сайта</a>
            <a href="#" class="bottom__menu-item">SEO продвижение</a>
            <a href="#" class="bottom__menu-item">Контент маркетинг</a>
            <a href="#" class="bottom__menu-item">Поисковый маркетинг</a>
            <a href="#" class="bottom__menu-item">Подготовка нового сайта к SEO</a>
          </div>
          <div class="bottom__menu">
            <span class="bottom__menu-title">Услуги разработки</span>
            <a href="#" class="bottom__menu-item">Создание лендинга</a>
            <a href="#" class="bottom__menu-item">Создание сайта услуг</a>
            <a href="#" class="bottom__menu-item">Создание интернет-магазина</a>
          </div>
          <div class="bottom__menu">
            <span class="bottom__menu-title">Обучение</span>
            <span href="#" class="bottom__menu-title">Блог</span>
          </div>
        </div>
      </div>
      <div class="copyright">
        <span class="copyright__author">2018-{{ new Date().getFullYear() }} Высоцкий Кирилл Алексеевич</span>
        <span class="copyright__title">VYSOTSKY.PRO</span>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  methods: {
    showModal () {
      this.$parent.isModalVisible = true
    }
  }
}
</script>

<style lang="sass">
footer
  margin: 150px 0 40px

.head
  padding: 30px 0
  border-top: 1px solid rgba(236, 233, 241, 1)
  border-bottom: 1px solid rgba(236, 233, 241, 1)
  border-radius: 150px 150px 0 0

  .side-width
    display: flex
    flex-direction: row
    align-items: center
    justify-content: space-between
    padding: 0

  &__logo
    display: flex
    align-items: center

  .btn
    padding: 11px 20px

  &__title
    margin-right: 30px
    color: #000
    font-size: 14px
    font-weight: 700
    line-height: 16px

  &__info
    font-size: 13px
    line-height: 18px

  &__social
    display: flex
    margin-left: 50px

  &__icon
    display: block
    width: 30px
    height: 30px

    &:not(:last-child)
      margin-right: 16px

    &.telegram
      background: url("../assets/images/telegram.svg") no-repeat center

    &.whatsapp
      background: url("../assets/images/whatsapp.svg") no-repeat center

    &.facetime
      background: url("../assets/images/facetime.svg") no-repeat center

.bottom
  display: flex
  padding: 10px 0 115px

  &__left
    width: 60%
    display: flex
    flex-direction: column

  &__quote
    display: flex
    flex-direction: column
    color: rgba(26, 5, 29, 1)

    &:not(:last-child)
      margin-bottom: 24px

  &__quote-text
    margin-bottom: 10px
    font-size: 15px
    font-weight: 500
    line-height: 20px

  &__quote-author
    font-size: 11px
    line-height: 13px

  &__right
    width: 60%
    display: flex
    justify-content: space-around
    border-left: 1px solid rgba(236, 233, 241, 1)

  &__menu
    display: flex
    flex-direction: column

  &__menu-title
    margin-bottom: 20px
    font-size: 12px
    font-weight: 500
    line-height: 16px
    text-transform: uppercase

  &__menu-item
    color: rgba(63, 51, 86, 1)
    font-size: 13px
    line-height: 18px
    text-decoration: none

    &:not(:last-child)
      margin-bottom: 10px

.copyright
  display: flex
  justify-content: space-between

  &__author
    font-size: 13px
    line-height: 18px

  &__title
    font-size: 14px
    font-weight: 700

@media (max-width: 480px)
  footer
    margin: 100px 0 0

  .head
    border: none

    .side-width
      flex-direction: column
      align-items: flex-start

    &__logo
      width: 100%
      flex-direction: column
      align-items: flex-start

    &__logo-wrap
      width: 100%
      display: flex
      flex-direction: column
      padding: 20px 40px
      border: 1px solid rgba(236, 233, 241, 1)
      border-radius: 60px 60px 0 0
      box-sizing: border-box

    &__title
      margin: 0

    &__social
      margin: 30px 0 20px
      padding: 0 40px

    .btn
      margin-left: 40px

  .bottom
    flex-direction: column
    padding: 30px 40px

    &__left
      width: 100%

    &__right
      width: 100%
      flex-direction: column
      border: none

    &__menu
      margin-top: 30px

    &__menu-title
      font-weight: 700

  .copyright
    flex-direction: column
    padding: 20px 40px 30px

    &__title
      margin-top: 10px
</style>
