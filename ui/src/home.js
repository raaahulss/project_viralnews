import React, { Component } from 'react'
import Input from './components/input.js';

class Home extends Component {
  componentDidMount(){
    document.title = "isViral - Home"
  }
  render() {
    return (
      <div style={{display: 'flex',
                  justifyContent:'center',
                  alignItems:'center'}}>
                  <Input />
      </div>
    );
  }
}

export default Home;
