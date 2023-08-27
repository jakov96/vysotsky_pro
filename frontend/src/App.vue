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
    <Who/>
    <About/>
    <Teaching/>
    <Podcast/>
    <SiteAnalysis/>
    <Blog/>
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
import Who from './components/Who'
import Podcast from './components/Podcast'
import Teaching from './components/Teaching'
import Blog from './components/Blog'
import SiteAnalysis from './components/SiteAnalysis'

export default {
  name: 'App',
  components: {
    About,
    Blog,
    Description,
    Footer,
    Header,
    Podcast,
    Prices,
    PricesDetail,
    ProblemExamples,
    RelatedPrices,
    Results,
    Services,
    SiteAnalysis,
    Teaching,
    Who,
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
