<template>
  <header>
    <div class="side-width">
      <nav>
        <div class="logo">
          <a href="/" class="title">/ VYSOTSKY /</a>
          <span class="info">SEO-оптимизация и создание сайтов</span>
        </div>
        <div class="menu">
          <ul>
            <li class="active"><a href="#">ГЛАВНАЯ</a></li>
            <li><a href="#">ЗАКАЗАТЬ SEO</a></li>
            <li><a href="#">РАЗРАБОТКА САЙТОВ</a></li>
            <li><a href="#">БЛОГ</a></li>
          </ul>
          <button @click="showModal" class="btn call">ЗАКАЗАТЬ ЗВОНОК</button>
        </div>
        <span class="icon-menu-mobile" v-on:click="toggleMenu"></span>
        <transition name="fade">
          <div class="mobile-menu" id="mobile-menu" v-if="show">
            <div class="mm__bg mm__close"></div>
            <div class="mm__wrapper" id="mm__wrapper">
              <div class="mm__header">
                <span class="close-btn close-btn--red mm__close" v-on:click="toggleMenu"></span>
                <div class="mm__items">
                  <ul>
                    <li class="active"><a href="#">ГЛАВНАЯ</a></li>
                    <li><a href="#">ЗАКАЗАТЬ SEO</a></li>
                    <li><a href="#">РАЗРАБОТКА САЙТОВ</a></li>
                    <li><a href="#">БЛОГ</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </transition>
      </nav>
      <div class="wrapper">
        <div class="wrapper__left">
          <div class="wrap">
            <div class="wrap__title">ВЫВЕДУ ВАШ БИЗНЕС НА НОВЫЙ УРОВЕНЬ</div>
            <span class="wrap__text">Сделаю эффективный маркетинг для вашего бизнеса. Настрою прозрачную аналитику,
              приведу клиентов, увеличу конверсию сайта.</span>
          </div>
          <div class="consultation">
            <div class="consultation__example"><a href="#">Скачать пример договора</a></div>
            <div class="consultation__buttons">
              <button class="btn free-project">ОБСУДИТЬ ПРОЕКТ</button>
              <button class="btn purple">БЕСПЛАТНЫЙ АУДИТ</button>
            </div>
            <div class="consultation__info">Оптимизирую сайты сам, без перепродажи третьим лицам, из-за этого очень
              ограничен в количестве проектов на ведении и очень избирательно беру новые сайты на продвижение.
            </div>
          </div>
        </div>
        <div class="about">
          <div class="about__wrapper">
            <span class="position">Маркетолог и SEO-специалист</span>
            <span class="name">Высоцкий Кирилл</span>
            <ul>
              <li>Более 9 лет занимаюсь SEO</li>
              <li>Дипломированный маркетолог</li>
              <li>Обучаю SEO в онлайн-школе GeekBrains</li>
            </ul>
            <div class="diploma">
              <img src="../assets/images/diplom.png" alt="Сертификат маркетолога">
              <p class="diploma__link"><a href="#" target="_blank">СЕРТИФИКАТ МАРКЕТОЛОГА</a></p>
            </div>
          </div>
          <img class="photo" src="../assets/images/photo.png" alt="Фото">
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      show: false
    }
  },
  methods: {
    toggleMenu: function (event) {
      event.preventDefault()
      this.show = !this.show
    },
    showModal () {
      this.$parent.isModalVisible = true
    }
  }
}
</script>

<style lang="sass">
@import '../assets/sass/base'

.fade-enter-active .fade-leave-active
  transition: all .4s ease-in-out

.fade-enter-from, .fade-leave-to
  display: none
  visibility: hidden
  transform: translateX(-100%)

.close-btn
  position: relative
  width: 20px
  height: 20px
  -ms-transform: rotate(45deg)
  transform: rotate(45deg)
  cursor: pointer

  &:before
    width: 2px
    height: 18px
    left: 8px
    top: 0

  &:after
    height: 2px
    width: 18px
    top: 8px
    left: 0

  &:before, &:after
    content: ""
    background: #000
    position: absolute

  &--red:before,
  &--red:after
    background: #e65765

header
  background: url("../assets/images/bg-header.png") no-repeat top

  .side-width
    padding: 40px 0 0

  nav
    display: flex
    flex-direction: row
    justify-content: space-between
    align-items: center
    padding: 18px 25px 18px 40px
    background: #fff
    border-radius: 90px

    .logo
      .title
        margin-right: 30px
        color: #000
        font-size: 14px
        font-weight: 700
        line-height: 18px
        text-decoration: none

      .info
        font-size: 14px
        font-weight: 400
        line-height: 18px

    .mobile-menu
      position: fixed
      top: 0
      left: 0
      height: 100%
      width: 100%
      z-index: 100

      .mm__bg
        position: absolute
        left: 0
        top: 0
        width: 100%
        height: 100%
        background: rgba(20, 20, 20, 0.8)
        z-index: 100

      .mm__wrapper
        transition: all .4s ease-in-out
        overflow-y: auto
        position: relative
        width: 100%
        height: 100%
        z-index: 200
        touch-action: auto
        -ms-touch-action: auto
        background: #fff

        .mm__header
          .close-btn
            position: absolute
            top: 0
            right: 0
            margin-right: 15px
            margin-top: 15px

        .mm__items
          padding: 20px 13px

          ul
            margin: 0
            padding: 0
            line-height: 35px
            list-style: none

          ul > li
            font-size: 16px

            a
              color: #000
              text-decoration: none

    .menu
      display: flex

      ul
        display: flex
        align-items: center
        margin: 0
        padding: 0
        list-style: none
        font-size: 13px
        font-weight: 700
        font-family: 'Golos', 'sans-serif'

        li:not(:last-child)
          margin: 0 25px 0 0

        li.active
          a
            color: #E65765

        a
          color: #000
          text-decoration: none

    .call
      margin-left: 40px
      padding: 10px 20px

  .wrapper
    position: relative
    display: flex
    justify-content: space-between
    margin-top: 100px

    &__left
      width: 48%

      .wrap
        &__title
          margin-bottom: 25px
          color: #000
          font-size: 63px
          font-weight: 700
          font-family: 'Unbounded', 'sans-serif'
          line-height: 86px
          text-shadow: 5px 5px #fff

        &__text
          font-size: 15px
          font-weight: 400
          line-height: 20px

    .about
      width: 48%
      height: 100%
      position: absolute
      top: 0
      right: 0
      background: #fff url("../assets/images/bg-about.png") no-repeat bottom
      border: 1px solid rgba(216, 232, 242, 1)
      border-radius: 40px

      .about__wrapper
        position: relative
        display: flex
        flex-direction: column
        padding: 40px 44px

        .position
          color: rgba(63, 51, 86, 1)
          font-size: 15px
          font-weight: 700
          font-family: 'Unbounded', 'sans-serif'
          line-height: 20px

        .name
          margin: 10px 0 30px
          color: rgba(26, 5, 29, 1)
          font-size: 30px
          font-weight: 700
          font-family: 'Unbounded', 'sans-serif'
          line-height: 30px

        .diploma
          margin-top: 55px

          &__link
            width: max-content
            font-size: 10px
            font-weight: 400
            border-bottom: 1px dashed rgba(63, 51, 86, 1)

            a
              text-decoration: none

        ul
          margin: 0
          padding: 0
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
          background-image: url('../assets/images/check-red.png')
          background-repeat: no-repeat

      .photo
        width: 460px
        height: auto
        position: absolute
        bottom: 0
        right: 0
        border-radius: 40px

  .consultation
    display: flex
    flex-direction: column
    margin-top: 150px

    &__example
      display: flex
      align-items: center
      font-size: 11px
      line-height: 13px

      a
        text-decoration: none
        border-bottom: 1px dashed rgba(63, 51, 86, 1)

      &:before
        content: ''
        display: block
        margin-right: 15px
        width: 24px
        height: 24px
        float: left
        background: url("../assets/images/download.png") no-repeat

    &__buttons
      margin: 25px 0 25px

      .btn
        &.purple
          background: rgba(63, 51, 86, 1)

    &__info
      font-size: 11px
      line-height: 13px

@media (max-width: 480px)
  header
    padding: 0 13px !important
    background: url(/static/img/bg-header.4134925.png) no-repeat top
    background-size: auto 550px

    .side-width
      padding: 10px 0 0 !important

    nav
      display: flex
      justify-content: space-between
      padding: 20px

      .logo
        display: flex
        flex-direction: column
        .info
          font-size: 12px

      .icon-menu-mobile
        display: block
        width: 35px
        height: 35px
        background: url(../assets/images/icon-menu.png) no-repeat

      .menu
        display: none

    .wrapper
      flex-direction: column
      margin-top: 30px

      &__left
        width: 100%

        .wrap
          &__title
            font-size: 30px
            line-height: 44px

          &__text
            display: none

        .consultation
          margin-top: 35px

          &__example
            font-size: 10px

          &__buttons
            display: flex
            flex-direction: column
            justify-content: center
            margin: 25px 0 15px

            .btn
              font-size: 15px

              &:last-child
                margin-top: 14px

          &__info
            font-size: 10px

      .about
        position: initial
        width: 100%
        margin-top: 60px
        background: #fff url("../assets/images/bg-about-mobile.png") no-repeat bottom
        background-size: contain

        .about__wrapper
          padding: 25px

          .name
            font-size: 24px

          .diploma
            margin-top: 35px

        .photo
          width: auto
          height: 180px

</style>
