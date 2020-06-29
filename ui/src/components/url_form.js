import React, {Component} from 'react'
import SubmitButton from './submit_button.js';
import { Form } from 'react-bootstrap';
import { Redirect } from "react-router-dom";
import axios from 'axios';
import '../css/url_form.css'

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
    var self = this;
    let response = axios({
                  method: 'post',
                  url: 'http://localhost:5000/api/url',
                  params: {
                    url: this.state.url
                  },
                  headers: {'Content-Type': 'text/html'}
                  })
                  .then((response) => {
                      //handle success
                      self.setState({responseData: response.data});
                      self.setState({ redirect: true });
                  })
                  .catch((response) => {
                      //handle error
                  });
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
