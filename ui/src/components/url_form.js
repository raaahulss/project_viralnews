import React, {Component} from 'react'
import SubmitButton from './submit_button.js';
import { Form } from 'react-bootstrap';
import { Container, Row, Col } from 'react-bootstrap';
import '../css/url_form.css'

class UrlForm extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div className="url-form">
        <Form>
          <Container>
            <Row>
              <Col md={10}>
                <Form.Group controlId="formBasicUrl">
                  <Form.Control type="email" placeholder="Enter a political news url..." />
                </Form.Group>
              </Col>
              <Col md={2}>
                <SubmitButton />
              </Col>
            </Row>
          </Container>
        </Form>
      </div>
    );
  }
}

export default UrlForm;

