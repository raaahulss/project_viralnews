import React, { Component } from 'react'
import {Jumbotron, Accordion, Card} from 'react-bootstrap';
import '../css/article_details.css'

class ArticleDetails extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if (this.props.type === "UnPub") {
      return (
        <div id="article-details-main">
          <Accordion>
            <Card id="article-details-card">
              <Card.Header id="article-details-card-header">
                <Accordion.Toggle as={Card.header} eventKey="0" id="article-details-button">
                  <h2><i> {this.props.title} </i></h2>
                  <p>Click for more article details</p>
                </Accordion.Toggle>
              </Card.Header>
              <Accordion.Collapse eventKey="0">
                <Card.Body>
                  <Jumbotron >
                    <p>
                      Content: {this.props.content}
                    </p>
                  </Jumbotron>
                </Card.Body>
              </Accordion.Collapse>
            </Card>
          </Accordion>
        </div>
      );
    } else {
      return (
        <div id="article-details-main">
          <Accordion>
            <Card id="article-details-card">
              <Card.Header id="article-details-card-header">
                <Accordion.Toggle as={Card.header} eventKey="0" id="article-details-button">
                  <h2><i> {this.props.title} </i></h2>
                  <p>Click for more article details</p>
                </Accordion.Toggle>
              </Card.Header>
              <Accordion.Collapse eventKey="0">
                <Card.Body>
                  <Jumbotron >
                    <p>
                      Source: {this.props.source}
                      <br />
                      URL: {this.props.url}
                      <br />
                      Author: {this.props.author}
                      <br />
                      Date Published: {this.props.date}
                      <br />
                      Content: {this.props.content}
                    </p>
                  </Jumbotron>
                </Card.Body>
              </Accordion.Collapse>
            </Card>
          </Accordion>
        </div>
      );
    }
  }
}

export default ArticleDetails;
