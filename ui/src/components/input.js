import React, { Component } from 'react'
import InputTabs from './input_tabs.js';
import '../css/input.css'

class Input extends Component {
    constructor(props){
        super(props);
    }
    render() {
      return (
        <div bg="light" expand="lg">
          <h2 className="index-page-title">Learn more about the News you are reading!</h2>
          <InputTabs />
        </div>
      );
    }
}

export default Input;
