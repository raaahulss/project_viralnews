import React, { Component } from 'react'
import {Jumbotron} from 'react-bootstrap';
import '../css/article_details.css'

class ArticleDetails extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div id="article-details-main">
        <Jumbotron >
          <h1>Article Title: {this.props.title}</h1>
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
      </div>
    );
  }
}

export default ArticleDetails;
