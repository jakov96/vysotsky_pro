<template>
  <header>
    <div class="side-width">
      <nav>
        <div class="logo">
          <span class="title">/ VYSOTSKY /</span>
          <span class="info">SEO-оптимизация и создание сайтов</span>
        </div>
        <div class="menu">
          <ul>
            <li>ГЛАВНАЯ</li>
            <li class="active">ЗАКАЗАТЬ SEO</li>
            <li>РАЗРАБОТКА САЙТОВ</li>
            <li>БЛОГ</li>
          </ul>
          <button class="btn call">ЗАКАЗАТЬ ЗВОНОК</button>
        </div>
      </nav>
      <div class="wrapper">
        <div class="wrapper__left">
          <div class="wrap">
            <div class="wrap__title">ВЫВЕДУ ВАШ БИЗНЕС НА НОВЫЙ УРОВЕНЬ</div>
            <span class="wrap__text">Сделаю эффективный маркетинг для вашего бизнеса. Настрою прозрачную аналитику, приведу клиентов,
          увеличу конверсию сайта.</span>
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
              <p class="diploma__link"><a href="#">СЕРТИФИКАТ МАРКЕТОЛОГА</a></p>
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
  name: 'Header'
}
</script>

<style lang="sass">
@import '../assets/sass/base'

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
        font-size: 14px
        font-weight: 700
        line-height: 18px

      .info
        font-size: 14px
        font-weight: 400
        line-height: 18px

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
          color: #E65765

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
    margin-top: 130px

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
      margin: 40px 0 25px

      .btn
        &.purple
          background: rgba(63, 51, 86, 1)

    &__info
      font-size: 11px
      line-height: 13px

</style>
