import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import OpinionMeter from './opinion_meter.js'
import '../css/opinion_model.css'

class OpinionModel extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div id="opinion-details-main">
        <Card id="opinion-card">
          <Card.Body id="opinion-card-body">
            <Card.Title id="opinion-card-title">{this.props.title}</Card.Title>
              <OpinionMeter id="opinion-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  }
}

export default OpinionModel;
