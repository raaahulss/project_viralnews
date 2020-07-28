import React, {Component} from 'react'
import {Nav} from 'react-bootstrap';
import '../css/navbar.css'

class NavBar extends Component {
  render() {
    return (
      <center id="navbar-center">
        <Nav fluid ariant="pills" className="justify-content-center" id="sticky-nav">
          <Nav.Item>
            <Nav.Link href="/">Home</Nav.Link>
          </Nav.Item>
          <div className="vline" />
          <Nav.Item>
            <Nav.Link href="https://github.com/raaahulss/project_viralnews">Source</Nav.Link>
          </Nav.Item>
          <div className="vline" />
          <Nav.Item>
            <Nav.Link href="/doc">API Documentation</Nav.Link>
          </Nav.Item>
          <div className="vline" />
          <Nav.Item>
            <Nav.Link href="/ml">ML Documentation</Nav.Link>
          </Nav.Item>
          <div className="vline" />
          <Nav.Item>
            <Nav.Link href="/about">About</Nav.Link>
          </Nav.Item>
          <div className="vline" />
          <Nav.Item>
            <Nav.Link href="/privacy">Privacy</Nav.Link>
          </Nav.Item>
        </Nav>
      </center>
    );
  }
}

export default NavBar;
