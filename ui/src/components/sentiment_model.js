import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import SentimentMeter from './sentiment_meter.js'
import '../css/sentiment_model.css'

class SentimentModel extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div id="sentiment-details-main">
        <Card id="sentiment-card">
          <Card.Body id="sentiment-card-body">
            <Card.Title id="sentiment-card-title">{this.props.title}</Card.Title>
              <SentimentMeter id="sentiment-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  }
}

export default SentimentModel;
