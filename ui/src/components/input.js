import React, { Component } from 'react'
import InputTabs from './input_tabs.js';
import '../css/input.css'

class Input extends Component {
    constructor(props){
        super(props);
    }
    render() {
      return (
        <div className="input">
          <h2 className="index-page-title">Learn more about the News <br /> you are reading!</h2>
          <InputTabs />
        </div>
      );
    }
}

export default Input;
