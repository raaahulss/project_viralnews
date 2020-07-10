import React, { Component } from 'react'
import './css/privacy.css'

class Privacy extends Component {
  render() {
    return (
      <div className = "about_pad">
        <h2 className="api_title">
          We don't store your data, period.
        </h2>
        <div id="body_par">
          <p>
            We physically can't. We have nowhere to store it. We don't even have a server database to store it.
          </p>
          </div>
      </div>
    );
  }
}

export default Privacy;
