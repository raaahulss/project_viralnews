import React, { Component } from 'react'
import CarouselMl from './components/carousel.js';

class Ml extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div style={{display: 'flex',
                  justifyContent:'center',
                  alignItems:'center',
                  height: '75vh'}}>
                  <CarouselMl />
      </div>
    );
  }
}

export default Ml;
