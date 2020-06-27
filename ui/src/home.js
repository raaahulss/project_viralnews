import React, { Component } from 'react'
import Input from './components/input.js';
import { Grid, Row, Col, Container } from 'react-bootstrap';

class Home extends Component {
  constructor(props){
    super(props);
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
