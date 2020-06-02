import React, {Component} from 'react'
import { Nav, Navbar, Grid, Row, Col} from 'react-bootstrap';

class NavBar extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <Nav variant="pills" className="justify-content-center">
        <Nav.Item>
          <Nav.Link href="/">Home</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link href="https://github.com/raaahulss/project_viralnews">Source</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link href="/api">API Documentation</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link href="/ml">ML Documentation</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link href="/about">About</Nav.Link>
        </Nav.Item>
      </Nav>
    );
  }
}

export default NavBar;
