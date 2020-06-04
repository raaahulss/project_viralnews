import React, { Component } from 'react'
import { Card, Button } from 'react-bootstrap';
import '../css/number_card.css'

class NumberCard extends Component {
  constructor(props){
    super(props);
  }
  render() {
    console.log(this.props.title)
    console.log(this.props.value)
    return (
      <div id="number-card-main">
        <Card>
		  <Card.Body id="number-card-body">
		    <Card.Title id="number-card-title">{this.props.title}</Card.Title>
		    <h2 id="number-text">{this.props.value}</h2>
		  </Card.Body>
		</Card>
      </div>
    );
  }
}

export default NumberCard;
