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
                  alignItems:'center',
                  height: '75vh'}}>
                  <Input />
      </div>
    );
  }
}

export default Home;
