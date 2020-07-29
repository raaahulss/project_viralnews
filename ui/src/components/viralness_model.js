import React, { Component } from 'react'
import { Card } from 'react-bootstrap';
import ViralnessMeter from './viralness_meter.js'
import '../css/viralness_model.css'

class ViralnessModel extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if (this.props.value == 0.05) {
      return (
        <div id="viralness-details-main">
          <Card id="viralness-card">
            <Card.Body id="viralness-card-body">
              <Card.Title id="viralness-card-title">{this.props.title}</Card.Title>
                <p id="class-value"> 0-10 Retweets </p>
                <ViralnessMeter id="viralness-model" value={this.props.value} />
            </Card.Body>
          </Card>
        </div>
      );
    } else if (this.props.value == 0.20){
        return (
          <div id="viralness-details-main">
            <Card id="viralness-card">
              <Card.Body id="viralness-card-body">
                <Card.Title id="viralness-card-title">{this.props.title}</Card.Title>
                  <p id="class-value"> 11-100 Retweets </p>
                  <ViralnessMeter id="viralness-model" value={this.props.value} />
              </Card.Body>
            </Card>
          </div>
        );
  } else if (this.props.value == 0.45){
      return (
        <div id="viralness-details-main">
          <Card id="viralness-card">
            <Card.Body id="viralness-card-body">
              <Card.Title id="viralness-card-title">{this.props.title}</Card.Title>
                <p id="class-value"> 101-1000 Retweets </p>
                <ViralnessMeter id="viralness-model" value={this.props.value} />
            </Card.Body>
          </Card>
        </div>
      );

  } else {
    return (
      <div id="viralness-details-main">
        <Card id="viralness-card">
          <Card.Body id="viralness-card-body">
            <Card.Title id="viralness-card-title">{this.props.title}</Card.Title>
              <p id="class-value"> 1000+Retweets </p>
              <ViralnessMeter id="viralness-model" value={this.props.value} />
          </Card.Body>
        </Card>
      </div>
    );
   }
  }
}
export default ViralnessModel;
