<template>
  <div>
    <Header/>
    <Description/>
    <Services/>
    <Prices/>
    <RelatedPrices/>
    <PricesDetail/>
    <WorkFormat/>
    <Results/>
    <About/>
    <Footer/>
  </div>
</template>

<script>
import Header from './components/Header'
import Services from './components/Services'
import Description from './components/Description'
import RelatedPrices from './components/RelatedPrices'
import Prices from './components/Prices'
import PricesDetail from './components/PricesDetail'
import WorkFormat from './components/WorkFormat'
import About from './components/About'
import Footer from './components/Footer'
import Results from './components/Results'

export default {
  name: 'App',
  components: {Results, Footer, About, WorkFormat, PricesDetail, Prices, RelatedPrices, Description, Services, Header}
}
</script>

<style lang="sass">
@font-face
  font-family: 'Golos'
  src: local('Golos'), url("assets/fonts/Golos/Golos_Text.ttf") format("truetype")

@font-face
  font-family: 'Unbounded'
  src: local('Unbounded'), url("assets/fonts/Unbounded/Unbounded.ttf") format("truetype")
</style>
