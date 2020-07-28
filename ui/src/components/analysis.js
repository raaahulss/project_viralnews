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
    if (this.props.input_type === "Twitter") {
      return (
        <div id="analysis-details-main">
          <center>
            <Container>
              <Row>
                <ViralnessHTML value={this.props.models.viralness}/>
                <div className="vline" />
                <SentimentHTML value={this.props.models.sentiment}/>
                <div className="vline" />
                <OpinionHTML value={this.props.models.public_opinion}/>
              </Row>
            </Container>
          </center>
        </div>
      );
    } else if (this.props.input_type === "NonTwitter") {
      return (
        <div id="analysis-details-main">
          <center>
            <Container>
              <Row>
                <ViralnessHTML value={this.props.models.viralness}/>
                <div className="vline" />
                <SentimentHTML value={this.props.models.sentiment}/>
              </Row>
            </Container>
          </center>
        </div>
      );
    } else if (this.props.input_type === "UnPub") {
      return (
        <div id="analysis-details-main">
          <center>
            <Container>
              <Row>
                <ViralnessHTML value={this.props.models.viralness}/>
                <div className="vline" />
                <SentimentHTML value={this.props.models.sentiment}/>
              </Row>
            </Container>
          </center>
        </div>
      );
    }
  }
}

function ViralnessHTML(props) {
  return (
    <Col id="viralness-column">
      <ViralnessModel title="Article Viralness" value={props.value}/>
      <Row style={{width: 330}}>
        <Col>
          <p style={{color:'#ffffff'}}>0 Retweets</p>
        </Col>
        <Col>
          <p style={{color:'#ffffff'}}>1000+ Retweets</p>
        </Col>
      </Row>
      <a href='/ml' style={{color:'#ffffff',fontWeight: "bold"}}>Uses a base-10 log scale</a>
    </Col>
  );
}

function SentimentHTML(props) {
  return (
    <Col id="sentiment-column">
      <SentimentModel title="Political Bias" value={props.value}/>
      <Row style={{width: 330}}>
        <Col>
          <p style={{color:'#ffffff'}}>Liberal</p>
        </Col>
        <Col>
          <p style={{color:'#ffffff'}}>Conservative</p>
        </Col>
      </Row>
      <a href='/ml' style={{color:'#ffffff',fontWeight: "bold"}}>0% is Liberal - 100% is Conservative </a>
    </Col>
  );
}

function OpinionHTML(props) {
  return (
    <Col id="opinion-column">
      <OpinionModel title="Public Reaction" value={props.value}/>
      <Row>
        <Col>
          <p style={{color:'#ffffff'}}>Disagree</p>
        </Col>
        <Col>
          <p style={{color:'#ffffff'}}>Agree</p>
        </Col>
      </Row>
    <a href='/ml' style={{color:'#ffffff',fontWeight: "bold"}}>Percentage of users that agree</a>
    </Col>
  );
}

export default Analysis;
