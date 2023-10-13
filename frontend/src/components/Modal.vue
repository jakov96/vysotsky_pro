<template>
  <div class="modal-backdrop">
    <div class="modal">
      <span @click="close" class="modal__close-icon"></span>
      <section class="modal__header">
        <div class="modal__title">Заявка на обратный звонок</div>
        <span class="modal__info">Заполни и я перезвоню через 10 минут...</span>
      </section>
      <section class="modal-body">
        <div class="modal__inputs">
          <input v-model="name" class="name" placeholder="Имя">
          <VuePhoneNumberInput @update="onUpdate" class="phone" :translations="translations" v-model="phoneNumber"/>
        </div>
        <span class="modal__agreement">
          Нажимая на кнопку, вы соглашаетесь на обработку <a target="_blank" class="link" href="#">персональных данных</a>.
        </span>
        <button @click="sendData" class="modal__feedback btn">Заказать звонок</button>
      </section>
      <section class="modal__footer">
        Сомневаешься, заполнять или нет?<br>
        Заполни, первая консультация БЕСПЛАТНА<br>
        и ты ничего не теряешь ;)
      </section>
    </div>
  </div>
</template>

<script>
import VuePhoneNumberInput from 'vue-phone-number-input'
import 'vue-phone-number-input/dist/vue-phone-number-input.css'

export default {
  name: 'Modal',
  components: {
    VuePhoneNumberInput
  },
  data () {
    return {
      name: null,
      phoneNumber: null,
      isValidPhone: false,
      translations: {
        phoneNumberLabel: 'Номер телефона',
        example: 'Пример'
      }
    }
  },
  methods: {
    clear () {
      this.name = this.phoneNumber = null
    },
    close () {
      this.$emit('close')
      this.clear()
    },
    onUpdate (payload) {
      this.isValidPhone = payload.isValid
    },
    sendData () {
      if (this.name && this.isValidPhone) {
        console.log('success')
        this.close()
      } else {
        console.log('error')
      }
    }
  }
}
</script>

<style lang="sass">
.modal-backdrop
  position: fixed
  top: 0
  bottom: 0
  left: 0
  right: 0
  background-color: rgba(0, 0, 0, 0.3)
  display: flex
  justify-content: center
  align-items: center

  .modal
    position: relative
    width: 450px
    height: auto
    padding: 50px 65px
    background: rgba(247, 245, 249, 1)
    border-radius: 25px

    &__close-icon
      position: absolute
      top: 15px
      right: 15px
      content: ''
      background: url("../assets/images/close.svg") no-repeat
      display: block
      width: 24px
      height: 24px
      cursor: pointer

      &:hover
        transform: scale(1.2)

    &__header
      text-align: center

    &__title
      margin-bottom: 20px
      color: #000
      font-size: 35px
      font-family: 'Unbounded', 'sans-serif'
      font-weight: 700
      line-height: 40px
      text-align: center

    &__info
      color: #000
      font-size: 15px
      line-height: 20px

    &__inputs
      display: flex
      flex-direction: column
      margin: 54px 0 20px

      input
        padding: 18px
        color: #000
        background: #fff
        border: none
        font-size: 20px
        outline: none

        &.name
          margin-bottom: 20px
          border-radius: 10px

          &:focus
            border: 2px solid dodgerblue

        &::placeholder
          color: rgba(208, 201, 214, 1)

    &__agreement
      font-size: 11px

    &__feedback
      width: 100%
      margin-top: 30px

    &__footer
      margin-top: 40px
      color: #000
      font-size: 15px
      line-height: 20px
      text-align: center

@media (max-width: 480px)
  .modal-backdrop
    .modal
      width: 80%
      padding: 25px 20px 30px

      &__title
        margin-bottom: 10px
        font-size: 20px
        line-height: 26px

      &__info
        font-size: 14px

      &__inputs
        margin: 20px 0 10px

        input
          font-size: 16px

          &.name
            margin-bottom: 10px

      &__agreement
        font-size: 11px
        line-height: 12px

      &__footer
        margin-top: 16px
        font-size: 14px
</style>
