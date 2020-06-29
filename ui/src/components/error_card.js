import React, { Component } from 'react'
import '../css/error_card.css'

class ErrorCard extends Component {
  render() {
    return (
      <div className="input">
        <h2 className="error-page-title">Oops!!!<br /> There seems to be a problems.</h2>
        <h4 className="error-message">{this.props.error.err_code} : {this.props.error.err_msg}</h4>
        <h4 className="error-message">Please go back to the home page and retry...</h4>
      </div>
    )
  }
}

export default ErrorCard;
