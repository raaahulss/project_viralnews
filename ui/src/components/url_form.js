import React, {Component} from 'react'
import SubmitButton from './submit_button.js';
import { Form } from 'react-bootstrap';
import { Container, Row, Col } from 'react-bootstrap';
import '../css/url_form.css'
import axios from 'axios';
import { Redirect } from "react-router-dom";

class UrlForm extends Component {
  constructor(props){
    super(props);
    this.state = {
      url: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange = (event) => {
    this.setState({
      url: event.target.value,
      data: {}
    })
  };

  handleSubmit = (event) => {
    event.preventDefault();
    let form_data = new FormData();
    form_data.append('url', this.state.url);

    let response = axios({
                  method: 'post',
                  url: 'http://localhost:5000/api/url',
                  data: form_data,
                  headers: {'Content-Type': 'text/html' }
                  })
                  .then(function (response) {
                      //handle success
                      console.log(response);
                  })
                  .catch(function (response) {
                      //handle error
                      console.log(response);
                  });
  };

  // render() {
  //   return (
  //     <div className="url-form">
  //       <Form onSubmit={this.handleSubmit}>
  //         <Container>
  //           <Row>
  //             <Col md={10}>
  //               <Form.Group controlId="formBasicUrl">
  //                 <Form.Control type="email" placeholder="Enter a political news url..." />
  //               </Form.Group>
  //             </Col>
  //             <Col md={2}>
  //               <SubmitButton />
  //             </Col>
  //           </Row>
  //         </Container>
  //       </Form>
  //     </div>
  //   );
  // }

  render() {
    let fireRedirect = false;
    return (
      <div className="url-form">
        <Form onSubmit={this.handleSubmit}>
          <Form.Group controlId="formBasicUrl">
            <Form.Control type="url" placeholder="Enter a political news url..." value={this.state.url} onChange={this.handleChange} required/>
          </Form.Group>
          <SubmitButton/>
        </Form>
        {fireRedirect && (
          <Redirect to={'/dashboard'}/>
        )}
      </div>
    );
  }
}

export default UrlForm;

