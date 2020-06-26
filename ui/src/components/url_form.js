import React, {Component} from 'react'
import SubmitButton from './submit_button.js';
import { Form } from 'react-bootstrap';
import { Container, Row, Col } from 'react-bootstrap';
import '../css/url_form.css'
import axios from 'axios';
import { Redirect } from "react-router-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


class UrlForm extends Component {
  constructor(props){
    super(props);
    this.state = {
      url: "",
      redirect: false,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange = (event) => {
    this.setState({
      url: event.target.value,
      data: {},
    })
  };

  handleSubmit = (event) => {
    event.preventDefault();
    let form_data = new FormData();
    form_data.append('url', this.state.url);
    //this.setState({ redirect: true });
    var self = this;
    let response = axios({
                  method: 'post',
                  url: 'http://localhost:5000/api/url',
                  data: form_data,
                  headers: {'Content-Type': 'text/html' }
                  })
                  .then((response) => {
                      //handle success
                      //console.log(response.data);
                      self.setState({responseData: response.data});
                      self.setState({ redirect: true });
                  })
                  .catch((response) => {
                      //handle error
                      //console.log(response);
                  });

          //console.log(response.data)
          //this.setState({response_data: response.data});

    //console.log(response.data);

  };


  render() {
    const { redirect } = this.state;
    if (redirect) {
      return <Redirect to={{
                pathname: '/dashboard',
                state: this.state.responseData
              }}
            />
    }
    return (
      <div className="url-form">
        <Form onSubmit={this.handleSubmit}>
          <Form.Group controlId="formBasicUrl">
            <Form.Control type="url" placeholder="Enter a political news url..." value={this.state.url} onChange={this.handleChange} required/>
          </Form.Group>
          <SubmitButton/>
        </Form>
      </div>
    );
  }
}

export default UrlForm;
