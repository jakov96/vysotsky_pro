<template>
  <section class="section-3">
    <div class="side-width">
      <div class="bounded">
        <div class="title-section">Обо мне в цифрах</div>
        <div class="about">
          <div class="about__item">
            <img src="../assets/images/10_item.png" alt="10">
            <span class="about__info">тысяч запросов продвинуто в ТОП10</span>
          </div>
          <div class="about__item">
            <img src="../assets/images/2_item.png" alt="2">
            <span class="about__info">трафик на проекты более 2 миллионов</span>
          </div>
          <div class="about__item">
            <img src="../assets/images/14_item.png" alt="14">
            <span class="about__info">проектов с нуля до окупаемости</span>
          </div>
          <div class="about__item">
            <img src="../assets/images/10_item.png" alt="10">
            <span class="about__info">10 лет в маркетинге и разработке</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'About'
}
</script>

<style lang="sass">
.about
  display: flex
  justify-content: space-between

  &__item
    width: 18%
    display: flex
    flex-direction: column

  &__info
    margin-top: 16px
    font-size: 15px
    font-weight: 500
    line-height: 22px
    text-transform: uppercase

@media (max-width: 480px)
  .about
    flex-direction: column

    &__item
      width: 100%
      align-items: center
      padding: 26px 0
      border-top: 1px solid rgba(208, 201, 214, 1)

      &:last-child
        border-bottom: 1px solid rgba(208, 201, 214, 1)

      img
        width: 190px

    &__info
      font-weight: 700
</style>
