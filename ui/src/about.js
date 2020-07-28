import React, { Component } from 'react'
import AboutCards from './components/about_cards.js'

class About extends Component {
  componentDidMount(){
    document.title = "isViral - About"
  }
  render() {
    return (
      <AboutCards />
    );
  }
}

export default About;
