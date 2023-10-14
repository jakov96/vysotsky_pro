<template>
  <section class="section-2">
    <div class="site-analysis">
      <div class="side-width">
        <div class="site-analysis__wrap">
          <div class="site-analysis__description">
            <div class="site-analysis__title">Бесплатный экспресс-анализ сайта</div>
            <div class="site-analysis__info">
              <div class="site-analysis__info-item">
                <span class="site-analysis__icon"></span>
                <span class="site-analysis__subtitle">Информация о трафике конкурентов</span>
                <span class="site-analysis__text">Будет понятно сколько трафика получают конкуренты, из каких источников и
              насколько хорошо оптимизированы их сайты.</span>
              </div>
              <div class="site-analysis__info-item">
                <span class="site-analysis__icon"></span>
                <span class="site-analysis__subtitle">Полнота контента на страницах сайтах</span>
                <span class="site-analysis__text">Быстрый анализ текстов на страницах - сразу будет понятно где добавить
                  контент чтобы получать больше трафика.</span>
              </div>
              <div class="site-analysis__info-item">
                <span class="site-analysis__icon"></span>
                <span class="site-analysis__subtitle">Грубые технические ошибки</span>
                <span class="site-analysis__text">Исправление технических ошибок приведет к лучшей индексации сайта и
                  даст дополнительный трафик.</span>
              </div>
              <div class="site-analysis__info-item">
                <span class="site-analysis__icon"></span>
                <span class="site-analysis__subtitle">Ошибки юзабилити</span>
                <span class="site-analysis__text">Гарантировано увеличит конверсию и поведенческие метрики
                  пользователей, что положительно отразиться на позициях сайта.</span>
              </div>
            </div>
            <div class="site-analysis__result">Исправление ошибок после экспресс аудита гарантированно увеличит трафик
              до 50%
            </div>
          </div>
          <div class="site-analysis__preview">
            <img src="../assets/images/photo-3.png" alt="">
            <div class="site-analysis__preview-caption">Оставляйте заявку, я разберу ваш сайт в формате видео и отправлю
              его на почту
            </div>
          </div>
        </div>
        <div class="audit-form">
          <span class="audit-form__title">Заказать бесплатный аудит</span>
          <span class="audit-form__text">Нужна помощь - заполни заявку.</span>
          <div class="audit-form__data">
            <input type="text" placeholder="Имя">
            <input type="tel" placeholder="Телефон">
            <button class="btn">Заказать бесплатный аудит</button>
          </div>
          <div class="audit-form__agree">Нажимая на кнопку, вы соглашаетесь на обработку
            <a class="link" href="#" target="_blank">персональных данных</a>.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'SiteAnalysis'
}
</script>

<style lang="sass">
.site-analysis
  background: rgba(247, 245, 249, 1)

  .side-width
    position: relative

  &__wrap
    display: flex
    justify-content: space-between
    padding: 100px 0 170px

  &__description
    width: calc(100% - 600px)
    display: flex
    flex-direction: column

  &__info
    display: flex
    justify-content: space-between
    flex-wrap: wrap
    margin-top: 40px

  &__title
    font-size: 42px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

  &__info-item
    width: 45%
    display: flex
    flex-direction: column

    &:nth-of-type(n+3)
      margin-top: 30px

  &__icon
    display: block
    width: 25px
    height: 25px
    background: url("../assets/images/check-red.svg") no-repeat

  &__subtitle
    margin: 18px 0 12px
    font-size: 12px
    font-weight: 500

  &__text
    font-size: 13px
    line-height: 18px

  &__result
    margin-top: 50px
    font-size: 13px
    font-weight: 600
    line-height: 18px
    text-transform: uppercase

  &__preview
    background: #fff
    width: 460px
    display: flex
    flex-direction: column
    border-radius: 30px

  &__preview-caption
    margin: auto
    padding: 40px 0
    font-size: 17px
    font-weight: 500
    line-height: 22px
    text-align: center
    text-transform: uppercase

.audit-form
  position: absolute
  bottom: -190px
  z-index: 1
  width: 100%
  display: flex
  flex-direction: column
  justify-content: center
  margin: 0 auto
  padding: 45px 80px
  background: rgba(63, 51, 86, 1)
  border-radius: 30px
  box-sizing: border-box

  &__title
    margin-bottom: 20px
    color: #fff
    font-size: 37px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'
    text-align: center
    line-height: 42px

  &__text
    color: #fff
    font-size: 15px
    line-height: 20px
    text-align: center

  &__agree
    color: #fff
    font-size: 11px

  &__data
    display: flex
    justify-content: space-between
    margin: 45px 0 10px

    input
      width: 300px
      margin-right: 20px
      padding: 18px
      border: none
      border-radius: 10px
      font-size: 20px

      &::placeholder
        color: rgba(208, 201, 214, 1)

    .btn
      width: 360px
      padding: 20px 0

@media (max-width: 480px)
  .site-analysis
    padding: 20px 13px 40px

    &__wrap
      flex-direction: column
      padding: 0

    &__title
      font-size: 28px

    &__description
      width: 100%

    &__info
      flex-direction: column
      margin-top: 30px

    &__info-item
      width: 100%

      &:not(:first-child)
        margin-top: 20px

    &__subtitle
      font-weight: 700

    &__result
      margin-top: 30px
      font-size: 12px

    &__preview
      width: 100%
      margin-top: 30px

    &__preview-caption
      padding: 20px
      font-size: 15px

  .audit-form
    position: initial
    margin-top: 20px
    padding: 20px 15px 30px

    &__title
      font-size: 22px

    &__text
      font-size: 14px

    &__data
      flex-direction: column
      margin-top: 30px

      input
        width: auto
        padding: 16px
        font-size: 16px

        &:not(:last-child)
          margin: 10px 0 0

      .btn
        width: 100%
        order: 1
        margin-top: 20px
        font-size: 15px

    &__agree
      order: 0
</style>
