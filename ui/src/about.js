import React, { Component } from 'react'
import AboutCards from './components/about_cards.js'

class About extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <AboutCards />
    );
  }
}

export default About;
