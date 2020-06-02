import React, {Component} from 'react'
import { Nav, Navbar} from 'react-bootstrap';

export const NavBar = () => (
  <Navbar bg="light" expand="lg">
    <Navbar.Brand href="#home">News Analyzer</Navbar.Brand>
    <Navbar.Toggle aria-controls="basic-navbar-nav" />
    <Navbar.Collapse id="basic-navbar-nav">
      <Nav className="mr-auto">
        <Nav.Link href="#home">Home</Nav.Link>
        <Nav.Link href="#link">Source</Nav.Link>
        <Nav.Link href="#ml">ML Documentation</Nav.Link>
        <Nav.Link href="#api">API Documentation</Nav.Link>
        <Nav.Link href="#about">About</Nav.Link>
      </Nav>
    </Navbar.Collapse>
  </Navbar>
)
