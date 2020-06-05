import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap';
import ViralnessModel from './viralness_model'
import SentimentModel from './sentiment_model'
import OpinionModel from './opinion_model'
import '../css/analysis.css'

class Analysis extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if (this.props.published === true) {
      return (
        <div id="analysis-details-main">
          <Container>
            <Row>
              <ViralnessHTML value={this.props.models.viralness}/>
              <div className="vline" />
              <SentimentHTML value={this.props.models.sentiment}/>
              <div className="vline" />
              <OpinionHTML value={this.props.models.public_opinion}/>
            </Row>
          </Container>
        </div>
      );
    } else {
      return (
        <div id="analysis-details-main">
          <Container>
            <Row>
              <SentimentHTML value={this.props.models.sentiment}/>
            </Row>
          </Container>
        </div>
      );
    }
    
  }
}

function ViralnessHTML(props) {
  return (
    <Col id="viralness-column">
      <ViralnessModel title="Will this Article go Viral?" value={props.value}/>
      <Row>
        <Col>
          <p style={{color:'#e27d60'}}>Low</p>
        </Col>
        <Col>
          <p style={{color:'#e27d60'}}>High</p>
        </Col>
      </Row>
    </Col>
  );
}

function SentimentHTML(props) {
  return (
    <Col id="sentiment-column">
      <SentimentModel title="Is this Article Biased?" value={props.value}/>
      <Row >
        <Col>
          <p style={{color:'#e27d60'}}>Left Wing</p>
        </Col>
        <Col>
          <p style={{color:'#e27d60'}}>Right Wing</p>
        </Col>
      </Row>
    </Col>
  );
}

function OpinionHTML(props) {
  return (
    <Col id="opinion-column">
      <OpinionModel title="How is the Public Reacting?" value={props.value}/>
      <Row>
        <Col>
          <p style={{color:'#e27d60'}}>Unhappy</p>
        </Col>
        <Col>
          <p style={{color:'#e27d60'}}>Happy</p>
        </Col>
      </Row>
    </Col>
  );
}

export default Analysis;
