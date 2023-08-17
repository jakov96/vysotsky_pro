<template>
  <header>
    <div class="side-width header">
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
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style lang="sass">
  .btn
    color: #FBFBFB
    cursor: pointer
    background: #E65765
    border: none
    border-radius: 20px
    font-weight: 500
    font-family: Golos, sans-serif

  .side-width
    &.header
      display: flex
      justify-content: space-between
      align-items: center
      padding: 25px
      background: red
      border-radius: 90px

      .logo
        .title
          margin-right: 30px
          font-size: 14px
          font-weight: 700
          line-height: 18px

        .info
          font-size: 13px
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
      font-weight: 500
      font-family: 'Unbounded', 'sans-serif'

      li:not(:last-child)
        margin: 0 25px 0 0

      li.active
        color: #E65765

  .call
    margin-left: 40px
    padding: 10px 20px
</style>
