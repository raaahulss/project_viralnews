import React, { Component } from 'react'

class ArticleEntry extends Component {
  constructor(props){
    super(props);
  }
  render() {
    if ("value" in this.props && this.props.value !== undefined && this.props.value !== "") {
      return(
        <p>
          {this.props.field}: {this.props.value}
          <br />
        </p>
      )
    } else {
      return(null);
    }
  }
}

export default ArticleEntry;
