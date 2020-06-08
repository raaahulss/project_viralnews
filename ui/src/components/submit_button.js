import React, { Component } from 'react';
import { Button, ButtonToolbar } from 'react-bootstrap';

class SubmitButton extends Component {
  constructor(props){
        super(props);
    }
  render() {
    return (
      <ButtonToolbar>
        <Button variant="primary" type="submit" size="lg" active>
          Analyze
        </Button>
      </ButtonToolbar>
    );
  }
}

export default () => (
  <div>
    <SubmitButton />
  </div>
);
