import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import '../css/date_card.css'

class DateCard extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div id="date-card-main">
        <Card>
		      <Card.Body id="date-card-body">
		        <Card.Title id="date-card-title">{this.props.title}</Card.Title>
		         <h2 id="date-text">{this.props.value}</h2>
		      </Card.Body>
		    </Card>
      </div>
    );
  }
}

export default DateCard;
