<template>
  <div>
    <Header/>
    <Description/>
    <Services/>
    <Prices/>
    <RelatedPrices/>
    <PricesDetail/>
    <WorkFormat/>
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

export default {
  name: 'App',
  components: {WorkFormat, PricesDetail, Prices, RelatedPrices, Description, Services, Header}
}
</script>

<style lang="sass">
@import url('https://fonts.googleapis.com/css2?family=Golos&display=swap')
@import url('https://fonts.googleapis.com/css2?family=Unbounded&display=swap')
</style>
