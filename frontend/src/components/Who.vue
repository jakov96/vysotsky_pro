<template>
  <section class="section-4">
    <div class="side-width">
      <div class="title-section">Кто я такой?</div>
      <div class="who">
        <div class="who__photo">
          <img src="../assets/images/photo-2.png" alt="">
        </div>
        <div class="who__info">
          <div class="who__item">Мне 30 лет. Живу в Москве</div>
          <div class="who__item">По образованию “Разработчик защищенного ПО” - хорошо разбираюсь в коде и умею работать
            почти с любой CMS, а так же умею разговаривать с программистами на одном языке и четко формулировать ТЗ
          </div>
          <div class="who__item">Преподаю SEO в университете GeekBrains Mail.ru</div>
          <div class="who__item">Продвигал крупные сайты, такие как goods.ru, rabota.ru, sberauto.com</div>
          <div class="who__item">Учился маркетингу в Яндексе</div>
          <div class="who__item">Все проекты веду сам. Изредка прибегаю к силам помощников</div>
          <div class="who__item">Ценю честность и открытость. Сам стараюсь быть честным и если пониманию,
            что клиенту не подходит SEO и нужно что-то иное, говорю об этом сразу.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Who'
}
</script>

<style lang="sass">
.who
  display: flex
  align-items: center
  margin-top: 40px

  &__photo
    position: relative
    width: 460px
    height: 420px
    background: url('../assets/images/bg-section-4.png') no-repeat bottom
    border: 1px solid rgba(208, 201, 214, 1)
    border-radius: 30px 0 0 30px
    border-right: none

    img
      position: absolute
      right: 0
      bottom: 0

  &__info
    width: calc(100% - 460px)
    height: 760px
    display: flex
    flex-direction: column
    padding-bottom: 30px
    border: 1px solid rgba(208, 201, 214, 1)
    border-radius: 30px

  &__item
    padding: 30px 45px
    border-bottom: 1px solid rgba(208, 201, 214, 1)
    font-size: 20px
    line-height: 26px

    &:last-child
      border-bottom: none

@media (max-width: 480px)
  .who
    flex-direction: column
    margin-top: 60px

    &__photo
      width: 100%
      height: 270px
      border: 1px solid rgba(208, 201, 214, 1)
      border-radius: 30px

      img
        height: 300px
        left: 25%

    &__info
      width: 100%
      height: auto
      margin: 20px 0
      padding: 0

    &__item
      padding: 20px 30px
      font-size: 14px
      line-height: 20px

</style>
