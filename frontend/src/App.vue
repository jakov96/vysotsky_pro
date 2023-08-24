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
    <ProblemExamples/>
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
import ProblemExamples from './components/ProblemExamples'

export default {
  name: 'App',
  components: {
    About,
    Description,
    Footer,
    Header,
    Prices,
    PricesDetail,
    ProblemExamples,
    RelatedPrices,
    Results,
    Services,
    WorkFormat
  }
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
