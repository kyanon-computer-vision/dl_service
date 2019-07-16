import React, { Component } from 'react';
// --- Post bootstrap -----
import ProductCategories from './components/landing/modules/views/ProductCategories';
import ProductSmokingHero from './components/landing/modules/views/ProductSmokingHero';
import AppFooter from './components/landing/modules/views/AppFooter';
import ProductHero from './components/landing/modules/views/ProductHero';
import ProductValues from './components/landing/modules/views/ProductValues';
import ProductHowItWorks from './components/landing/modules/views/ProductHowItWorks';
import ProductCTA from './components/landing/modules/views/ProductCTA';
import AppAppBar from './components/landing/modules/views/AppAppBar';


export default class App extends Component {
  static displayName = App.name;

  render () {
    return (
      <React.Fragment>
        <AppAppBar />
        <ProductHero />
        <ProductValues />
        <ProductCategories />
        <ProductHowItWorks />
        <ProductCTA />
        <ProductSmokingHero />
        <AppFooter />
      </React.Fragment>
    );
  }
}
