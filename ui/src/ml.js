import React, { Component } from 'react'
import CarouselMl from './components/carousel.js';

class Ml extends Component {
  componentDidMount(){
    document.title = "isViral - ML"
  }
  render() {
    return (
      <div style={{display: 'flex',
                  justifyContent:'center',
                  alignItems:'center'}}>
                  <CarouselMl />
      </div>
    );
  }
}

export default Ml;
