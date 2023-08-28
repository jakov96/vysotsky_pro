<template>
  <section class="section-3">
    <div class="side-width">
      <div class="questions-wrap">
        <div class="questions">
          <div class="title-section">Вопросы и ответы</div>
          <div class="questions__content">
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">Какие гарантии?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">Какой срок продвижения?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">Почему именно я?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">Почему мало кейсов/отзывов?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">Что делать после продвижения?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">В каких регионах России работаю?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
            <div class="questions__item">
              <div class="questions__question" @click="toggleBtn($event)">Как оценить результат моей работы?</div>
              <div class="questions__answer">Ответ на вопрос</div>
            </div>
          </div>
        </div>
        <div class="question-form">
          <div class="question-form__title">Не нашли ответ на свой вопрос?</div>
          <span class="question-form__text">Оставьте заявку, я перезвоню и отвечу  на все Ваши вопросы</span>
          <div class="question-form__data">
            <input type="text" placeholder="Имя">
            <input type="tel" placeholder="+7 (999) 999-99-99">
          </div>
          <div class="question-form__agree">Нажимая на кнопку, вы соглашаетесь на обработку
            <a href="#" class="link">персональных данных</a>.
          </div>
          <button class="btn">Заказать звонок</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Questions',
  methods: {
    toggleBtn: function (event) {
      let button = event.target.parentElement
      button.classList.toggle('active')
    }
  }
}
</script>

<style lang="sass">
.questions-wrap
  display: flex
  justify-content: space-between

.questions
  width: 47%
  display: flex
  flex-direction: column

  &__item
    display: flex
    flex-direction: column
    padding: 22px 0 26px
    border-top: 1px solid rgba(247, 245, 249, 1)
    border-bottom: 1px solid rgba(247, 245, 249, 1)

    &.active
      .questions__answer
        display: block

  &__question
    width: 100%
    display: flex
    justify-content: space-between
    align-items: center
    cursor: pointer
    font-size: 15px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

    &:after
      content: ''
      display: block
      width: 24px
      height: 24px
      background: url('../assets/images/plus.png') no-repeat

  &__answer
    display: none
    margin-top: 20px

.question-form
  width: 47%
  height: max-content
  display: flex
  flex-direction: column
  padding: 50px 80px
  background: rgba(247, 245, 249, 1)
  border-radius: 30px
  box-sizing: border-box

  &__title
    color: rgba(26, 5, 29, 1)
    font-size: 35px
    font-weight: 700
    font-family: 'Unbounded', 'sans-serif'

  &__text
    margin-top: 40px
    font-size: 15px
    line-height: 20px
    text-align: center

  &__data
    display: flex
    flex-direction: column
    margin: 30px 0 20px
    text-align: center

    input
      height: 60px
      padding: 18px
      font-size: 20px
      border: none
      border-radius: 10px
      box-sizing: border-box

      &::placeholder
        color: rgba(208, 201, 214, 1)

      &:last-child
        margin-top: 24px

  &__agree
    font-size: 11px

  .btn
    width: 300px
    margin: 30px auto 0
</style>
