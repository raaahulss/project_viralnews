import React, { Component } from 'react'
import Jumbo from './components/jumbo.js';

class Api extends Component {
  componentDidMount(){
    document.title = "isViral - API"
  }
  render() {
    return (
      <Jumbo />
    );
  }
}

export default Api;
