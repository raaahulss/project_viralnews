import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import OpinionMeter from './opinion_meter.js'
import '../css/opinion_model.css'

class OpinionModel extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if (this.props.value <= 0.35) {
      return (
        <div id="opinion-details-main">
          <Card id="opinion-card">
            <Card.Body id="opinion-card-body">
              <Card.Title id="opinion-card-title">{this.props.title}</Card.Title>
                <p id="class-value">Disagree</p>
                <OpinionMeter id="opinion-model" value={this.props.value} />
            </Card.Body>
          </Card>
        </div>
      );
    } else if (this.props.value > 0.36 && this.props.value <= 0.65 ){
    return (
      <div id="opinion-details-main">
        <Card id="opinion-card">
          <Card.Body id="opinion-card-body">
            <Card.Title id="opinion-card-title">{this.props.title}</Card.Title>
              <p id="class-value">Neutral</p>
              <OpinionMeter id="opinion-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  } else{
    return (
      <div id="opinion-details-main">
        <Card id="opinion-card">
          <Card.Body id="opinion-card-body">
            <Card.Title id="opinion-card-title">{this.props.title}</Card.Title>
              <p id="class-value">Agree</p>
              <OpinionMeter id="opinion-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
      );
  }
 }
}

export default OpinionModel;
