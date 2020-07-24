import React, { Component } from 'react'
import {Jumbotron, Accordion, Card} from 'react-bootstrap';
import ArticleEntry from './article_entry'
import '../css/article_details.css'

class ArticleDetails extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return(
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
                  <div>
                    <ArticleEntry field="Source" value={this.props.source}/>
                    <ArticleEntry field="URL" value={this.props.url}/>
                    <ArticleEntry field="Author" value={this.props.author}/>
                    <ArticleEntry field="Date Published" value={this.props.date}/>
                    <ArticleEntry field="Content" value={this.props.content}/>
                  </div>
                </Jumbotron>
              </Card.Body>
            </Accordion.Collapse>
          </Card>
        </Accordion>
      </div>
    )
  }
}

export default ArticleDetails;
