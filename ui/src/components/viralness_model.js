import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import ViralnessMeter from './viralness_meter.js'
import '../css/viralness_model.css'

class ViralnessModel extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div id="viralness-details-main">
        <Card id="viralness-card">
          <Card.Body id="viralness-card-body">
            <Card.Title id="viralness-card-title">{this.props.title}</Card.Title>
              <ViralnessMeter id="viralness-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
  }
}

export default ViralnessModel;
