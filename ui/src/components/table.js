import React, {Component} from 'react'
import { ListGroup} from 'react-bootstrap';

class Table extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <ListGroup>
        <ListGroup.Item>API Call 1</ListGroup.Item>
        <ListGroup.Item>API Call 2</ListGroup.Item>
        <ListGroup.Item>API Call 3</ListGroup.Item>
        <ListGroup.Item>API Call 4</ListGroup.Item>
        <ListGroup.Item>API Call 5</ListGroup.Item>
      </ListGroup>
    );
  }
}

export default Table
