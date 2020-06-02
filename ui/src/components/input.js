import React, {Component} from 'react'
import InputTabs from './input_tabs.js';
import {Grid, Row, Col} from 'react-bootstrap';

class Input extends Component {
    constructor(props){
        super(props);
    }
    render() {
      return (
        <div bg="light" expand="lg">
          <h2>Learn more about the News you are reading!</h2>
          <InputTabs />
        </div>
      );
    }
}

export default Input;
