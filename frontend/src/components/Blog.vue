<template>
  <section class="section-5">
<!--    <div class="side-width blog-wrap">-->
<!--      <div class="title-section">Последние статьи из блога</div>-->
<!--      <VueSlickCarousel class="blog" v-bind="settings">-->
<!--        <div class="blog__item">-->
<!--          <img src="../assets/images/blog-photo.png" alt="">-->
<!--          <div class="blog__description">-->
<!--            <span class="blog__date">13 июня 2021</span>-->
<!--            <span class="blog__title">Что такое Title и зачем нужен для SEO?</span>-->
<!--          </div>-->
<!--          <a href="#">-->
<!--            <button class="btn">ЧИТАТЬ</button>-->
<!--          </a>-->
<!--        </div>-->
<!--        <div class="blog__item">-->
<!--          <img src="../assets/images/blog-photo.png" alt="">-->
<!--          <div class="blog__description">-->
<!--            <span class="blog__date">13 июня 2021</span>-->
<!--            <span class="blog__title">Что такое Title и зачем нужен для SEO?</span>-->
<!--          </div>-->
<!--          <a href="#">-->
<!--            <button class="btn">ЧИТАТЬ</button>-->
<!--          </a>-->
<!--        </div>-->
<!--        <div class="blog__item">-->
<!--          <img src="../assets/images/blog-photo.png" alt="">-->
<!--          <div class="blog__description">-->
<!--            <span class="blog__date">13 июня 2021</span>-->
<!--            <span class="blog__title">Что такое Title и зачем нужен для SEO?</span>-->
<!--          </div>-->
<!--          <a href="#">-->
<!--            <button class="btn">ЧИТАТЬ</button>-->
<!--          </a>-->
<!--        </div>-->
<!--        <div class="blog__item">-->
<!--          <img src="../assets/images/blog-photo.png" alt="">-->
<!--          <div class="blog__description">-->
<!--            <span class="blog__date">13 июня 2021</span>-->
<!--            <span class="blog__title">Что такое Title и зачем нужен для SEO?</span>-->
<!--          </div>-->
<!--          <a href="#">-->
<!--            <button class="btn">ЧИТАТЬ</button>-->
<!--          </a>-->
<!--        </div>-->
<!--      </VueSlickCarousel>-->
<!--    </div>-->
  </section>
</template>

<script>
import VueSlickCarousel from 'vue-slick-carousel'

export default {
  name: 'Blog',
  components: { VueSlickCarousel },
  data () {
    return {
      'settings': {
        'arrows': true,
        'dots': false,
        'infinite': true,
        'slidesToShow': 3,
        'slidesToScroll': 1,
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
.side-width
  &.blog-wrap
    position: relative

.blog
  position: initial !important

  &__item
    display: flex
    flex-direction: column
    padding: 40px
    border-radius: 30px
    box-shadow: rgba(0, 0, 0, 0.07) 0 1px 4px

    img
      width: 100%
      object-fit: cover

  .slick-slide
    width: 260px !important
    padding: 5px 20px
    margin: 0 40px
    box-sizing: border-box

  .slick-list
    margin: 0 -20px

  .slick-arrow
    width: 30px
    height: 24px
    top: 21px !important
    left: initial !important

    &:before
      content: none

    &.slick-prev
      right: 70px !important
      background: url('../assets/images/prev-arrow.svg') no-repeat center center

    &.slick-next
      right: 0 !important
      background: url('../assets/images/next-arrow.svg') no-repeat center center

  &__description
    display: flex
    flex-direction: column
    margin-top: 20px

  &__date
    color: rgba(63, 51, 86, 1)
    font-size: 12px
    line-height: 16px

  &__title
    margin: 10px 0 25px
    font-size: 18px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    line-height: 24px

  .btn
    width: 100%

    &:hover
      background: rgba(255, 214, 0, 1)
      color: rgba(63, 51, 86, 1)

@media (max-width: 480px)
  .side-width
    &.blog-wrap
      padding: 0 13px
      box-sizing: border-box

  .blog
    &__item
      width: 25%
      padding: 20px

    .slick-list
      width: 100%
      margin: 0

    .slick-slide
      margin: 0 20px
      padding: 5px 10px
      box-sizing: border-box

    .slick-arrow
      top: calc(100% + 40px) !important

      &.slick-prev
        left: calc(50% - 30px) !important

      &.slick-next
        left: calc(50% + 30px) !important
</style>
