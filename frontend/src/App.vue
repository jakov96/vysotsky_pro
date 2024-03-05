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
    <Reviews/>
    <Questions/>
    <SiteAnalysis/>
    <Blog/>
    <Footer/>
    <Modal
      v-show="isModalVisible"
      @close="closeModal"
    />
  </div>
</template>

<script>
import Header from './components/Header'
import Modal from './components/Modal'
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
import Questions from './components/Questions'
import Reviews from './components/Reviews'

export default {
  name: 'App',
  components: {
    About,
    Blog,
    Description,
    Footer,
    Header,
    Modal,
    Podcast,
    Prices,
    PricesDetail,
    ProblemExamples,
    RelatedPrices,
    Results,
    Reviews,
    Services,
    SiteAnalysis,
    Teaching,
    Questions,
    Who,
    WorkFormat
  },
  data () {
    return {
      isModalVisible: false
    }
  },
  methods: {
    closeModal () {
      this.isModalVisible = false
    },
    fetchData (data) {
      let url = `/landing/feedback/`
      fetch(url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: data

      })
        .then((response) => {
          if (response.ok) {
            return response.json()
          }
          throw new Error('Network response was not ok')
        })
        .then((json) => {
          if (json['success']) {
            this.closeModal()
          }
        })
        .catch((error) => {
          console.log(error)
        })
    }
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
