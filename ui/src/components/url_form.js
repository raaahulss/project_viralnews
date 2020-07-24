import React, {Component} from 'react'
import SubmitButton from './submit_button.js';
import { Form } from 'react-bootstrap';
import { Spinner } from 'react-bootstrap';
import { Redirect } from "react-router-dom";
import axios from 'axios';
import '../css/url_form.css'

class UrlForm extends Component {
  constructor(props){
    super(props);
    this.state = {
      url: "",
      redirect_success: false,
      redirect_failure: false,
      loader: false
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
    let input_url = this.state.url;
    this.setState({ loader: true });
    let form_data = new FormData();
    form_data.append('url', this.state.url);
    var self = this;
    let response = axios({
                    method: 'post',
                    url: 'http://3.128.42.45:5000/api/url',
                    params: {
                      url: input_url
                    },
                    headers: {
                      'Content-Type': 'text/html',
                      'Access-Control-Allow-Origin': '*'
                    }
                  })
                  .then((response) => {
                    //handle success
                    self.setState({ responseData: response.data });
                    self.setState({ loader: false });
                    self.setState({ redirect_success: true });
                  })
                  .catch((error) => {
                    //handle error
                    self.setState({ errorData: error.message });
                    self.setState({ loader: false });
                    self.setState({ redirect_failure: true });
                  });
  };

  render() {
    const { redirect_success } = this.state;
    const { loader } = this.state;
    const { redirect_failure } = this.state;
    if (redirect_success) {
      return <Redirect to={{
                pathname: '/dashboard',
                state: this.state.responseData
              }}
            />
    } else if (redirect_failure) {
      return <Redirect to={{
                pathname: '/error',
                state: this.state.errorData
              }}
            />
    } else if (loader) {
      return (
        <div>
          <br />
          <br />
          <br />
          <center>
            <Spinner animation="border" />
            <p>This may take about 5 seconds ...</p>
          </center>
        </div>
      )
    } else {
      return (
        <div className="url-form">
          <Form onSubmit={this.handleSubmit}>
            <Form.Group controlId="formBasicUrl">
              <Form.Control type="url" placeholder="Enter a political news url or a twitter url that contains a political news url..." value={this.state.url} onChange={this.handleChange} required/>
            </Form.Group>
            <SubmitButton/>
          </Form>
          <div id="url-note">Note: The list of supported politcal news sources are The New York Times, The Wall Street Journal, CNN, NBC News, Los Angeles Times, National Public Radio(NPR), Reuters, HuffPost and ABC News.</div>
        </div>
      );
    }
  }
}

export default UrlForm;
