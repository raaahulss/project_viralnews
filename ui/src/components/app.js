import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch, Redirect } from "react-router-dom";
import NavBar from './navbar.js';
import Home from '../home.js';
import Api from '../api.js';
import Ml from '../ml.js';
import About from '../about.js';
import Dashboard from '../dashboard.js';
import Privacy from '../privacy.js';
import ErrorCard from './error_card.js';
import '../css/app.css'

class App extends Component {
  render() {
    return (
        <React.Fragment id="container">
          <Router>
            <NavBar />
              <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/index" component={Home} />
                <Route path="/doc" component={Api} />
                <Route path="/ml" component={Ml} />
                <Route path="/about" component={About} />
                <Route path="/dashboard" component={Dashboard} />
                <Route path="/privacy" component={Privacy} />
                <Route path="/error" component={ErrorCard} />
                <Redirect to="/" component={Home}/>
              </Switch>
          </Router>
        </React.Fragment>
    );
  }
}

export default App;
