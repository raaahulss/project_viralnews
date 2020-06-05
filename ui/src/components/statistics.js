import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap';
import NumberCard from './number_card.js';
import DateCard from './date_card.js';
import '../css/statistics.css'

class Statistics extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div id="statistics-details-main">
        <Container>
          <Row>
            <Col>
              <NumberCard title="Retweets" value={this.props.metrics.retweets}/>
            </Col>
            <Col>
              <NumberCard title="Favourites" value={this.props.metrics.favourites}/>
            </Col>
            <Col>
              <NumberCard title="Responses" value={this.props.metrics.responses}/>
            </Col>
          </Row>
          <Row id="second-row">
            <Col>
              <NumberCard title="Trending?" value={this.props.metrics.trending}/>
            </Col>
            <Col>
              <DateCard id="date-card" title="First Tweet" value={this.props.metrics.first_tweet}/>
            </Col>
            <Col>
              <DateCard title="Last Tweet" value={this.props.metrics.last_tweet}/>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Statistics;