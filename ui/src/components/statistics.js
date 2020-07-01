import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap';
import NumberCard from './number_card.js';
import '../css/statistics.css'
import '../css/date_card.css'

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
              <center>
                <NumberCard title="Retweets" value={this.props.metrics.retweets}/>
              </center>
            </Col>
            <Col>
              <center>
                <NumberCard title="Favorites" value={this.props.metrics.favourites}/>
              </center>
            </Col>
            <Col>
              <center>
                <NumberCard title="Responses" value={this.props.metrics.responses}/>
              </center>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default Statistics;
