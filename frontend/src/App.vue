<template>
  <div>
    <Header/>
    <Services/>
  </div>
</template>

<script>
import Header from './components/Header'
import Services from './components/Services'

export default {
  name: 'App',
  components: {Services, Header}
}
</script>

<style lang="sass">
@import url('https://fonts.googleapis.com/css2?family=Golos&display=swap')
@import url('https://fonts.googleapis.com/css2?family=Unbounded&display=swap')
</style>
