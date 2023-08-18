<template>
  <div>
    <Header/>
    <Description/>
    <Services/>
  </div>
</template>

<script>
import Header from './components/Header'
import Services from './components/Services'
import Description from './components/Description'

export default {
  name: 'App',
  components: {Description, Services, Header}
}
</script>

<style lang="sass">
@import url('https://fonts.googleapis.com/css2?family=Golos&display=swap')
@import url('https://fonts.googleapis.com/css2?family=Unbounded&display=swap')
</style>
