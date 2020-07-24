import React, {Component} from 'react'
import { Jumbotron } from 'react-bootstrap';
import '../css/jumbo.css'

class Jumbo extends Component {
  render() {
    return (
      <div className = "jumbo_pad">
      <h2 className="api_title">API for Published Articles</h2>
      <Jumbotron >
        <h1>POST /url</h1>
        <p>
          Request body parameters:
        </p>
        <p>
          {'{'}
        </p>
        <p>
          “url”: “https://twitter.com/nytimes/status/1263205819413417990”
        </p>
        <p>
          {'}'}
        </p>
      </Jumbotron>
      <h2 className="api_title">API for Unpublished Articles</h2>
      <Jumbotron>
        <h1>POST /article</h1>
        <p>
          Request body parameters:
        </p>
        <p>
          {'{'}
        </p>
        <p>
          “title”: “Supreme Court Blocks Release of Full Mueller Report for Now”
        </p>
        <p>
          “body”: “WASHINGTON — The Supreme Court on Wednesday temporarily blocked the release of parts of the
          report prepared by Robert S. Mueller III, the special counsel who investigated Russian interference in the 2016
          election.
        </p>
        <p>
          {'}'}
        </p>
      </Jumbotron>
    </div>
    );
  }
}

export default Jumbo
