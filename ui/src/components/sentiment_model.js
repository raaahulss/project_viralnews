import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import SentimentMeter from './sentiment_meter.js'
import '../css/sentiment_model.css'

class SentimentModel extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if (this.props.value <= 0.20) {
      return (
        <div id="sentiment-details-main">
          <Card id="sentiment-card">
            <Card.Body id="sentiment-card-body">
              <Card.Title id="sentiment-card-title">{this.props.title}</Card.Title>
                <p id="class-value">Highly Liberal</p>
                <SentimentMeter id="sentiment-model" value={this.props.value} />
            </Card.Body>
          </Card>
        </div>
      );
    } else if (this.props.value > 0.20 && this.props.value <= 0.40 ){
    return (
      <div id="sentiment-details-main">
        <Card id="sentiment-card">
          <Card.Body id="sentiment-card-body">
            <Card.Title id="sentiment-card-title">{this.props.title}</Card.Title>
               <p id="class-value">Liberal</p>
              <SentimentMeter id="sentiment-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  } else if (this.props.value > 0.41 && this.props.value <= 0.60 ){
    return (
      <div id="sentiment-details-main">
        <Card id="sentiment-card">
          <Card.Body id="sentiment-card-body">
            <Card.Title id="sentiment-card-title">{this.props.title}</Card.Title>
               <p id="class-value">Neutral</p>
              <SentimentMeter id="sentiment-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  } else if (this.props.value > 0.61 && this.props.value <= 0.80 ){
    return (
      <div id="sentiment-details-main">
        <Card id="sentiment-card">
          <Card.Body id="sentiment-card-body">
            <Card.Title id="sentiment-card-title">{this.props.title}</Card.Title>
               <p id="class-value">Conservative</p>
              <SentimentMeter id="sentiment-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  } else {
    return (
      <div id="sentiment-details-main">
        <Card id="sentiment-card">
          <Card.Body id="sentiment-card-body">
            <Card.Title id="sentiment-card-title">{this.props.title}</Card.Title>
               <p id="class-value">Highly Conservative</p>
              <SentimentMeter id="sentiment-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
      );
    }
  }
}

export default SentimentModel;
